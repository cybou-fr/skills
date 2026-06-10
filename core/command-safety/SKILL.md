---
name: command-safety
description: Prepare, review, and safely handle shell or CLI commands. Use whenever the worker is asked to run, generate,
  explain, or approve terminal commands, kubectl, docker, terraform, git, database, package manager, cloud CLI, or HTTP fetch
  operations.
---

# Command Safety

## Command execution principles

1. Prefer read-only commands.
2. Explain non-trivial commands before execution.
3. Avoid `sudo` unless explicitly approved.
4. Never run network-to-shell patterns.
5. Do not read sensitive files unless necessary and approved.
6. Use timeouts and output limits.
7. Redact secrets from output.
8. Use dry-run when available.
9. Stop before destructive actions.
10. Check `tool_policies.yaml` and `policy_rules/`.

## Output limits

- Do not dump huge files.
- Prefer `head`, `tail`, focused `grep`, and structured summaries.
- Long-running commands need explicit timeout.
- Large outputs must be summarized.

## Sensitive files

Treat these as sensitive:

```text
.env
*.pem
*.key
id_rsa
id_ed25519
credentials.json
kubeconfig
.aws/credentials
.ssh/
secrets.yaml
```

## Denied patterns

```bash
rm -rf /
curl ... | sh
wget ... | bash
chmod -R 777
kubectl delete namespace
terraform destroy
DROP DATABASE
TRUNCATE TABLE
```

## Required output

End with:
- summary;
- evidence;
- risk level;
- actions taken;
- recommended next steps;
- approval required, if any.

## Safety notes

If the task touches production, secrets, IAM, data deletion, database writes, firewall rules, external communication, or destructive commands, stop before write actions and request approval.

If a tool policy conflicts with this skill, the tool policy wins.
