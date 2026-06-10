---
name: runtime-tamper-evidence
description: Implement and review hash-chain tamper-evidence logic for audit JSONL records and evidence metadata.
---

# Runtime Tamper Evidence

Detects deleted/modified/reordered audit records through previous-hash and record-hash verification.

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
