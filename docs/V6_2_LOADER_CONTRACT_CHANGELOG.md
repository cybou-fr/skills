# v6.2 Loader Contract Changelog

## Added

- `integration/loader_manifest.yaml`
- `schemas/skill_frontmatter.schema.json`
- `schemas/registry.schema.json`
- `schemas/policy_rule.schema.json`
- `schemas/tool_classes.schema.json`
- `schemas/eval_scenario.schema.json`
- `schemas/loader_manifest.schema.json`
- `docs/CYBOU_CORE_LOADER_CONTRACT.md`
- `docs/SCHEMA_REFERENCE.md`
- `scripts/validate_loader_contract_v6_2.py`

## Changed

- Package version bumped to `6.2.0`.
- README now treats loader contract as the main integration surface.
- `package.yaml` references loader manifest and schemas.

## Non-goal

v6.2 still does not add runtime execution logic. It remains an external corpus.
