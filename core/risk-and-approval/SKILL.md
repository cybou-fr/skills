---
name: risk-and-approval
description: Evaluate operational risk and decide whether the worker may proceed, stay read-only, draft only, or ask for human
  approval. Use before infrastructure changes, shell commands, deployments, IAM, secrets, database writes, incidents, or production
  actions.
description_fr: Évaluer le risque opérationnel et décider si le worker peut procéder, rester en lecture seule, rédiger uniquement ou demander une approbation humaine. À utiliser avant les changements d'infrastructure, commandes shell, déploiements, IAM, secrets, écritures en base ou actions en production.
category: core
default_risk: low
default_mode: read_only
skill_format: operational_contract_v1
version: "10.1"
requires_tools:
  preferred:
    - mcp:filesystem:read_file
  fallback:
    - shell
triggers:
  - risk evaluation
  - approval required
  - operational risk
  - risk assessment
  - évaluation du risque
  - approbation requise
  - risque opérationnel
---

# Risk and Approval

## 1. Use when

Use this skill before any action that could change system state, expose data, affect users, consume resources, or trigger side effects in production or unknown environments.

## 2. Operating mode

Default mode: read_only. Assessment itself is always safe. The outcome of the assessment determines the mode for the subsequent action.

## 3. Risk levels

### low
Read-only, no secrets, no production impact, no external side effects, fully reversible.

**→ Proceed without approval.**

### medium
Non-production changes, patch drafts, test execution, config edits in VM/sandbox, reversible actions with a known rollback path.

**→ Proceed with caution. Log actions. Verify after.**

### high
Production, security controls, IAM, secrets, customer data, significant cost impact, external communication, service restarts.

**→ Stop and request explicit human approval before proceeding.**

### critical
Irreversible or destructive: data loss, secret exposure, disabling security controls, dropping databases, deleting infrastructure, credential compromise.

**→ Hard stop. Do NOT proceed without verified written approval.**

## 4. Default rule

> If unsure, classify **one level higher** and stay read-only.

An unknown environment is always treated as **production** for risk purposes.

## 5. Risk scoring matrix

| Action | Default risk |
|---|---|
| `kubectl get pods`, `docker ps`, `git log` | low |
| `kubectl get pods -n production` | medium |
| `kubectl rollout restart deployment` in production | high |
| `kubectl delete namespace` in production | critical |
| `terraform plan` (read) | medium |
| `terraform apply` | high |
| `terraform destroy` | critical |
| `SELECT COUNT(*)` | low |
| `UPDATE` / `DELETE` in production | high |
| `DROP DATABASE` | critical |
| Create draft PR | low |
| Merge PR to main | medium |
| Deploy to production | high |
| Rotate leaked secret | high |
| Purge audit logs | critical |

## 6. Environment modifiers

| Environment | Risk modifier |
|---|---|
| local sandbox | −1 level (high → medium) |
| development | no change |
| staging | no change |
| production | +1 level (medium → high) |
| unknown | treat as production |
| customer environment | treat as critical |

## 7. Approval decision flow

```
Is risk LOW?  →  proceed.
Is risk MEDIUM in sandbox/dev?  →  proceed with logging.
Is risk HIGH or CRITICAL?  →  STOP → use approval-request skill → wait.
Is environment UNKNOWN?  →  treat as HIGH → STOP → use approval-request skill.
```

## 8. Verify-before-finish

After any approved mutating action:
- confirm the change took effect (status, diff, or read-back);
- confirm rollback path is still viable;
- log the action in the required output.

## 9. Required output format

```markdown
## Risk assessment

### Action evaluated

### Environment

### Risk classification

### Reasoning

### Decision

### Approval required

### Rollback path
```
