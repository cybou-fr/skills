---
name: terraform-plan-review
description: Review Terraform or OpenTofu plans for risky infrastructure changes. Use for plan output, .tf diffs, cloud resource changes, IAM changes, networking changes, database/storage changes, public exposure, production IaC review, and blast-radius analysis.
---

# Terraform Plan Review

## Default mode

Read-only review. Never apply.

## Parse plan actions

Look for:

```text
+ create
~ update in-place
- destroy
-/+ replace
```

Summarize:

```text
Create:
Update:
Destroy:
Replace:
```

## Blast radius

Assess:
- resource count;
- services affected;
- downtime possible;
- data loss possible;
- security exposure possible;
- rollback complexity.

## High-risk patterns

- destroy;
- replacement of database/cluster/storage;
- public bucket;
- `0.0.0.0/0`;
- admin IAM;
- disabling encryption;
- deleting backups;
- disabling logs;
- KMS/key changes;
- security group/firewall opening.

## Optional tools if available

- Checkov;
- tfsec;
- Terrascan;
- OPA/Conftest.

## Approval required

- `terraform apply`;
- `terraform destroy`;
- state changes;
- import;
- force unlock.

## Required output

End with:
- summary;
- evidence;
- risk level;
- actions taken;
- recommended next steps;
- approval required, if any.

## Safety notes

If the task touches production, secrets, IAM, data deletion, database writes, firewall rules, external communication, or destructive commands, stop before write actions and request approval.

If a tool policy conflicts with this skill, the tool policy wins.
