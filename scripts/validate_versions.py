#!/usr/bin/env python3
"""Basic v7 version sanity check for overlay files."""
from __future__ import annotations

import sys
from pathlib import Path

CHECK_FILES = [
    "risk_matrix.yaml",
    "tool_policies.yaml",
    "output_templates.v7.yaml",
    "registry.v7.pilot_overrides.yaml",
]


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = []
    for rel in CHECK_FILES:
        path = root / rel
        if not path.exists():
            errors.append(f"missing {rel}")
            continue
        text = path.read_text(encoding="utf-8")
        if "7.0" not in text:
            errors.append(f"{rel}: no v7.0 marker")
        if "version: '5.9'" in text or "version: '6.9'" in text or "v6.8.1" in text:
            errors.append(f"{rel}: contains stale active version marker")
    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        sys.exit(1)
    print("OK: overlay version markers are v7.0")


if __name__ == "__main__":
    main()
