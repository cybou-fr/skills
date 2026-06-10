---
name: evidence-handling
description: Preserve and summarize evidence for DevOps or SecOps incidents without destroying logs or modifying state. Use for outages, suspected breaches, suspicious activity, leaked secrets, forensic review, or audit preparation.
---

# Evidence Handling

## Rules

1. Do not delete logs.
2. Do not purge queues.
3. Do not modify evidence files.
4. Never run cleanup before evidence collection.
5. Prefer copy/snapshot/export.
6. Record time zone.
7. Record command used to collect evidence.
8. Redact secrets before sharing.
9. Keep original order of events.
10. If compromise is suspected, avoid state-modifying commands unless necessary and approved.

## Evidence summary

```md
## Evidence collected
- Source:
- Time window:
- Collection method:
- Integrity concerns:
- Redaction applied:
```

## Chain-of-custody-lite

Record:
- who collected;
- when;
- from where;
- how;
- where stored;
- hash if applicable.

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
