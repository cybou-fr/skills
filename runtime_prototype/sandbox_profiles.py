from __future__ import annotations
from pathlib import Path
from typing import Any, Dict
import yaml

def load_sandbox_profiles(root: str | Path) -> Dict[str, Any]:
    path = Path(root) / "sandbox_profiles.yaml"
    if not path.exists():
        return {"profiles": {}}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {"profiles": {}}

def select_sandbox_profile(action, decision, root: str | Path) -> tuple[str, dict, list[str]]:
    config = load_sandbox_profiles(root)
    profiles = config.get("profiles", {})
    reasons = []

    if decision.decision in ["deny", "deny_by_default", "refuse_or_escalate"]:
        return "blocked", profiles.get("blocked", {}), ["decision_denied"]
    if decision.approval_required:
        return "no_execution", profiles.get("no_execution", {}), ["approval_required_no_execution"]
    if decision.decision == "allow_with_approval":
        return "approval_required_execution", profiles.get("approval_required_execution", {}), ["valid_approval_simulate_only"]

    if action.tool == "cargo" and action.operation in ["check", "test", "fmt", "clippy", "metadata", "tree", "audit", "deny", "doc"]:
        return "repo_quality", profiles.get("repo_quality", {}), ["cargo_quality_command"]
    if action.tool == "http_fetch":
        return "network_fetch_restricted", profiles.get("network_fetch_restricted", {}), ["http_fetch"]
    if action.decision if False else False:
        pass
    return "readonly_local", profiles.get("readonly_local", {}), ["default_readonly_local"]
