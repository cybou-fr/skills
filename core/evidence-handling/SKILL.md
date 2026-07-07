---
name: evidence-handling
description: Preserve and summarize evidence for DevOps or SecOps incidents without destroying logs or modifying state. Use
  for outages, suspected breaches, suspicious activity, leaked secrets, forensic review, or audit preparation.
description_fr: Préserver et résumer les preuves lors d'incidents DevOps ou SecOps sans détruire les journaux ni modifier l'état. À utiliser pour les pannes, violations suspectes, activités anormales, secrets divulgués ou audits.
category: core
default_risk: low
default_mode: read_only
skill_format: operational_contract_v1
version: "10.1"
requires_tools:
  preferred:
    - mcp:filesystem:read_file
    - shell
  fallback:
    - shell
triggers:
  - evidence handling
  - incident evidence
  - forensic review
  - audit preparation
  - preserve logs
  - chain of custody
  - collecte de preuves
  - gestion des preuves
  - préserver journaux
  - revue forensique
---

# Evidence Handling

## 1. Use when

Use this skill during or after any DevOps or SecOps incident — outage, suspected breach, suspicious activity, leaked secret, data exfiltration, unauthorized access, or audit — to collect, preserve, and summarize evidence without corrupting the incident record.

## 2. Operating mode

Default mode: read_only. Evidence collection must never mutate logs, delete files, or modify system state. Any cleanup must wait until evidence is fully collected and secured.

## 3. Risk mapping

### low
- read logs with `journalctl`, `tail`, `cat`, `grep`;
- export/copy evidence to a secure location;
- compute file hashes (`sha256sum`).

### medium
- snapshot a running process or container state;
- export database query results to a file;
- capture network state (`ss -tlnp`, `netstat`, `tcpdump` read-only).

### high
- isolate a service or container to prevent further damage (approved only);
- rotate a compromised credential (approved only).

### critical
- delete, purge, or overwrite logs;
- run cleanup scripts before evidence collection is complete.

## 4. Preservation rules

1. **Do not delete logs** — ever, before evidence is secured.
2. **Do not purge queues** — preserve message order.
3. **Do not modify evidence files** — read-only copies only.
4. **Never run cleanup before evidence collection.**
5. Prefer `cp`, `rsync`, snapshot, or export — never move originals.
6. Always record the **timezone** of collection.
7. Always record **the exact command** used to collect evidence.
8. **Redact secrets** before sharing or logging evidence summaries.
9. Preserve the **original order of events** in timelines.
10. If compromise is suspected, avoid state-modifying commands unless approved.

## 5. Collection commands

```bash
# System logs
journalctl -u <service> --since "2h ago" --no-pager | head -500
journalctl -p err..crit --since "4h ago" --no-pager | head -200

# Auth and access logs
tail -n 500 /var/log/auth.log
tail -n 500 /var/log/syslog
grep -i "failed\|invalid\|unauthorized" /var/log/auth.log | tail -100

# Process snapshot
ps aux --sort=-%cpu | head -30
ss -tlnp

# File integrity
sha256sum <file>
stat -c '%y %a %U %G %n' <file>

# Active network connections
ss -antp
```

## 6. Chain-of-custody record

```markdown
## Chain of custody

- Collected by: <worker | operator name>
- Collected at: <ISO 8601 timestamp with timezone>
- From: <host / service / container>
- Method: <exact commands used>
- Stored at: <path or location>
- SHA256: <hash of collected file if applicable>
- Integrity concerns: <none | describe anomalies>
```

## 7. Stop / block conditions

- Stop if the next planned step is a cleanup, log rotation, or purge before collection is complete.
- Stop if a command would overwrite or truncate a log file.
- Do not share evidence that contains unredacted credentials.

## 8. Verify-before-finish

A task is not complete until:
- all relevant logs are copied or exported;
- chain-of-custody record is filled;
- hashes are computed for key evidence files;
- secrets in the evidence are redacted before any summary is shared.

## 9. Required output format

```markdown
## Evidence handling report

### Incident summary

### Time window

### Evidence collected

| Source | Method | Hash | Timezone |
|---|---|---|---|

### Chain of custody

### Redaction applied

### Integrity concerns

### Recommended next steps

### Risk classification
```
