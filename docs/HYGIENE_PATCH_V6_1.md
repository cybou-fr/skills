# v6.1 Hygiene Patch

## Purpose

Prepare the pack for real ingestion by `cybou-core` and future publication as `cybou-fr/skills`.

## Changes

- Strict YAML frontmatter for all `SKILL.md` files.
- Removed `legacy-removed-runtime-prototype/`.
- Removed duplicated legacy test directories.
- Removed all `*.pyc` and `__pycache__`.
- Removed v5 prototype scripts.
- Canonical eval layout is now `evals/`.
- Added `integration/decision_mapping.yaml`.
- Added `integration/tool_classes.yaml`.
- Added clean validator: `scripts/validate_pack_v6_1.py`.

## Validation target

```text
Skill files: 207
Registry skills: 207
Output templates: 139
Eval files: 41
Eval scenarios: 222
Known tools: 64
```
