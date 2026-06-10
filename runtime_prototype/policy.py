from __future__ import annotations

from pathlib import Path
from .models import NormalizedAction, PolicyDecision, ApprovalState
from .policy_loader import load_policy_bundle, PolicyBundle
from .rule_matcher import match_tool_rules, DECISION_ORDER
from .risk_engine import risk_from_action
from .profile_engine import evaluate_profile_scope


def _decision_requires_approval(decision: str | None) -> bool:
    return bool(decision and "approval_required" in decision)


def _is_deny(decision: str | None) -> bool:
    return decision in {"deny", "deny_by_default", "refuse_or_escalate"}


def _strongest_decision(*decisions: str | None) -> str:
    out = None
    for d in decisions:
        if not d:
            continue
        if out is None or DECISION_ORDER.get(d, 0) > DECISION_ORDER.get(out, 0):
            out = d
    return out or "allow_read_only"


def _fallback_decision(action: NormalizedAction) -> tuple[str, str, list[str]]:
    raw = action.raw_input.lower()
    matched: list[str] = []
    if action.operation == "pipe_to_shell":
        return "deny_by_default", "critical", ["fallback:shell-pipe-to-shell"]
    if "rm -rf /" in raw:
        return "deny_by_default", "critical", ["fallback:shell-rm-root"]
    if "drop database" in raw or action.operation.lower() in ["drop", "truncate"]:
        return "deny_by_default", "critical", ["fallback:database-destructive"]
    if "system prompt" in raw and any(x in raw for x in ["reveal", "print", "dump", "extract"]):
        return "deny_by_default", "critical", ["fallback:secret-exfiltration"]
    if "jailbreak" in raw and any(x in raw for x in ["generate", "create", "write", "bypass"]):
        return "deny_by_default", "critical", ["fallback:ai-jailbreak-generation"]

    high = False
    if action.tool == "terraform" and action.operation in ["apply", "destroy", "state", "force-unlock"]:
        high = True; matched.append("fallback:terraform-high-risk")
    if action.tool == "kubectl" and action.operation in ["apply", "delete", "patch", "edit", "scale", "exec"]:
        high = True; matched.append("fallback:kubectl-high-risk")
    if action.tool == "cargo" and action.operation in ["publish", "install", "update", "add", "remove"]:
        high = True; matched.append("fallback:cargo-high-risk")
    if action.tool == "docker" and action.operation in ["rm", "rmi", "stop", "restart"]:
        high = True; matched.append("fallback:docker-high-risk")
    if action.tool == "git" and ("history_rewrite" in action.side_effects or action.operation in ["push", "reset", "clean", "rebase"]):
        high = True; matched.append("fallback:git-high-risk")
    if action.tool == "docker" and ("privileged_container" in action.side_effects or "docker_socket_mount" in action.side_effects):
        high = True; matched.append("fallback:docker-privileged")
    if "destructive" in action.side_effects or action.environment == "production":
        high = True; matched.append("fallback:side-effect-or-production")

    if high:
        return "approval_required", "high", matched
    if action.sensitive_data_possible:
        return "allow_read_only_and_redact", "medium", ["fallback:sensitive-data-possible"]
    return "allow_read_only", "low", ["fallback:read-only"]


def evaluate_policy(
    action: NormalizedAction,
    approval: ApprovalState | None = None,
    profile: str = "readonly_copilot",
    scope_name: str | None = None,
    policy_root: str | Path | None = None,
    policy_bundle: PolicyBundle | None = None,
) -> PolicyDecision:
    if policy_bundle is None:
        root = Path(policy_root) if policy_root else Path(__file__).resolve().parents[1]
        policy_bundle = load_policy_bundle(root)

    rule_result = match_tool_rules(action, policy_bundle)
    fallback_decision, fallback_risk, fallback_rules = _fallback_decision(action)
    profile_decision, profile_reasons = evaluate_profile_scope(action, policy_bundle, profile, scope_name)

    risk, risk_reasons = risk_from_action(action, policy_bundle, rule_result.risk or fallback_risk)
    decision = _strongest_decision(rule_result.decision, fallback_decision, profile_decision)

    if action.sensitive_data_possible and DECISION_ORDER.get(decision, 0) < DECISION_ORDER["approval_required"]:
        decision = "allow_read_only_and_redact"

    approval_required = _decision_requires_approval(decision)
    matched = []
    matched.extend(rule_result.matched_rules)
    matched.extend(fallback_rules)
    matched.extend(profile_reasons)
    matched.extend(risk_reasons)
    matched.extend([f"policy_error:{e}" for e in rule_result.errors])

    if approval_required and approval and approval.is_valid_for(action):
        decision = "allow_with_approval"
        approval_required = False
        matched.append("approval-valid")

    if _is_deny(decision):
        approval_required = False

    return PolicyDecision(
        decision=decision,
        risk=risk,
        tool=action.tool,
        normalized_action=action.to_dict(),
        matched_rules=matched,
        approval_required=approval_required,
        approval_scope=action.scope or action.target or action.environment,
        redaction_required=action.sensitive_data_possible or risk in ["high", "critical"],
        audit_required=True,
        reason="data-driven policy evaluation with safe fallback",
    )
