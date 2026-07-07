---
name: approval-request
description: Create precise human approval requests for risky DevOps/SecOps actions. Use when the worker proposes production
  changes, deployments, restarts, IAM changes, secret rotation, database writes, firewall changes, destructive commands, restore
  operations, or external messages.
description_fr: Formuler des demandes d’approbation humaine précises pour les actions DevOps/SecOps risquées. À utiliser pour les changements en production, déploiements, redémarrages, IAM, rotation de secrets, écritures en base, ou commandes destructrices.
---

# Approval Request

## Approval scope

Approval must be scoped:

- one command only;
- one task only;
- time-bounded approval;
- environment-specific approval.

Do not treat vague approval as broad permission.

## Template

```md
## Approval required

Target:
...

Proposed action:
...

Approval scope:
...

Reason:
...

Evidence:
...

Risk:
...

Rollback:
...

Safer alternative:
...

Please confirm explicitly before I proceed.
```

## Good approval request

> Please confirm whether I may run `kubectl rollout restart deployment/api -n production`. Approval applies only to this command.

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
