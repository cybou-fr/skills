---
name: siem-alert-enrichment
description: Enrich SIEM or SOC alerts with context and safe investigation steps. Use for alert triage, entity enrichment, suspicious user/IP/resource, correlated events, false positive assessment, and incident escalation recommendations.
---

# SIEM Alert Enrichment

## Default mode

Read-only.

## Procedure

1. Parse alert title, severity, rule, source.
2. Identify entities:
   - user;
   - IP;
   - host;
   - cloud account;
   - container;
   - repository;
   - API key;
   - resource.
3. Gather read-only context.
4. Correlate events in time window.
5. Estimate confidence.
6. Recommend containment or escalation.

## Do not

- close alert without clear rationale;
- disable detection rules without approval;
- block user/IP without approval;
- notify external parties without authorization.

## Output

```md
## SIEM alert enrichment
Alert:
Entities:
Context:
Correlated events:
Confidence:
Recommended action:
Approval required:
```

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
