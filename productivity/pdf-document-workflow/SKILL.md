---
name: pdf-document-workflow
description: Analyze and process PDFs safely, including extraction planning, visual-page inspection guidance, form/table extraction, summarization, redaction planning, and conversion workflow selection.
---

# PDF Document Workflow

## Use for

- PDF summaries;
- form extraction;
- table extraction;
- visual layout review;
- redaction planning;
- conversion planning.

## Procedure

1. Determine whether text extraction is enough or visual inspection is needed.
2. Identify pages containing tables, forms, diagrams, or signatures.
3. Preserve citations/page references.
4. Do not rely on OCR unless necessary.
5. Redact sensitive information before sharing.
6. Explain extraction uncertainty.

## Safety

- Do not expose signatures, IDs, private data, or confidential metadata.
- Use redaction for sensitive PDFs.

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
