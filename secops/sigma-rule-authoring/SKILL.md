---
name: sigma-rule-authoring
description: Draft, validate and review Sigma detection rules from alert patterns, log examples and detection ideas without
  deploying them automatically.
---

# Sigma Rule Authoring

Draft Sigma rules with title, status, logsource, detection, false positives and level. Deployment requires approval.

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
