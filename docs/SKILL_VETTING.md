# Skill Vetting

External skills are untrusted content.

Default prompt access:

```text
name
description
category
triggers
risk
```

Full body is loaded only after vetting.

Reject skills that attempt to:

- bypass immunity;
- disable audit;
- disable approval;
- print secrets;
- exfiltrate data;
- hide prompt injection;
- request direct tool execution.
