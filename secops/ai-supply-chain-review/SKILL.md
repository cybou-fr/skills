---
name: ai-supply-chain-review
description: Review AI-specific supply chain risks: model provenance, third-party models, datasets, embeddings, vector stores, prompt templates, eval datasets, plugins/tools, adapters, and model-serving dependencies.
---

# AI Supply Chain Review

## Purpose

Assess supply chain risks specific to AI systems.

## Review areas

- base model provider;
- model provenance;
- model card/license;
- fine-tuning datasets;
- embedding model;
- vector database;
- RAG documents;
- prompt templates;
- eval datasets;
- agent tools/plugins;
- model-serving container;
- dependencies;
- third-party APIs.

## Risks

- compromised model artifact;
- untrusted dataset;
- poisoned RAG corpus;
- malicious plugin/tool;
- prompt template tampering;
- vector store contamination;
- insecure model-serving image;
- dependency compromise;
- unclear license or data use terms.

## Controls

- provenance tracking;
- signed artifacts where possible;
- approved model registry;
- dataset documentation;
- prompt template versioning;
- tool approval workflow;
- dependency scanning;
- SBOM;
- access control on vector stores.

## Output

```md
## AI supply chain review
System:
Components:
Provenance gaps:
High-risk dependencies:
Dataset/RAG risks:
Recommended controls:
Approval required:
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
