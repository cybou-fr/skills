---
name: risk-and-approval
description: Evaluate operational risk and decide whether the worker may proceed, stay read-only, draft only, or ask for human
  approval. Use before infrastructure changes, shell commands, deployments, IAM, secrets, database writes, incidents, or production
  actions.
description_fr: Évaluer le risque opérationnel et décider si le worker peut procéder, rester en lecture seule, rédiger uniquement ou demander une approbation humaine. À utiliser avant les changements d’infrastructure, commandes shell, déploiements, IAM, secrets, écritures en base ou actions en production.
---

# Risk and Approval

## Default rule

If unsure, classify one level higher and stay read-only.

## Risk scoring

Use `risk_matrix.yaml` when runtime scoring is available.

## Risk levels

### Low
Read-only, no secrets, no production impact, no external side effects.

### Medium
Local or non-production changes, patch drafts, test execution, reversible actions.

### High
Production, security controls, IAM, secrets, customer data, cost impact, external communication.

### Critical
Irreversible or destructive actions, data loss, secret exposure, disabling security, deleting resources.

## Examples

| Action | Risk |
|---|---|
| `kubectl get pods` | medium if real cluster, low if local |
| `kubectl delete pod` in prod | high |
| `terraform plan` | medium/high depending target |
| `terraform destroy` | critical |
| `SELECT count(*)` | low |
| `DELETE FROM users` | critical |
| create PR draft | medium |
| merge PR | high |
| rotate leaked secret | high/critical |

## Approval request

Use the approval request template when needed.

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
