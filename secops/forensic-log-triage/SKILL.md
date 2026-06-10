---
name: forensic-log-triage
description: 'Triage forensic logs safely: normalize events, extract indicators, map sources, preserve raw references and
  avoid exposing secrets.'
---

# Forensic Log Triage

Analyze logs for incident investigation while preserving references and redacting sensitive material.

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
