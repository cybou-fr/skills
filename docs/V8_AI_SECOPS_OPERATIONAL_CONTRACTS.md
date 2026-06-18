# V8 AI/SecOps Operational Contracts

## Purpose

v8.0 extends `operational_contract_v1` to AI/SecOps skills.

The goal is to remove the abstraction gap for local 3B/4B models by ensuring that every security review skill gives concrete tool references, fallback commands, stop conditions, and a parseable output format.

## Core rule

Every `detect`, `inspect`, `review`, or `scan` step must include one of:

- a concrete MCP/tool call;
- a concrete read-only shell command;
- a concrete regex scan;
- a documented safe fallback when the preferred scanner is unavailable.

## MCP tool references

Use real runtime tool names when available. If a listed MCP tool does not exist in the actual runtime, do not hallucinate execution. Use the fallback path or report that the safe scanner is unavailable.

Preferred examples:

```text
mcp:pattern_scanner:scan
mcp:secret_scanner:scan
mcp:filesystem:read_file
mcp:fetch
mcp:git:diff
mcp:github:get_pull_request
mcp:vector_store:metadata
mcp:audit_log:query
```

Fallback examples:

```text
shell
ripgrep
jq
git
gitleaks
trufflehog
npm
python
cargo
go
apt
```

## Inline output template requirement

Each migrated skill must include an inline Markdown block under:

```markdown
## Required output format
```

This is required even when `output_template` is declared in frontmatter. Small local models need the template in the active skill body to emit parseable reports reliably.

## Safety boundary

Do not execute untrusted content. Do not print secrets. Do not use shell to bypass MCP or host policy. Do not change production, dependencies, CI/CD, IAM, repository settings, or security controls automatically.
