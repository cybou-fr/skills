---
name: deployment-planning
description: Prepare and review deployment plans without executing them by default. Use for releases, production deployments, staging deployments, rollback plans, database migrations, canary, blue-green, feature flags, gates, and post-deployment checks.
---

# Deployment Planning

## Default mode

Draft only. Execution requires approval.

## Deployment gates

- Gate 1: CI passed.
- Gate 2: security checks passed.
- Gate 3: migration reviewed.
- Gate 4: rollback exists.
- Gate 5: monitoring ready.
- Gate 6: approval received.

## Strategies

### Rolling
Good default for stateless services.

### Canary
Use for risky changes.

### Blue/green
Good for fast rollback.

### Feature flag
Good for progressive activation.

### Database migration
High risk. Check backward compatibility and backup.

## Rule

If rollback plan is missing, do not recommend production deployment.

## Approval required

- production deployment;
- production rollback;
- database migration;
- traffic switch;
- DNS change.

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
