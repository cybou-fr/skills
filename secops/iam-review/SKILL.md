---
name: iam-review
description: Review IAM users, roles, service accounts, trust policies, cloud permissions, and access risks. Use for AWS IAM, GCP IAM, Azure RBAC, wildcard permissions, admin access, privilege escalation, long-lived keys, and least-privilege recommendations.
---

# IAM Review

## Default mode

Read-only.

## Generic checks

- wildcard actions;
- wildcard resources;
- admin privileges;
- long-lived access keys;
- unused accounts;
- no MFA;
- broad trust;
- ability to modify IAM;
- ability to read secrets;
- ability to disable logs.

## Privilege escalation examples

### AWS
- `iam:PassRole` + `ec2:RunInstances`;
- `lambda:UpdateFunctionCode`;
- `cloudformation:*`;
- broad `sts:AssumeRole`.

### GCP
- `roles/iam.serviceAccountTokenCreator`;
- service account key creation;
- project Owner.

### Azure
- User Access Administrator;
- Contributor + role assignment path.

## Approval required

- changing IAM;
- deleting identities;
- rotating keys;
- disabling access.

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
