---
name: post-incident-case-summary
description: Draft post-incident case summary with impact, timeline, root cause hypotheses, evidence, remediation, lessons
  learned and follow-ups.
---

# Post-Incident Case Summary

Create case summary with evidence references and confidence markers.

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
