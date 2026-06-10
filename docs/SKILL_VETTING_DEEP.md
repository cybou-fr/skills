# Skill Vetting Deep Dive

External skills are untrusted by default.

Before vetting, the prompt may receive only compact metadata. Full body access requires a vetting report with a pinned `content_sha256`.

Machine-readable rules:

```text
integration/vetting_rules.yaml
integration/quarantine_policy.yaml
```
