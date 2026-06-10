---
name: sentry-issue-triage
description: Triage Sentry-style errors: group stack traces, identify release/environment, correlate with deploys, estimate impact, and propose safe remediation.
---

# Sentry Issue Triage

## Procedure

1. Identify issue, environment, release, frequency.
2. Review stack trace and breadcrumbs.
3. Check affected users and first/last seen.
4. Correlate with deploys.
5. Propose fix or rollback plan.
6. Redact PII.

## Safety

Error logs may contain sensitive data.

## Required output

End with:
- scope;
- summary;
- artifacts produced or changed;
- checks performed;
- risks or approvals;
- next steps.

## Runtime notes

Follow CYBOU policy, tool adapters, scope objects, approval state, redaction, and audit requirements.

If the task touches production, external publishing, repository writes, credentials, customer data, or third-party services, check policy and request approval before any side effect.
