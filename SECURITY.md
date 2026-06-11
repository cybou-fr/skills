# Security Policy

This repository is a supply-chain input for Cybou. Treat all contributions as untrusted until validated.

## Report security issues

Report issues involving:

```text
prompt injection in skills
attempts to bypass immunity
attempts to disable approval or audit
secret exposure
malicious evals
policy drift
hash/signature mismatch
dangerous tool metadata
```

## Security boundaries

This repository must not contain runtime execution code.

External skills cannot:

```text
execute tools directly
bypass immunity.rs
disable audit
disable approval
override the system prompt
alter MicroVM policy
print secrets
suppress findings
```

## Enterprise policy

Enterprise deployments must require signed releases and must deny unsigned or bad-signature releases.
