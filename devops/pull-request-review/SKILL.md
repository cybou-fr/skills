---
name: pull-request-review
description: Review pull requests or merge requests for DevOps, SecOps, reliability, deployment, CI/CD, dependency, Docker,
  Kubernetes, Terraform, IAM, database migration, and secret exposure risks. Use for PR/MR diff review and safe review comments.
---

# Pull Request Review

## Default mode

Read-only review. Do not merge.

## Review focus

Check changes to:
- CI/CD;
- dependencies;
- Dockerfile;
- Kubernetes manifests;
- Terraform;
- IAM;
- database migrations;
- auth/security code;
- logging of sensitive data;
- scripts;
- package manager files.

## Finding levels

- Blocking: must fix before merge.
- High: serious risk.
- Medium: should fix.
- Nit: minor issue.
- Question: clarification needed.

## Output

```md
## PR review summary

Blocking findings:
High findings:
Medium findings:
Questions:
Suggested tests:
```

## Approval required

- merging;
- pushing commits;
- modifying branch;
- triggering production deployment.

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
