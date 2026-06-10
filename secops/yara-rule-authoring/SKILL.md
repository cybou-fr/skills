---
name: yara-rule-authoring
description: Draft and review defensive YARA rules from benign indicators, malware family notes or file metadata without creating weaponized artifacts.
---

# YARA Rule Authoring

Draft defensive YARA rules for detection. Do not generate malware or evasion logic.

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
