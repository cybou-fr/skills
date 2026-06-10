---
name: secret-detection
description: Detect and safely report possible secrets in files, logs, CI output, repositories, environment variables, tickets, or pasted text. Use for API keys, tokens, private keys, credentials, database URLs, JWTs, cookies, leaked secrets, and secret exposure investigations.
---

# Secret Detection

## Default mode

Read-only and redacted.

## Detect

Look for:
- API keys;
- private keys;
- JWTs;
- OAuth tokens;
- DB URLs;
- cloud credentials;
- SSH keys;
- cookies;
- webhooks;
- `.env` content.

## Common hints

- AWS access keys often begin with `AKIA` or `ASIA`.
- GitHub tokens may begin with `ghp_` or `github_pat_`.
- Slack tokens often begin with `xoxb-`, `xoxp-`, or similar.
- Private keys often contain `BEGIN PRIVATE KEY`.
- JWTs usually have three dot-separated base64url parts.

## Tools if available

- gitleaks;
- trufflehog;
- detect-secrets.

## Report safely

Never show full secret. Use type-only or prefix/suffix redaction.

## Escalate

Use `secret-rotation-playbook` for rotation and `secops-incident-response` for suspected compromise.

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
