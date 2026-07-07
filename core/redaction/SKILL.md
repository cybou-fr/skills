---
name: redaction
description: Redact secrets, credentials, tokens, PII, customer data, and sensitive operational output before summarizing,
  logging, or displaying results. Use for logs, files, CI output, secret scans, environment variables, database rows, and
  incident reports.
description_fr: Masquer les secrets, identifiants, tokens, données personnelles (PII) et sorties opérationnelles sensibles avant résumé, journalisation ou affichage. À utiliser pour les journaux, fichiers, sorties CI, scans de secrets et rapports d'incidents.
category: core
default_risk: low
default_mode: read_only
skill_format: operational_contract_v1
version: "10.1"
requires_tools:
  preferred:
    - mcp:filesystem:read_file
    - mcp:pattern_scanner:scan
  fallback:
    - shell
    - grep
triggers:
  - redact secrets
  - redaction
  - mask credentials
  - hide tokens
  - PII redaction
  - masquer secrets
  - masquer identifiants
  - données personnelles
  - masquage PII
---

# Redaction

## 1. Use when

Use this skill before including any command output, log content, file content, API response, environment variable dump, or scan result in a summary, report, or user-facing message.

## 2. Operating mode

Default mode: read_only. Redaction never modifies the source file; it only filters content shown in the output.

## 3. Risk mapping

### low
- scan and redact output before displaying;
- summarize counts of redacted items.

### medium
- overwrite a file on disk with redacted version (e.g. scrub a .env file before committing);
- requires write approval.

### critical
- exposing an unredacted real credential or private key in output or logs.

## 4. Redaction levels

| Level | Output | Use for |
|---|---|---|
| 1 — Type label | `[REDACTED_GITHUB_TOKEN]` | Low-sensitivity tokens |
| 2 — Prefix/suffix | `ghp_***...a3f9` | Debugging token identity |
| 3 — Aggregate | `3 API keys found` | Summary reports |
| 4 — Full omit | *(nothing)* | Private keys, JWTs, passwords, PII |

**Default for real credentials, JWTs, private keys, and customer PII: Level 4 (full omit).**

## 5. Always redact these

```text
API keys (any provider)        → Level 4
Private keys (RSA, EC, ed25519) → Level 4
OAuth / Bearer tokens          → Level 4
JWTs                           → Level 4
Passwords                      → Level 4
Session cookies                → Level 4
Database connection strings    → Level 4
Cloud access keys (AWS, GCP)   → Level 4
SSH private keys               → Level 4
Webhook signing secrets        → Level 4
Customer PII (name, email, SSN, IBAN) → Level 3 or 4
Internal IPs / subnets         → Level 2
Hostnames in prod              → Level 2
```

## 6. Common patterns to detect and mask

```text
AKIA[0-9A-Z]{16}                    # AWS access key
ghp_[A-Za-z0-9]{36}                # GitHub token
-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----  # private key block
password\s*=\s*\S+                  # password assignment
DATABASE_URL=.*@                    # DB connection string with creds
Bearer [A-Za-z0-9._~+/]+=*         # Bearer token
eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+ # JWT
```

## 7. Output disclosure statement

When redaction occurred, always include this line in the report:

```
⚠️ Sensitive values were redacted. Full secret values are not shown.
```

## 8. Stop / block conditions

- Stop immediately and do NOT display if the output contains an unmasked private key or plaintext password.
- Do not log the discovered secret count without redacting first.

## 9. Required output format

```markdown
## Redaction report

### Source

### Items redacted

| Type | Count | Level applied |
|---|---|---|

### Output (after redaction)

### Disclosure statement
```
