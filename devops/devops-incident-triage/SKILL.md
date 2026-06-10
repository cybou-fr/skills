---
name: devops-incident-triage
description: Triage reliability incidents and outages. Use for service down, degraded performance, SEV events, production symptoms, customer impact, rollback decisions, incident summaries, status updates, and postmortem preparation.
---

# DevOps Incident Triage

## Default mode

Read-only until mitigation is approved.

## Procedure

1. Define what is broken.
2. Define impact and affected users.
3. Define start time and current status.
4. Check recent changes.
5. Collect evidence.
6. Build hypotheses.
7. Recommend mitigation options.
8. Prepare communication summary.

## Severity

- SEV-1: full outage, data loss, security breach.
- SEV-2: major degraded service.
- SEV-3: partial issue.
- SEV-4: minor issue.

## Communication templates

### Internal update

```md
Current status:
Impact:
What we know:
What we are checking:
Next update:
```

### Customer-facing update

```md
We are investigating an issue affecting ...
Impact:
Mitigation:
Next update:
```

## Rules

- no blame;
- no invented root cause;
- include confidence level;
- approval required for production mitigation.

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
