---
name: github-security-review
description: Review GitHub repository and organization security posture. Use for branch protection, Actions security, secrets
  exposure, deploy keys, GitHub Apps, repository visibility, Dependabot, code scanning, environments, and audit events.
---

# GitHub Security Review

## Default mode

Read-only.

## Review areas

- branch protection;
- required reviews;
- required status checks;
- repository visibility;
- deploy keys;
- GitHub Apps;
- Actions permissions;
- workflow secrets;
- Dependabot alerts;
- code scanning;
- environments and deployment approvals;
- audit log events.

## Red flags

- branch protection disabled;
- Actions write-all permissions;
- secrets available to unsafe workflows;
- unpinned third-party actions;
- public repository with sensitive history;
- deploy key with write access;
- environment without reviewers for production.

## Approval required

- changing repository settings;
- rotating secrets;
- disabling keys;
- modifying workflows;
- merging PRs.

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
