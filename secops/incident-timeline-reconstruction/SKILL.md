---
name: incident-timeline-reconstruction
description: Reconstruct incident timelines from alerts, logs, CloudTrail, EDR, identity events, tickets and analyst notes
  with confidence levels.
---

# Incident Timeline Reconstruction

Create chronological timeline with source attribution, confidence and gaps.

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
