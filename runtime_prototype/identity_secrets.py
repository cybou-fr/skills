from __future__ import annotations
from typing import Any, Dict, List
import re, time
from .ioc_extractor import extract_iocs

SECRET_PATTERNS = {
    "aws_access_key_id": re.compile(r"AKIA[0-9A-Z]{16}"),
    "generic_token": re.compile(r"(?i)(token|secret|password|api[_-]?key)\s*[:=]\s*['\"]?([A-Za-z0-9_\-./+=]{8,})"),
    "bearer_token": re.compile(r"(?i)bearer\s+[A-Za-z0-9_\-./+=]{12,}"),
    "private_key_marker": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "github_token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
}

HIGH_RISK_SCOPES = {"Directory.ReadWrite.All", "User.ReadWrite.All", "Mail.ReadWrite", "Files.ReadWrite.All", "offline_access", "Application.ReadWrite.All"}
HIGH_RISK_KEY_ACTIONS = {"ScheduleKeyDeletion", "DisableKey", "PutKeyPolicy", "setIamPolicy", "delete_secret", "purge_secret"}

def classify_secret(text: str) -> Dict[str, Any]:
    findings = []
    for kind, pattern in SECRET_PATTERNS.items():
        for m in pattern.finditer(text):
            findings.append({
                "kind": kind,
                "start": m.start(),
                "end": m.end(),
                "value_redacted": True,
                "preview": "<REDACTED>",
            })
    severity = "high" if findings else "low"
    if any(f["kind"] in ["private_key_marker", "aws_access_key_id"] for f in findings):
        severity = "critical"
    return {
        "finding_count": len(findings),
        "severity": severity,
        "findings": findings,
        "read_only_next_steps": [
            "identify storage location and exposure window",
            "map consumers/dependencies",
            "check recent use logs without printing secret",
            "prepare rotation/revocation plan",
        ],
        "approval_required_actions": [
            "rotate secret",
            "revoke session/token",
            "delete exposed credential",
            "update dependent applications",
        ],
    }

def review_oauth_app(app: Dict[str, Any]) -> Dict[str, Any]:
    scopes = set(app.get("scopes", []) or [])
    risky = sorted(scopes.intersection(HIGH_RISK_SCOPES))
    redirect_uris = app.get("redirect_uris", []) or []
    reasons = []
    if risky:
        reasons.append("high_risk_scopes")
    if any(uri.startswith("http://") for uri in redirect_uris):
        reasons.append("insecure_redirect_uri")
    if app.get("publisher_verified") is False:
        reasons.append("unverified_publisher")
    severity = "high" if reasons else "low"
    return {
        "app_id": app.get("app_id"),
        "publisher": app.get("publisher"),
        "severity": severity,
        "risky_scopes": risky,
        "reasons": reasons,
        "approval_required_actions": ["remove consent", "disable app", "delete app credential"],
    }

def review_key_policy(policy: Dict[str, Any]) -> Dict[str, Any]:
    text = str(policy)
    findings = []
    if "*" in text:
        findings.append({"risk":"high","issue":"wildcard_principal_or_action"})
    for marker in ["kms:*", "PutKeyPolicy", "ScheduleKeyDeletion", "DisableKey", "setIamPolicy", "destroyCryptoKeyVersion"]:
        if marker.lower() in text.lower():
            findings.append({"risk":"high","issue":marker})
    if "Principal" in text and ":root" in text:
        findings.append({"risk":"medium","issue":"account_root_principal"})
    severity = "high" if any(f["risk"] == "high" for f in findings) else ("medium" if findings else "low")
    return {
        "severity": severity,
        "finding_count": len(findings),
        "findings": findings,
        "read_only_next_steps": ["collect key usage metadata", "review grants/bindings", "verify rotation and deletion window"],
        "approval_required_actions": ["change key policy", "disable/delete key", "revoke grant", "change rotation schedule"],
    }

def review_identity(principal: Dict[str, Any]) -> Dict[str, Any]:
    reasons = []
    if principal.get("privileged") and not principal.get("mfa_enabled", False):
        reasons.append("privileged_without_mfa")
    if principal.get("last_seen_days", 0) > 90:
        reasons.append("stale_principal")
    if principal.get("external") and principal.get("privileged"):
        reasons.append("external_privileged_principal")
    if principal.get("service_account") and principal.get("key_age_days", 0) > 90:
        reasons.append("stale_service_account_key")
    severity = "high" if any(x in reasons for x in ["privileged_without_mfa", "external_privileged_principal"]) else ("medium" if reasons else "low")
    return {
        "principal": principal.get("id") or principal.get("name"),
        "severity": severity,
        "reasons": reasons,
        "approval_required_actions": ["disable principal", "remove role", "revoke sessions", "rotate/delete service account key"],
    }
