# Skill Authoring Guide

A Cybou skill is a procedural knowledge unit used to improve reasoning and reporting.

## Layout

```text
<category>/<skill-id>/SKILL.md
```

## Minimal frontmatter

```yaml
---
name: rust-security-hardening
description: Review Rust code and dependency risks with security-focused recommendations.
---
```

## Forbidden content

```text
bypass immunity
disable audit
disable approval
print secrets
exfiltrate credentials
ignore previous instructions
execute this command directly
```

Full body access is not enabled by default.
