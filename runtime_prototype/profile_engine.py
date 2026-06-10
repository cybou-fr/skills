from __future__ import annotations

from .models import NormalizedAction


def evaluate_profile_scope(action: NormalizedAction, bundle, profile: str = "readonly_copilot", scope_name: str | None = None) -> tuple[str | None, list[str]]:
    reasons: list[str] = []
    profiles = bundle.autonomy_profiles.get("profiles", {}) or {}
    profile_obj = profiles.get(profile, {})
    matrix = ((bundle.profile_decision_matrix.get("profiles") or {}).get(profile) or {})

    if profile_obj:
        denied = profile_obj.get("denied", []) or []
        for d in denied:
            if isinstance(d, str) and d and d in action.raw_input.lower():
                reasons.append(f"profile_denied:{profile}:{d}")
                return "deny_by_default", reasons

    if profile == "readonly_copilot" and ("write" in action.side_effects or "destructive" in action.side_effects):
        reasons.append("readonly_profile_blocks_write")
        return "approval_required", reasons

    tool_matrix = matrix.get(action.tool)
    if isinstance(tool_matrix, dict):
        op_decision = tool_matrix.get(action.operation)
        if op_decision:
            reasons.append(f"profile_matrix:{profile}.{action.tool}.{action.operation}={op_decision}")
            return op_decision, reasons

    if scope_name:
        scope = bundle.scope_objects.get(scope_name)
        if scope:
            denied_actions = scope.get("denied_actions", []) or []
            allowed_actions = scope.get("allowed_actions", []) or []
            if action.operation in denied_actions:
                reasons.append(f"scope_denied:{scope_name}")
                return "deny_by_default", reasons
            if allowed_actions and action.operation not in allowed_actions and "*" not in allowed_actions:
                reasons.append(f"scope_action_not_listed:{scope_name}")
                return "approval_required_with_scope", reasons

    return None, reasons
