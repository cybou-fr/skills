#!/usr/bin/env python3
"""Validate v7 operational_contract_v1 pilot skills.

Usage:
  python scripts/validate_skill_contract_v7.py [repo_root]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## 1. Use when",
    "## 2. Do not use when",
    "## 3. Operating mode",
    "## 4. Risk mapping",
    "## 5. Preferred tool order",
    "## 6. Command templates",
    "## 7. Failure recovery",
    "## 8. Stop / block conditions",
    "## 9. Output contract",
    "## 10. Eval requirements",
]
REQUIRED_FRONTMATTER = [
    'version: "7.0"',
    'skill_format: operational_contract_v1',
    'requires_tools:',
    'policy_refs:',
    'output_template:',
]
PILOT_SKILLS = [
    "devops/package-manager-safety/SKILL.md",
    "devops/linux-diagnostics/SKILL.md",
    "devops/kubernetes-readonly-triage/SKILL.md",
    "devops/database-safety/SKILL.md",
    "devops/terraform-plan-review/SKILL.md",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        errors.append("missing YAML frontmatter")
    for marker in REQUIRED_FRONTMATTER:
        if marker not in text:
            errors.append(f"missing frontmatter marker: {marker}")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing section: {section}")
    for risk in ["### low", "### medium", "### high", "### critical"]:
        if risk not in text:
            errors.append(f"missing risk mapping: {risk}")
    for klass in ["### read_only", "### guarded", "### approval_or_policy_required", "### blocked"]:
        if klass not in text:
            errors.append(f"missing command class: {klass}")
    if re.search(r"ask\s+(the\s+)?user\s+for\s+approval", text, flags=re.I):
        errors.append("contains human-runbook approval wording")
    if "rm -rf /" in text and "### blocked" not in text:
        errors.append("destructive command appears without blocked section")
    return errors


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    all_errors: list[str] = []
    for rel in PILOT_SKILLS:
        path = root / rel
        if not path.exists():
            all_errors.append(f"missing pilot skill: {rel}")
            continue
        errors = validate_file(path)
        all_errors.extend(f"{rel}: {e}" for e in errors)
    if all_errors:
        for err in all_errors:
            print(f"FAIL: {err}")
        sys.exit(1)
    print("OK: v7 operational_contract_v1 pilot skills validated")


if __name__ == "__main__":
    main()
