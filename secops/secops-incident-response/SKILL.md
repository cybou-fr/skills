---
name: secops-incident-response
description: Guide security incident response while preserving evidence. Use for suspected breach, account compromise, leaked
  secret, malware, data exfiltration, cloud compromise, container escape, malicious dependency, prompt/tool abuse, and suspicious
  admin activity.
---

# SecOps Incident Response

## Default behavior

Preserve evidence. Do not destroy logs. Do not rotate/delete without approval unless authorized.

## Phases

1. Prepare.
2. Identify.
3. Contain.
4. Eradicate.
5. Recover.
6. Lessons learned.

## Mini-playbooks

### Leaked secret
Use `secret-detection`, then `secret-rotation-playbook`.

### Compromised account
Preserve logs, disable/revoke with approval, check privilege changes.

### Public data exposure
Identify scope, remove exposure with approval, preserve evidence, assess access logs.

### Malicious dependency
Use `malicious-dependency-review`, isolate builds, check artifacts.

### Cloud compromise
Use `cloud-readonly-triage`, review audit logs, propose containment.

## Rule

Do not notify external parties unless explicitly authorized.

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
