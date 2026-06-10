---
name: ci-fix-proposal
description: Analyze CI failures and propose minimal safe fixes, with special focus on GitHub Actions, flaky tests, dependency failures, secrets, and deployment gates.
---

# CI Fix Proposal

## Procedure

1. Identify failing job.
2. Find first meaningful error.
3. Classify failure.
4. Check recent diff.
5. Propose minimal fix.
6. Suggest tests.
7. Do not push changes without approval.

## Output

- root cause;
- minimal patch plan;
- test plan;
- security concerns.

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
