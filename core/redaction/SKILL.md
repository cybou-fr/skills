---
name: redaction
description: Redact secrets, credentials, tokens, PII, customer data, and sensitive operational output before summarizing,
  logging, or displaying results. Use for logs, files, CI output, secret scans, environment variables, database rows, and
  incident reports.
---

# Redaction

## Rule

Never reveal full secrets.

## Redaction levels

- Level 1: type only, e.g. `[REDACTED_GITHUB_TOKEN]`.
- Level 2: prefix/suffix only, e.g. `ghp_...abcd`.
- Level 3: aggregate only, e.g. `3 tokens found`.
- Level 4: omit completely.

Use the strictest level for real credentials, JWTs, private keys, and customer secrets.

## Redact these

- API keys;
- private keys;
- OAuth tokens;
- JWTs;
- session cookies;
- passwords;
- database URLs;
- cloud credentials;
- SSH keys;
- webhook URLs;
- customer PII;
- access tokens.

## Output statement

When redaction occurred, include:

```md
Sensitive values were redacted. Full secret values are not shown.
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
