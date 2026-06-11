# Repository Boundaries

This repository is a skills corpus.

It may contain:

```text
SKILL.md files
registry.yaml
output templates
policy metadata
activity policies
tool adapter metadata
scope objects
schemas
evals
trust/signing/provenance manifests
documentation for the corpus format
validators for the corpus format
```

It must not contain:

```text
cybou-core Rust implementation
guest runtime code
MicroVM implementation code
CLI implementation patches
event.rs patches
audit.rs patches
immunity.rs patches
Cargo workspace patches
```

Integration expectations may be documented, but runtime implementation belongs in the Cybou runtime repository.
