# Validation Report

Generated: 2026-06-10T22:42:34.308640+00:00

## v6.3 immunity compatibility status

```text
v6.1 validator: pass
v6.2 loader validator: pass
v6.3 immunity validator: pass
Errors: 0
Warnings: 0
```

## Structural counts

```text
Total files: 464
Skill files: 207
Registry skills: 207
Output templates: 139
Policy rule files: 13
Activity policy files: 2
Tool adapter files: 74
Scope object files: 6
Schema JSON files: 27
Schema total files: 29
Eval files: 41
Eval scenarios: 222
Immunity mapping files: 6
```

## Immunity mapping stats

```text
Command patterns: 18
Sensitive targets: 10
Decision mappings: 17
Risk levels: 4
```

## Added in v6.3

```text
immunity_mapping/
docs/IMMUNITY_COMPATIBILITY.md
docs/V6_3_IMMUNITY_COMPATIBILITY_CHANGELOG.md
docs/RUST_IMMUNITY_CONTRACT_SKETCH.rs
scripts/validate_immunity_compat_v6_3.py
schemas/immunity_manifest.schema.json
schemas/command_pattern_mapping.schema.json
schemas/sensitive_targets.schema.json
```
