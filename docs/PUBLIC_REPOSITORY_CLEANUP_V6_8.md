# v6.8 Public Repository Cleanup

v6.8 finalizes the pack as a skills-only corpus.

## Cleanup actions

```text
removed Rust contract sketch artifact
confirmed no cybou-core patch/scaffold directories
added CONTRIBUTING.md
added SECURITY.md
added SKILL_AUTHORING_GUIDE.md
added RELEASE.md
added repository boundary documentation
renamed runtime-* skill ids to cybou-core-* skill ids
added v6.8 public repository validator
```

## Naming cleanup

Skills previously named `runtime-*` were renamed to `cybou-core-*` to avoid implying that this pack contains runtime code.

The pack remains a corpus, not an execution layer.
