---
name: soc-alert-triage
description: Triage SOC alerts from SIEM/EDR/cloud sources with severity, confidence, affected assets, evidence, containment recommendations and approval boundaries.
---

# SOC Alert Triage

Classify security alerts, gather evidence, extract entities, map likely tactic/technique and recommend safe next steps.

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
