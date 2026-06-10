from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List
import re

from .models import NormalizedAction

RISK_ORDER = {"low": 1, "medium": 2, "high": 3, "critical": 4}
DECISION_ORDER = {
    "allow_read_only": 1,
    "allow_read_only_and_redact": 2,
    "allow_draft": 2,
    "allow_with_approval": 3,
    "approval_required": 4,
    "approval_required_with_scope": 4,
    "approval_required_with_scope_and_rate_limit": 4,
    "approval_required_with_sandbox_and_time_limit": 4,
    "deny": 5,
    "deny_by_default": 5,
    "refuse_or_escalate": 5,
}


@dataclass
class RuleMatchResult:
    matched_rules: List[str]
    decision: str | None
    risk: str | None
    errors: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "matched_rules": self.matched_rules,
            "decision": self.decision,
            "risk": self.risk,
            "errors": self.errors,
        }


def _strongest_risk(a: str | None, b: str | None) -> str | None:
    if not a:
        return b
    if not b:
        return a
    return a if RISK_ORDER.get(a, 0) >= RISK_ORDER.get(b, 0) else b


def _strongest_decision(a: str | None, b: str | None) -> str | None:
    if not a:
        return b
    if not b:
        return a
    return a if DECISION_ORDER.get(a, 0) >= DECISION_ORDER.get(b, 0) else b


def _candidate_rule_keys(tool: str) -> list[str]:
    keys = [tool]
    if tool == "cargo":
        keys.append("rust_toolchain")
    if tool == "log_reader":
        keys.append("shell")
    if tool == "http_fetch":
        keys.append("http_fetch")
    return list(dict.fromkeys(keys))


def match_tool_rules(action: NormalizedAction, policy_bundle) -> RuleMatchResult:
    errors: List[str] = []
    matched: List[str] = []
    final_decision: str | None = None
    final_risk: str | None = None

    for key in _candidate_rule_keys(action.tool):
        rules_file = policy_bundle.policy_rules.get(key)
        if not rules_file:
            continue
        for rule in rules_file.get("rules", []) or []:
            rid = rule.get("id", "<unknown>")
            pattern = rule.get("match_regex")
            if not pattern:
                continue
            try:
                if re.search(pattern, action.raw_input, re.IGNORECASE):
                    matched.append(rid)
                    final_decision = _strongest_decision(final_decision, rule.get("decision"))
                    final_risk = _strongest_risk(final_risk, rule.get("risk"))
            except re.error as exc:
                errors.append(f"{key}:{rid}: invalid regex: {exc}")

    return RuleMatchResult(matched, final_decision, final_risk, errors)
