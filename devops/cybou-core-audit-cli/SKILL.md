---
name: cybou-core-audit-cli
description: Implement and review CLI workflows for appending, listing, verifying and exporting audit/evidence records.
---

# Runtime Audit CLI

Provides append/list/verify/export workflows for prototype audit and evidence stores.

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
