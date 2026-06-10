# Immunity Compatibility

v6.3 adds direct compatibility assets for `cybou-core/src/immunity.rs` and `risk.rs`.

## Goal

The external pack must be consumable as deterministic safety metadata without giving the LLM execution authority.

## New directory

```text
immunity_mapping/
```

## Files

```text
immunity_mapping/immunity_manifest.yaml
immunity_mapping/decision_mapping.yaml
immunity_mapping/risk_mapping.yaml
immunity_mapping/tool_class_mapping.yaml
immunity_mapping/command_pattern_mapping.yaml
immunity_mapping/sensitive_targets.yaml
```

## Runtime verdicts

All policy outcomes must compile into:

```text
Allow
Deny
NeedsApproval
```

## Matching policy

```text
Deny overrides NeedsApproval.
NeedsApproval overrides Allow.
Highest risk wins.
Approval cannot override Deny.
```

## Command patterns

`command_pattern_mapping.yaml` contains deterministic regex-style rules for high-risk command classes:

- remote pipe-to-shell;
- destructive filesystem operations;
- Terraform destroy / auto-approve;
- Kubernetes delete;
- privileged Docker;
- force push;
- destructive database statements;
- sensitive path access;
- nested interpreters;
- encoded payload execution.

## Sensitive targets

`sensitive_targets.yaml` contains sensitive paths and credential locations that should trigger `NeedsApproval` or `Deny`.

## Rust integration

Recommended target:

```text
cybou-core/src/immunity/policy_bundle.rs
```

Suggested contract sketch:

```text
docs/RUST_IMMUNITY_CONTRACT_SKETCH.rs
```

## Security rule

The mapping may inform `immunity.rs`, but it never bypasses it.
