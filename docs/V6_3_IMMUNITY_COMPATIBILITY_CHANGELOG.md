# v6.3 Immunity Compatibility Changelog

## Added

- `immunity_mapping/`
- `immunity_mapping/immunity_manifest.yaml`
- `immunity_mapping/decision_mapping.yaml`
- `immunity_mapping/risk_mapping.yaml`
- `immunity_mapping/tool_class_mapping.yaml`
- `immunity_mapping/command_pattern_mapping.yaml`
- `immunity_mapping/sensitive_targets.yaml`
- `schemas/immunity_manifest.schema.json`
- `schemas/command_pattern_mapping.schema.json`
- `schemas/sensitive_targets.schema.json`
- `docs/IMMUNITY_COMPATIBILITY.md`
- `legacy-removed-rust-immunity-contract-sketch`
- `scripts/validate_immunity_compat_v6_3.py`

## Purpose

Make the pack directly useful for `immunity.rs` and `risk.rs` without introducing a new runtime.

## Non-goal

v6.3 does not execute commands and does not replace Rust immunity.
