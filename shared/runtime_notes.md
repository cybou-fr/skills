# Runtime Notes

## Important

The skill pack is not a security boundary.

CYBOU or another worker runtime should enforce:
- tool policy;
- environment policy;
- risk matrix;
- approval state;
- audit logging;
- output redaction.

## Recommended implementation

1. Parse user task.
2. Select candidate skills.
3. Load selected `SKILL.md`.
4. Detect environment.
5. Calculate risk.
6. Intercept tool calls.
7. Match tool call against `policy_rules/`.
8. Execute only if allowed.
9. Redact output.
10. Produce report.
11. Store audit trace.
