---
name: cicd-failure-analysis
description: Analyze failed CI/CD pipelines and propose safe fixes. Use for GitHub Actions, GitLab CI, Jenkins, Docker builds, Node/Python/Go/Java/Rust build failures, tests, lint, dependency failures, deployment jobs, flaky tests, and CI security concerns.
---

# CI/CD Failure Analysis

## Default mode

Read-only analysis and patch proposal only.

## Procedure

1. Identify failed job and first meaningful error.
2. Classify failure:
   - dependency;
   - lint;
   - test;
   - build;
   - Docker build;
   - deployment;
   - credentials;
   - registry/network;
   - flaky test;
   - infrastructure.
3. Extract evidence.
4. Check recent changes.
5. Propose minimal fix.
6. Flag security issues.

## Ecosystem hints

- Node: npm/pnpm/yarn lockfile and install errors.
- Python: pip/poetry dependency resolution and wheel build errors.
- Go: module download, `go.sum`, test race.
- Java: Maven/Gradle dependency and test lifecycle.
- Rust: Cargo.lock and feature flags.
- Docker: build context, missing files, registry auth.

## CI security checks

Look for:
- secrets printed in logs;
- unpinned GitHub Actions;
- fork PR with secrets;
- suspicious install scripts;
- `curl | sh`;
- artifacts from untrusted source.

If CI logs contain secrets, activate `secret-detection` and `redaction`.

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
