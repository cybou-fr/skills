# AGENTS.md — Cybou Skills Corpus v6.8.1

This file describes repository-wide expectations for the Cybou skills corpus.

This repository is not the Cybou runtime.

## Boundary

The corpus may provide:

```text
skills
policies
evals
schemas
tool metadata
scope metadata
trust/signing/provenance manifests
documentation
validators
```

The corpus must not provide:

```text
cybou-core Rust implementation
guest runtime code
MicroVM implementation code
CLI implementation patches
event/audit/immunity patches
```

## Safety formula

```text
Skills improve reasoning.
Rust decides safety.
MicroVM contains execution.
Audit records everything.
```

Only compact metadata should be exposed by default. Full skill body access requires vetting.
