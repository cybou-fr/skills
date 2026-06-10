from __future__ import annotations
from typing import Any, Dict, List
import re, time
from .ioc_extractor import extract_iocs

HIGH_RISK_AWS = {"DeleteTrail", "StopLogging", "PutBucketPolicy", "CreateAccessKey", "AttachUserPolicy", "PutUserPolicy", "AssumeRole", "UpdateAssumeRolePolicy"}
HIGH_RISK_AZURE = {"Microsoft.Authorization/roleAssignments/write", "Microsoft.KeyVault/vaults/secrets/read", "Microsoft.Network/networkSecurityGroups/write"}
HIGH_RISK_GCP = {"SetIamPolicy", "CreateServiceAccountKey", "compute.firewalls.insert", "logging.sinks.delete"}

def provider_from_event(event: Dict[str, Any]) -> str:
    text = str(event).lower()
    if "eventname" in text or "guardduty" in text or "cloudtrail" in text or "aws" in text:
        return "aws"
    if "operationname" in text or "entra" in text or "azure" in text:
        return "azure"
    if "protoPayload" in event or "gcp" in text or "google" in text:
        return "gcp"
    return event.get("provider", "unknown")

def triage_cloud_event(event: Dict[str, Any]) -> Dict[str, Any]:
    provider = provider_from_event(event)
    text = str(event)
    iocs = extract_iocs(text)
    severity = "medium"
    reasons: List[str] = []
    identity = event.get("userIdentity") or event.get("principal") or event.get("principalEmail") or event.get("caller") or event.get("identity")
    resource = event.get("resource") or event.get("resourceName") or event.get("arn") or event.get("asset") or event.get("project")
    action = event.get("eventName") or event.get("operationName") or event.get("methodName") or event.get("action")

    if provider == "aws" and action in HIGH_RISK_AWS:
        severity = "high"; reasons.append(f"aws_high_risk_action:{action}")
    if provider == "azure" and action in HIGH_RISK_AZURE:
        severity = "high"; reasons.append(f"azure_high_risk_action:{action}")
    if provider == "gcp" and action in HIGH_RISK_GCP:
        severity = "high"; reasons.append(f"gcp_high_risk_action:{action}")
    if any(x in text.lower() for x in ["disable", "stoplogging", "deletetrail", "createaccesskey", "external", "anomalous", "malicious", "exfiltration"]):
        severity = "high"; reasons.append("suspicious_keyword")
    if any(x in text.lower() for x in ["critical", "credential", "root", "admin", "owner"]):
        severity = "critical"; reasons.append("critical_identity_or_credential_keyword")

    return {
        "provider": provider,
        "severity": severity,
        "identity": identity,
        "resource": resource,
        "action": action,
        "iocs": iocs,
        "reasons": reasons,
        "read_only_next_steps": [
            "collect related audit events in the same time window",
            "verify MFA/session context and source IP reputation",
            "check related IAM/role changes",
            "preserve evidence and build incident timeline",
        ],
        "approval_required_actions": [
            "disable identity or revoke sessions",
            "change IAM/RBAC policy",
            "quarantine resource",
            "suppress/archive finding",
            "delete or modify logging configuration",
        ],
    }

def least_privilege_review(policy: Dict[str, Any]) -> Dict[str, Any]:
    text = str(policy)
    findings = []
    if "*" in text:
        findings.append({"risk":"high","issue":"wildcard_permission_or_resource"})
    for dangerous in ["iam:PassRole", "sts:AssumeRole", "iam:AttachUserPolicy", "iam:CreateAccessKey", "Microsoft.Authorization/roleAssignments/write", "resourcemanager.projects.setIamPolicy"]:
        if dangerous.lower() in text.lower():
            findings.append({"risk":"high","issue":dangerous})
    return {
        "finding_count": len(findings),
        "findings": findings,
        "recommendation": "draft least-privilege diff; do not mutate IAM without approval",
    }
