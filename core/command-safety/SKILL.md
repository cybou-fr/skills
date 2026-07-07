---
name: command-safety
description: Prepare, review, and safely handle shell or CLI commands. Use whenever the worker is asked to run, generate,
  explain, or approve terminal commands, kubectl, docker, terraform, git, database, package manager, cloud CLI, or HTTP fetch
  operations.
description_fr: Préparer, examiner et exécuter des commandes shell ou CLI en toute sécurité. À utiliser pour les commandes terminal, kubectl, docker, terraform, git, gestionnaires de paquets, CLI cloud ou requêtes HTTP.
category: core
default_risk: medium
default_mode: read_only
skill_format: operational_contract_v1
version: "10.1"
requires_tools:
  preferred:
    - mcp:filesystem:read_file
    - shell
  fallback:
    - shell
triggers:
  - command safety
  - shell command review
  - run bash safely
  - kubectl review
  - docker command
  - terraform command
  - database command safety
  - revue commande shell
  - exécuter bash en sécurité
  - commande kubectl
---

# Command Safety

## 1. Use when

Use this skill whenever the worker is about to execute, generate, or approve any shell command, CLI call, kubectl, docker, terraform, git, package manager, database CLI, cloud CLI, or HTTP fetch operation.

## 2. Operating mode

Default mode: read_only. Write commands require explicit approval or low-risk environment confirmation.

## 3. Risk mapping

### low
- read-only inspection: `ls`, `cat`, `grep`, `stat`, `kubectl get`, `docker ps`, `git status`, `SELECT`;
- dry-run modes: `terraform plan`, `apt-get install --dry-run`, `rsync -n`.

### medium
- local/sandbox changes: write config files, install packages in VM, restart local services;
- reversible actions with known rollback.

### high
- production changes, service restarts, IAM modifications, firewall rule changes, secret rotation;
- package upgrades on live services.

### critical
- destructive or irreversible: `rm -rf`, `DROP DATABASE`, `TRUNCATE`, `terraform destroy`, `kubectl delete namespace`, `chmod 777 -R`, network-to-shell pipes.

## 4. Command execution principles

1. Prefer non-interactive and idempotent commands (pass `-y` to `apt`, `--yes` to pip, etc.).
2. Explain non-trivial commands before execution.
3. Never pipe the output of a remote fetch (curl, wget) directly into a shell interpreter.
4. Use `--dry-run` or `plan` modes when available.
5. Timeout long-running commands (`timeout 30 <cmd>`).
6. Redact secrets from all output before logging or displaying.
7. Back up files before overwriting.
8. Stop and request approval before high/critical commands.

## 5. Output limits

- Do not dump huge files raw; use `head -n 100`, `tail -n 50`, `grep -n`, or structured summaries.
- If output exceeds ~200 lines, summarize and highlight key findings.
- Never log secrets, API keys, or tokens.

## 6. Sensitive files — treat as restricted

```text
.env  *.pem  *.key  id_rsa  id_ed25519
credentials.json  kubeconfig  .aws/credentials
.ssh/  secrets.yaml  .netrc  *.pfx  *.p12
```

Do not read these unless the task explicitly requires it and the risk level is approved.

## 7. Denied patterns

The following patterns must never be executed without prior explicit operator approval:

- Filesystem destruction: `rm -rf` on root or system paths
- Network-to-shell execution: piping curl or wget output directly into sh or bash
- World-writable permissions: `chmod -R 777`
- Cluster-scope destruction: `kubectl delete namespace`
- Infrastructure wipe: `terraform destroy`
- Data destruction: `DROP DATABASE`, `TRUNCATE TABLE`
- Credential file read: reading `/etc/shadow` without explicit need

## 8. Stop / block conditions

- Stop immediately if the requested command matches a denied pattern.
- Stop if the environment is unknown and the command is write/destructive.
- Stop if the command requires root and `sudo` was not explicitly approved.

## 9. Verify-before-finish

For any write command that ran, verify:
```bash
# For file writes:
stat -c '%a %U %G %n' <target>
# For service changes:
systemctl status <unit> --no-pager
# For package installs:
dpkg -l | grep <package>
```

## 10. Required output format

```markdown
## Command safety report

### Command reviewed

### Risk classification

### Pre-execution checks

### Execution result (summarized)

### Sensitive output redacted

### Blocked patterns

### Recommended next steps
```
