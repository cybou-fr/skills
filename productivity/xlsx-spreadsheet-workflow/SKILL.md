---
name: xlsx-spreadsheet-workflow
description: Design, analyze, and validate spreadsheets with tables, formulas, data quality checks, summaries, charts planning, and safe handling of sensitive rows.
---

# XLSX Spreadsheet Workflow

## Use for

- spreadsheet creation;
- formula review;
- data cleaning;
- reporting tables;
- charts;
- validation checks.

## Procedure

1. Identify data schema.
2. Preserve raw data separately from calculations.
3. Use clear sheet names.
4. Validate formulas.
5. Check missing values and duplicates.
6. Avoid exposing sensitive rows.
7. Create summaries and charts only when useful.

## Safety

- Redact PII/customer data.
- Do not silently alter source data.

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
