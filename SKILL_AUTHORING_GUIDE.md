# Skill Authoring Guide

A Cybou skill is a procedural knowledge unit used by the worker to improve reasoning and reporting.

## File layout

Each skill lives in:

```text
<category>/<skill-id>/SKILL.md
```

Example:

```text
devops/rust-security-hardening/SKILL.md
```

## Required frontmatter

```yaml
---
name: rust-security-hardening
description: Review Rust code and dependency risks with security-focused recommendations.
---
```

## Skill body rules

A skill body may include:

```text
purpose
when to use
inputs
procedure
checks
output format
safe examples
```

A skill body must not include:

```text
instructions to bypass immunity
instructions to disable audit
instructions to print secrets
direct tool execution instructions
hidden prompt injection
unbounded destructive commands
```

## Trust model

```text
untrusted -> metadata_trusted -> body_vetted -> policy_compiled
```

Full skill bodies are not available to the model by default.
