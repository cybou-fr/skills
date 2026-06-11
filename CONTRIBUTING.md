# Contributing to Cybou Skills

This repository contains external Cybou skills, policies, schemas, evals and trust metadata.

It does **not** contain Cybou runtime code.

## Contribution types

Accepted contribution types:

```text
new SKILL.md files
skill metadata fixes
policy rule improvements
eval scenarios
schema improvements
documentation improvements
output templates
tool adapter metadata
```

Not accepted here:

```text
cybou-core Rust code
runtime patches
CLI implementation patches
guest execution code
MicroVM implementation code
```

Those belong in the Cybou runtime repository.

## Skill contribution rules

Every skill must:

```text
have valid YAML frontmatter
have a stable id
have a clear description
declare required tools
declare risk level
use an existing output template or add one
avoid direct execution instructions
avoid prompt-injection patterns
avoid secret exposure
```

## Safety rule

A skill may propose reasoning and procedures. It must never claim execution authority.

```text
Skills improve reasoning.
Rust decides safety.
MicroVM contains execution.
Audit records everything.
```
