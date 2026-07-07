---
name: approval-request
description: Create precise human approval requests for risky DevOps/SecOps actions. Use when the worker proposes production
  changes, deployments, restarts, IAM changes, secret rotation, database writes, firewall changes, destructive commands, restore
  operations, or external messages.
description_fr: Formuler des demandes d'approbation humaine précises pour les actions DevOps/SecOps risquées. À utiliser pour les changements en production, déploiements, redémarrages, IAM, rotation de secrets, écritures en base, ou commandes destructrices.
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
  - approval request
  - human approval
  - request confirmation
  - demande d'approbation
  - confirmation humaine
  - attente validation
  - approbation opérateur
---

# Approval Request

## 1. Use when

Use this skill to generate a human approval request whenever the `risk-and-approval` skill classifies an action as **high** or **critical**, or when the environment is unknown/production and the next step is mutating.

## 2. Operating mode

Default mode: read_only. Generating an approval request never modifies state — it only pauses execution until explicit confirmation is received.

## 3. Risk mapping

### low
- drafting and displaying an approval request without executing anything.

### critical
- proceeding with a high/critical action before receiving explicit approval.

## 4. Approval scope rules

A valid approval grants permission for **exactly one** of:
- one specific command on one specific target;
- one defined task in one defined environment;
- a time-bounded window for a specific operation.

**Do not treat vague or broad approvals as blanket permission.**

Examples of invalid approvals:
- "Go ahead" (no target specified)
- "Do what you need to" (no scope)
- "Yes" (after multiple pending questions)

Examples of valid approvals:
- "Yes, run `kubectl rollout restart deployment/api -n production` only."
- "Confirmed: create the MariaDB database `wp_prod` on the guest VM."

## 5. Approval request template

```markdown
## ⚠️ Approval required

**Target**: <host / cluster / database / service>

**Proposed action**:
```bash
<exact command or set of commands>
```

**Scope**: <this command only / this task only / time-bounded: X minutes>

**Reason**: <why this action is needed>

**Evidence**: <what was observed or diagnosed>

**Risk**: <high / critical — explanation>

**Rollback**: <how to undo if something goes wrong>

**Safer alternative** (if any): <lower-risk option>

Please confirm explicitly with the exact command before I proceed.
```

## 6. Stop / block conditions

- Do NOT execute until the operator's reply contains the exact proposed command or an unambiguous confirmation of it.
- If the operator says "yes" without specifying the target, re-ask with the target spelled out.
- If 5 minutes pass with no reply, escalate with a reminder — do not proceed autonomously.

## 7. Verify-before-finish

After receiving approval and executing the action:
- confirm the result;
- confirm rollback path is still available;
- include both the approval received and the outcome in the final report.

## 8. Required output format

```markdown
## Approval request report

### Action proposed

### Approval received

### Approval scope validated

### Execution result

### Rollback availability

### Risk classification
```
