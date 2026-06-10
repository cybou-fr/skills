---
name: notebook-analysis-workflow
description: Analyze Jupyter-style notebooks for reproducibility, data flow, execution order, outputs, dependencies, security
  risks, and report quality.
---

# Notebook Analysis Workflow

## Procedure

1. Identify notebook purpose.
2. Check execution order and hidden state.
3. Review dependencies.
4. Inspect data inputs/outputs.
5. Check for secrets/PII.
6. Validate charts/results.
7. Recommend reproducibility improvements.

## Safety

Notebooks may execute arbitrary code. Do not run unknown notebooks without review.

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
