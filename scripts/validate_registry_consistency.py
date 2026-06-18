#!/usr/bin/env python3
"""Validate pilot override registry paths exist in the working tree.

This script intentionally validates the pilot override file rather than replacing the full registry.
For full migration, merge registry.v7.pilot_overrides.yaml into registry.yaml and extend this script
against all 207 skills.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    registry = root / "registry.v7.pilot_overrides.yaml"
    if not registry.exists():
        print("FAIL: registry.v7.pilot_overrides.yaml missing")
        sys.exit(1)
    text = registry.read_text(encoding="utf-8")
    paths = re.findall(r"path:\s*([^\n]+)", text)
    errors = []
    for p in paths:
        rel = p.strip().strip('"').strip("'")
        if not (root / rel).exists():
            errors.append(f"missing skill path: {rel}")
    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        sys.exit(1)
    print(f"OK: {len(paths)} pilot registry paths exist")


if __name__ == "__main__":
    main()
