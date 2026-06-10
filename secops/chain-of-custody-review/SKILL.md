---
name: chain-of-custody-review
description: 'Review chain-of-custody integrity: who collected evidence, when, from where, hash verification, transfers and
  tamper status.'
---

# Chain of Custody Review

Verify evidence custody and identify gaps that weaken forensic confidence.

## Runtime enforcement rule

This skill belongs to incident forensics and case management.

Forensic workflows must preserve evidence, maintain chain-of-custody metadata, avoid destructive collection, redact secrets before model exposure, and distinguish investigative notes from confirmed facts. Deleting evidence, altering audit history, suppressing alerts or mutating production containment controls requires approval or must be denied.

## Required output

End with:

- case ID;
- incident phase;
- evidence/artifacts;
- chain-of-custody status;
- timeline confidence;
- open questions;
- next read-only actions;
- approval-required actions.
