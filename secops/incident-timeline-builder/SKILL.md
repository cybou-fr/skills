---
name: incident-timeline-builder
description: Build incident timelines from logs, SIEM events, EDR findings, cloud audit events, Sentry issues and operator
  notes.
---

# Incident Timeline Builder

Normalize timestamped events into a chronological incident timeline with source, actor, asset, action and evidence references.

## Runtime enforcement rule

This skill belongs to the SOC and detection engineering layer.

SOC actions are read-only by default. Drafting detection logic is allowed; deploying, suppressing, disabling, blocking, quarantining or closing alerts requires explicit approval and audit. Evidence and alert data must pass through redaction before reports, exports or model-visible context.

## Required output

End with:

- alert/source context;
- extracted entities/IOCs;
- detection logic;
- severity/confidence;
- evidence references;
- recommended response;
- approval required, if any.
