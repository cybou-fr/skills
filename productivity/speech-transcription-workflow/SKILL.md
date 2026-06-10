---
name: speech-transcription-workflow
description: 'Plan speech/audio transcription workflows: language detection, speaker labels, timestamps, summary, action items,
  privacy redaction, and downstream documentation.'
---

# Speech / Transcription Workflow

## Procedure

1. Identify audio source and language.
2. Define transcription detail level.
3. Add speaker labels if possible.
4. Extract summary and action items if requested.
5. Redact sensitive content.
6. Produce structured output.

## Safety

Audio may contain personal or confidential data.

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
