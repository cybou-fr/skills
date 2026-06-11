---
name: cybou-core-audit-regression-suite
description: Create regression tests for append-only audit records, hash-chain verification, tamper detection, redacted evidence
  capture and export.
---

# Runtime Audit Regression Suite

Tests append/list/verify/export, tamper detection and redaction-aware evidence storage.

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
