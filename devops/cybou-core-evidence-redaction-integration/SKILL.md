---
name: cybou-core-evidence-redaction-integration
description: Integrate redaction boundary with evidence capture so sensitive outputs are stored only after redaction and marked
  with redaction status.
---

# Runtime Evidence Redaction Integration

Evidence capture must pass through redaction first. Raw secret-bearing outputs must not be persisted.

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
