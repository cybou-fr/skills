# Skill Corpus Format

The corpus is designed to be consumed by a Cybou loader in metadata-only mode first.

## Canonical directories

```text
core/
devops/
secops/
productivity/
policy_rules/
activity_policies/
tool_adapters/
scope_objects/
schemas/
evals/
integration/
immunity_mapping/
docs/
examples/
scripts/
```

## First-load behavior

```text
load registry.yaml
parse SKILL.md frontmatter only
validate paths/templates/tools
verify file hashes
check signature status
classify metadata as metadata_trusted
keep full bodies unavailable until vetting
```

## Public repository expectation

This repository can be public or private. Enterprise deployments should pin a signed release.
