# Contributing to Cybou Skills

This repository contains the external Cybou skills corpus. It does not contain Cybou runtime code.

## What can be contributed

```text
SKILL.md files
output templates
policy metadata
eval scenarios
schema improvements
documentation
validator improvements
```

## What must not be contributed

```text
Cybou Core Rust implementation
MicroVM code
guest execution code
CLI implementation patches
runtime patches
secrets or credentials
```

## Skill PR checklist

```text
1. Put the skill in the correct category directory.
2. Add valid YAML frontmatter.
3. Use a stable lowercase kebab-case id.
4. Avoid direct execution instructions.
5. Avoid prompt injection patterns.
6. Avoid secret exposure.
7. Run python scripts/validate_all.py.
```
