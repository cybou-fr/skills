---
name: runtime-durable-audit-store
description: Implement and review durable append-only audit store with JSONL records, hash chaining, verification and export support.
---

# Runtime Durable Audit Store

Stores audit events as append-only JSONL records with sequence number, previous hash, record hash and verification support.

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
