#!/usr/bin/env python3
"""Ensure migrated skills classify command templates into v7 command classes."""
from __future__ import annotations

import sys
from pathlib import Path

PILOT_SKILLS = [
    "devops/package-manager-safety/SKILL.md",
    "devops/linux-diagnostics/SKILL.md",
    "devops/kubernetes-readonly-triage/SKILL.md",
    "devops/database-safety/SKILL.md",
    "devops/terraform-plan-review/SKILL.md",
]
COMMAND_CLASSES = ["### read_only", "### guarded", "### approval_or_policy_required", "### blocked"]


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = []
    for rel in PILOT_SKILLS:
        path = root / rel
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        if "```bash" in text or "```sql" in text:
            missing = [c for c in COMMAND_CLASSES if c not in text]
            if missing:
                errors.append(f"{rel}: missing command classes {missing}")
        if "### blocked" in text:
            blocked = text.split("### blocked", 1)[1]
            if "```" not in blocked:
                errors.append(f"{rel}: blocked section has no command/code template")
    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        sys.exit(1)
    print("OK: command templates are classified")


if __name__ == "__main__":
    main()
