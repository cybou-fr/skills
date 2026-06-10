---
name: rag-poisoning-defense
description: Assess and harden Retrieval-Augmented Generation systems against poisoned documents, malicious instructions in
  knowledge bases, untrusted source injection, stale or low-trust documents, and sensitive corpus exposure.
---

# RAG Poisoning Defense

## Purpose

Defensively review RAG pipelines for poisoning, untrusted document injection, sensitive data exposure, and retrieval trust failures.

## Review areas

- source ingestion;
- document provenance;
- trust labels;
- access control;
- chunking;
- metadata;
- retrieval filters;
- ranking;
- citation behavior;
- stale content;
- sensitive documents;
- instruction-like content inside documents.

## Safe assessment procedure

1. Map data sources.
2. Classify source trust.
3. Identify who can write to each source.
4. Review ingestion validation.
5. Check if retrieved content is treated as untrusted data.
6. Test with benign instruction-like markers.
7. Verify citations and provenance.
8. Check sensitive corpus access control.

## Controls

- trusted/untrusted source separation;
- signed or approved documents;
- source-level access control;
- ingestion scanning;
- instruction-like content detection;
- retrieval-time filtering;
- provenance in answers;
- RAG regression tests.

## Output

```md
## RAG poisoning defense review
Corpus:
Sources:
Trust boundaries:
Poisoning risks:
Sensitive data risks:
Evidence:
Recommended controls:
```

## Required output

End with:
- assessment scope;
- summary;
- evidence;
- risk level;
- actions taken;
- recommended controls;
- approval required, if any.

## Safety notes

This skill is for defensive AI security assessment and hardening.

Do not generate jailbreak prompts, bypass recipes, exploit payloads, data exfiltration instructions, stealth techniques, credential theft steps, or instructions for evading model safety systems.

When testing is needed, use benign placeholders, synthetic examples, allowlisted test cases, and approved evaluation harnesses.

If a policy rule conflicts with this skill, the policy rule wins.
