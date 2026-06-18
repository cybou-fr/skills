# Operational Contract v1

`operational_contract_v1` is the v7.0 skill format for autonomous Cybou agents and local fine-tuned workers such as Strix.

The format changes a skill from a human runbook into an executable decision unit. A v7 skill must specify when it applies, which tools to prefer, which commands are read-only, which actions are guarded or blocked, how failures are recovered, how risk is classified, and which output contract must be emitted.

## Required frontmatter

```yaml
---
name: example-skill
version: "7.0"
skill_format: operational_contract_v1
category: devops
default_mode: read_only
default_risk: low
requires_tools:
  preferred:
    - mcp:filesystem:read_file
  fallback:
    - shell
policy_refs:
  - policy_rules/shell.yaml
output_template: example_report
---
```

Allowed `default_mode` values:

```text
read_only
review_only
guarded
blocked
```

Allowed risk values:

```text
low
medium
high
critical
```

## Required sections

Every migrated operational skill must contain:

```text
## 1. Use when
## 2. Do not use when
## 3. Operating mode
## 4. Risk mapping
## 5. Preferred tool order
## 6. Command templates
## 7. Failure recovery
## 8. Stop / block conditions
## 9. Output contract
## 10. Eval requirements
```

## Command classification

Every operational command must be placed under one of these classes:

```text
read_only
guarded
approval_or_policy_required
blocked
```

No command template should be left unclassified.

## Tool preference

Prefer host-governed MCP tools for host files, repository diffs, GitHub, Kubernetes, cloud APIs, secrets, search, and external data. Use guest shell only for VM-local inspection or execution. Never use shell to bypass host policy, connector visibility, approval boundaries, or secret controls.

## Autonomy semantics

Avoid human-runbook phrasing such as “ask the user for approval.” Instead, express the runtime boundary:

```text
If the action exceeds the VM autonomy envelope or runtime policy, do not execute it. Emit a blocked/high-risk decision or approval_request artifact for the host policy layer.
```

VM-local read-only inspection is usually low risk. VM-local reversible changes are medium if policy allows. Unknown or production writes are high. Destructive or irreversible actions are critical and blocked by default.
