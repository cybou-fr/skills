---
name: detection-regression-suite
description: Create and maintain regression tests for IOC extraction, Sigma/YARA generation, alert triage, cloud event triage
  and timeline reconstruction.
---

# Detection Regression Suite

Regression tests for SOC and detection engineering behavior.

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
