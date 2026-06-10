from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict
import yaml


@dataclass
class PolicyBundle:
    root: Path
    risk_matrix: Dict[str, Any] = field(default_factory=dict)
    tool_policies: Dict[str, Any] = field(default_factory=dict)
    policy_rules: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    activity_policies: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    autonomy_profiles: Dict[str, Any] = field(default_factory=dict)
    profile_decision_matrix: Dict[str, Any] = field(default_factory=dict)
    scope_objects: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    def to_summary(self) -> Dict[str, Any]:
        return {
            "risk_matrix_version": self.risk_matrix.get("version"),
            "tool_policy_count": len(self.tool_policies.get("tools", {})),
            "policy_rule_files": sorted(self.policy_rules.keys()),
            "activity_policy_files": sorted(self.activity_policies.keys()),
            "autonomy_profiles": sorted((self.autonomy_profiles.get("profiles") or {}).keys()),
            "profile_decision_matrix_version": self.profile_decision_matrix.get("version"),
            "scope_objects": sorted(self.scope_objects.keys()),
        }


def _load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_policy_bundle(root: str | Path) -> PolicyBundle:
    root = Path(root)
    bundle = PolicyBundle(root=root)
    bundle.risk_matrix = _load_yaml(root / "risk_matrix.yaml")
    bundle.tool_policies = _load_yaml(root / "tool_policies.yaml")
    bundle.autonomy_profiles = _load_yaml(root / "autonomy_profiles.yaml")
    bundle.profile_decision_matrix = _load_yaml(root / "profile_decision_matrix.yaml")

    for path in sorted((root / "policy_rules").glob("*.yaml")) if (root / "policy_rules").exists() else []:
        bundle.policy_rules[path.stem] = _load_yaml(path)
    for path in sorted((root / "activity_policies").glob("*.yaml")) if (root / "activity_policies").exists() else []:
        bundle.activity_policies[path.stem] = _load_yaml(path)
    for path in sorted((root / "scope_objects").glob("*.yaml")) if (root / "scope_objects").exists() else []:
        bundle.scope_objects[path.stem] = _load_yaml(path)
    return bundle
