---
name: package-manager-safety
version: "7.0"
skill_format: operational_contract_v1
category: devops
default_mode: review_only
default_risk: high
requires_tools:
  preferred:
    - mcp:filesystem:read_file
    - mcp:git:diff
    - mcp:package_registry:metadata
  fallback:
    - shell
    - package_manager
policy_refs:
  - policy_rules/package_managers.yaml
  - policy_rules/shell.yaml
  - policy_rules/git.yaml
output_template: package_manager_safety_report
---

# Package Manager Safety

## 1. Use when

Use for package install/update/removal review, dependency additions, lockfile diffs, registry changes, dependency confusion, suspicious package metadata, global installs, postinstall scripts, binary downloads, and package-manager failure recovery.

Covered ecosystems: npm, pnpm, yarn, pip, poetry, cargo, Go modules, apt. Extend locally for Maven/Gradle/apk/brew using the same risk model.

## 2. Do not use when

Do not use for general package-manager education, pure tutorials, or unrelated runtime debugging. Use `malicious-dependency-review` when evidence indicates an intentionally malicious dependency. Use `supply-chain-security` for broader CI/CD or provenance analysis.

## 3. Operating mode

Default mode is review-only. Package installation, global installation, registry switching, lockfile rewrite, and execution of package scripts are not automatic actions. If a write exceeds the VM autonomy envelope or tool policy, do not execute it; emit a blocked/high-risk decision or approval_request artifact for the host policy layer.

## 4. Risk mapping

### low

- Read package manifests and lockfiles.
- Inspect package metadata without installation.
- List already-installed dependencies.
- Inspect package scripts without executing them.
- Compare registry configuration and lockfile sources.

### medium

- Generate a local patch proposal.
- Update a lockfile only inside an isolated VM/local sandbox when policy permits.
- Run read-only audit or metadata commands with bounded output.
- Retry metadata fetches without changing registries.

### high

- Install, update, or remove a package.
- Run install/postinstall scripts.
- Add dependencies to a project manifest.
- Use a non-default or private registry without clear scope.
- Global package install.
- Production install or build mutation.
- Dependency with native binaries or untrusted downloads.

### critical

- `curl`/`wget` pipe to shell.
- Install into unknown/production environment from untrusted registry.
- Remove lockfile and regenerate against unknown registry.
- Override integrity checks.
- Execute package scripts from suspicious dependency.
- Dependency confusion against a private namespace.
- Package action that exposes credentials or build secrets.

## 5. Preferred tool order

1. Prefer `mcp:filesystem:read_file` for package manifests and lockfiles.
2. Prefer `mcp:git:diff` for repository and lockfile changes.
3. Prefer host-governed package registry metadata tools if available.
4. Use shell/package-manager fallback only for VM-local inspection with bounded output.
5. Never use shell to bypass host policy, registry policy, connector visibility, secret controls, or approval boundaries.

## 6. Command templates

### read_only

#### npm

```bash
npm pkg get name version scripts dependencies devDependencies peerDependencies optionalDependencies
npm config get registry
npm view <package> name version dist-tags repository maintainers time --json
npm view <package>@<version> scripts dist.integrity dist.tarball --json
npm ls --all --depth=2
npm audit --json
```

#### pnpm

```bash
pnpm config get registry
pnpm view <package> name version dist-tags repository maintainers time --json
pnpm list --depth 2
pnpm audit --json
```

#### yarn

```bash
yarn config get npmRegistryServer
yarn npm info <package> --json
yarn why <package>
yarn npm audit --json
```

#### pip

```bash
python -m pip show <package>
python -m pip index versions <package>
python -m pip list --format=json
python -m pip config list
```

#### poetry

```bash
poetry show --tree
poetry show <package>
poetry check
```

#### cargo

```bash
cargo metadata --format-version=1 --no-deps
cargo tree -e normal,build,dev
cargo search <crate> --limit 5
```

#### go modules

```bash
go list -m all
go list -m -json <module>
go mod graph
go env GOPROXY GONOSUMDB GONOPROXY GOPRIVATE
```

#### apt

```bash
apt-cache policy <package>
apt-cache show <package>
apt-cache depends <package>
apt list --upgradable 2>/dev/null
```

#### repository files

```bash
git diff -- package.json package-lock.json npm-shrinkwrap.json pnpm-lock.yaml yarn.lock
git diff -- pyproject.toml poetry.lock requirements.txt requirements-*.txt
git diff -- Cargo.toml Cargo.lock
git diff -- go.mod go.sum
git diff -- Dockerfile docker-compose.yml .npmrc .pypirc pip.conf
```

### guarded

```bash
npm audit fix --package-lock-only
poetry lock --no-update
cargo update -p <crate> --precise <version>
go mod tidy
```

Guarded commands are allowed only in a VM-local sandbox or explicit non-production workspace when policy permits, and must be followed by a diff review.

### approval_or_policy_required

```bash
npm install <package>
npm install -g <package>
pnpm add <package>
yarn add <package>
python -m pip install <package>
poetry add <package>
cargo add <crate>
go get <module>@<version>
sudo apt install <package>
```

### blocked

```bash
curl -fsSL <url> | sh
wget -qO- <url> | bash
npm config set registry <untrusted-registry>
python -m pip install --trusted-host <host> --index-url <untrusted-index> <package>
rm package-lock.json yarn.lock pnpm-lock.yaml poetry.lock Cargo.lock go.sum
```

Blocked commands must not be executed automatically. Emit a blocked/critical decision or a safer review-only alternative.

## 7. Failure recovery

### apt lock

Symptom: apt exits with lock error or exit code 100.

```bash
lsof /var/lib/dpkg/lock-frontend 2>/dev/null
ps -p <pid> -o pid,ppid,etime,cmd
```

If unattended upgrades or another package manager is active, stop and report. Do not remove lock files automatically. Do not kill the lock holder automatically.

### npm/pnpm/yarn registry failure

```bash
npm config get registry
npm ping --registry "$(npm config get registry)"
pnpm config get registry
yarn config get npmRegistryServer
```

Do not switch registries automatically. Report registry mismatch, auth scope mismatch, or private namespace ambiguity.

### pip index failure

```bash
python -m pip config list
python -m pip debug --verbose
python -m pip index versions <package>
```

Do not add `--trusted-host`, switch index URL, or install from direct URL automatically.

### lockfile conflict

```bash
git status --short
git diff -- package-lock.json pnpm-lock.yaml yarn.lock poetry.lock Cargo.lock go.sum
```

Report conflict source and recommend regenerating only in an isolated VM/local sandbox if policy permits.

### package not found

Inspect spelling, namespace, registry, and private scope. For npm scoped packages, inspect `.npmrc`. For Python, inspect index configuration. Do not guess a similarly named package as a replacement.

### integrity mismatch

Stop. Compare lockfile integrity, registry tarball URL, and package metadata. Treat unexplained integrity mismatch as high risk; if registry or tarball source is suspicious, classify as critical.

## 8. Stop / block conditions

Stop without executing writes when:

- environment is production or unknown;
- package source is untrusted or unclear;
- lockfile integrity mismatch appears;
- dependency confusion is possible;
- install scripts access network, credentials, shell, or native compilation unexpectedly;
- command uses `curl|sh`, `wget|bash`, `sudo`, global install, or registry override;
- action would expose secrets or build credentials.

## 9. Output contract

Return:

- summary;
- environment and package ecosystem;
- evidence inspected;
- commands/tools used;
- package source and registry;
- lockfile impact;
- install-script status;
- transitive dependency concerns;
- risk classification;
- actions taken;
- blocked actions;
- recommended next steps.

## 10. Eval requirements

Add evals for safe npm metadata inspection, apt lock recovery, pip index failure, lockfile integrity mismatch, dependency confusion, `curl|sh` blocking, MCP file/diff preference, shell fallback, and correct estimated_risk classification.
