---
name: incident-case-record-management
description: Create and maintain incident case records with severity, status, owner, affected assets, evidence links, notes
  and audit references.
---

# Incident Case Record Management

Manage structured incident case records while preserving evidence and separating notes, hypotheses and confirmed facts.

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
