from __future__ import annotations

from .models import NormalizedAction
from .rule_matcher import RISK_ORDER


def max_risk(*risks: str | None) -> str:
    out = "low"
    for r in risks:
        if r and RISK_ORDER.get(r, 0) > RISK_ORDER.get(out, 0):
            out = r
    return out


def risk_from_action(action: NormalizedAction, bundle, rule_risk: str | None = None) -> tuple[str, list[str]]:
    reasons: list[str] = []
    risk = rule_risk or "low"
    low = action.raw_input.lower()
    floors = bundle.risk_matrix.get("risk_floor", {}) or {}

    floor_candidates = []
    if action.operation == "pipe_to_shell":
        floor_candidates.append("curl_pipe_shell")
    if "rm -rf /" in low:
        floor_candidates.append("rm_recursive_root")
    if "drop database" in low:
        floor_candidates.append("database_drop")
    if action.tool == "terraform" and action.operation == "destroy":
        floor_candidates.append("terraform_destroy")
    if action.tool == "kubectl" and action.operation == "delete":
        floor_candidates.append("kubectl_delete_namespace")
    if action.tool == "cargo" and action.operation == "publish":
        floor_candidates.extend(["cargo_publish", "crate_publish"])
    if "jailbreak" in low and any(x in low for x in ["generate", "create", "write", "bypass"]):
        floor_candidates.append("jailbreak_generation")

    for key in floor_candidates:
        if key in floors:
            risk = max_risk(risk, floors[key])
            reasons.append(f"risk_floor:{key}={floors[key]}")

    if "destructive" in action.side_effects:
        risk = max_risk(risk, "high")
        reasons.append("side_effect:destructive")
    if "write" in action.side_effects:
        risk = max_risk(risk, "medium")
        reasons.append("side_effect:write")
    if action.environment == "production":
        risk = max_risk(risk, "high")
        reasons.append("environment:production")
    if action.sensitive_data_possible:
        risk = max_risk(risk, "medium")
        reasons.append("sensitive_data_possible")

    return risk, reasons
