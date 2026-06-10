---
name: security-log-review
description: Review security logs and audit events for suspicious activity. Use for auth logs, cloud audit logs, IdP events, WAF logs, VPN logs, Kubernetes audit logs, GitHub audit logs, SIEM alerts, brute force, suspicious login, privilege escalation, and exfiltration signals.
---

# Security Log Review

## Default mode

Read-only.

## Sources and examples

### GitHub audit
- deploy key created;
- secret accessed;
- repository visibility changed;
- branch protection disabled.

### AWS CloudTrail
- `CreateAccessKey`;
- `PutBucketPolicy`;
- `AuthorizeSecurityGroupIngress`;
- `ConsoleLogin`;
- `AssumeRole`.

### Kubernetes audit
- `get secrets`;
- `exec into pod`;
- privileged pod creation;
- clusterrolebinding creation.

### IdP
- MFA disabled;
- impossible travel;
- new admin;
- repeated failures then success.

## Confidence scoring

- Low: isolated anomaly.
- Medium: related suspicious events.
- High: suspicious access plus privilege or data access.
- Critical: confirmed exfiltration, persistence, or compromise.

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
