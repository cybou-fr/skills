---
name: secret-rotation-playbook
description: Plan safe credential revocation and rotation after a suspected or confirmed secret leak. Use for API keys, cloud credentials, GitHub tokens, SSH keys, database passwords, webhook secrets, OAuth tokens, service account keys, and dependency mapping before rotation.
---

# Secret Rotation Playbook

## Default mode

Approval required for actual rotation.

## Dependency mapping

Before rotation identify:
- where secret is stored;
- which services use it;
- how config is deployed;
- whether dual-secret rotation is possible;
- whether restart is required;
- how to validate the new secret;
- rollback plan.

## Procedure

1. Identify secret type.
2. Identify owner/system.
3. Determine exposure window.
4. Check recent use logs.
5. Create replacement secret.
6. Update dependent services.
7. Test new secret.
8. Revoke old secret.
9. Monitor failures.
10. Document incident.

## Approval required

- creating new credential;
- revoking old credential;
- updating production config;
- restarting services.

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
