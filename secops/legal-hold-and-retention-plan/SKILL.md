---
name: legal-hold-and-retention-plan
description: Draft legal hold and retention plan for security evidence, audit logs, case records and exports without deleting
  or altering evidence.
---

# Legal Hold and Retention Plan

Plan retention and hold status; do not delete evidence.

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
