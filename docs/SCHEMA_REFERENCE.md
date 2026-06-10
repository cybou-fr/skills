# Schema Reference

v6.2 adds machine-readable schemas for loader compatibility.

## Schemas

```text
schemas/skill_frontmatter.schema.json
schemas/registry.schema.json
schemas/policy_rule.schema.json
schemas/tool_classes.schema.json
schemas/eval_scenario.schema.json
schemas/loader_manifest.schema.json
```

## Why schemas exist

They give `cybou-core` a stable contract for consuming the external skills repository.

## Validation policy

The pack validator checks the practical constraints needed by the loader:

- all skill paths exist;
- all `SKILL.md` frontmatter parses as YAML;
- all output templates referenced by registry exist;
- all required tools are classified;
- all policy decisions are mapped to runtime verdicts;
- legacy runtime artifacts are absent.

JSON Schema files are intentionally permissive where future extension is expected.
