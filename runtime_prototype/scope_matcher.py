from __future__ import annotations
from typing import Any, Dict
from .models import NormalizedAction, ApprovalState

def action_matches_scope(action: NormalizedAction, scope: Dict[str, Any] | None) -> tuple[bool, list[str]]:
    if not scope:
        return True, ["no_scope_object"]
    denied = scope.get("denied_actions", []) or []
    allowed = scope.get("allowed_actions", []) or []
    if action.operation in denied:
        return False, [f"scope_denied_action:{action.operation}"]
    if allowed and "*" not in allowed and action.operation not in allowed:
        return False, [f"scope_operation_not_allowed:{action.operation}"]
    env = scope.get("environment")
    if env and env not in ["*", action.environment]:
        return False, [f"scope_environment_mismatch:{env}!={action.environment}"]
    targets = scope.get("targets")
    if targets and action.target and "*" not in targets and action.target not in targets:
        return False, [f"scope_target_mismatch:{action.target}"]
    return True, ["scope_match"]

def approval_matches_action(approval: ApprovalState, action: NormalizedAction) -> tuple[bool, list[str]]:
    if approval.status != "approved":
        return False, [f"approval_status:{approval.status}"]
    if not approval.is_valid_for(action):
        return False, ["approval_state_is_not_valid_for_action"]
    return True, ["approval_match"]
