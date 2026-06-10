---
name: runtime-evidence-store
description: Implement and review evidence store for redacted tool outputs, command decisions, file references, screenshots/log
  snippets and structured evidence metadata.
---

# Runtime Evidence Store

Stores evidence records linked to audit events and policy decisions. Evidence content must be redacted before storage.

## Runtime enforcement rule

This skill belongs to durable audit and evidence handling.

Audit and evidence records must be append-only in normal operation, redaction-aware, linkable to task/action/decision IDs, and verifiable for tampering. Evidence must never intentionally store secret values.

## Required output

End with:

- audit/evidence record type;
- storage path;
- hash/tamper status;
- redaction status;
- linked task/action/decision IDs;
- export behavior;
- tests required.
