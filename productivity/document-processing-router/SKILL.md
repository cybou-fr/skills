---
name: document-processing-router
description: Route document and artifact tasks to the right workflow for DOCX, PDF, PPTX, XLSX, screenshots, extraction, editing,
  conversion, summarization, and validation.
---

# Document Processing Router

## Purpose

Classify document/artifact tasks and select the correct workflow.

## Procedure

1. Identify artifact type: DOCX, PDF, PPTX, XLSX, screenshot/image, mixed.
2. Identify operation: create, edit, extract, summarize, convert, validate, compare.
3. Check whether the task needs visual inspection, data extraction, or generated files.
4. Route to the appropriate skill.
5. Preserve original files unless user explicitly asks to modify.
6. Keep generated artifacts auditable and linked in final output.

## Routing

- DOCX -> `docx-document-workflow`
- PDF -> `pdf-document-workflow`
- PPTX -> `pptx-presentation-workflow`
- XLSX -> `xlsx-spreadsheet-workflow`
- screenshot/image -> `screenshot-analysis-workflow`

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
