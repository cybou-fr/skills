---
name: forensic-artifact-inventory
description: Build forensic artifact inventory for logs, disk images, memory captures, cloud audit records, EDR events, screenshots,
  tickets and hashes.
---

# Forensic Artifact Inventory

Catalog forensic artifacts with source, hash, collection time, collector, custody and redaction metadata.

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
