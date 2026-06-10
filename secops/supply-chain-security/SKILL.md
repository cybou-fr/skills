---
name: supply-chain-security
description: Review software supply chain risk in dependencies, lockfiles, CI/CD, artifacts, containers, SBOMs, provenance,
  package managers, unpinned actions, suspicious install scripts, and dependency confusion scenarios.
---

# Supply Chain Security

## Default mode

Read-only review.

## Review lockfiles

- package-lock.json;
- pnpm-lock.yaml;
- yarn.lock;
- poetry.lock;
- requirements.txt;
- go.sum;
- Cargo.lock;
- Gemfile.lock;
- pom.xml / gradle.lockfile.

## Review layers

1. Source code.
2. Dependencies.
3. Build system.
4. Artifacts.
5. Deployment.
6. Runtime.

## High-risk signals

- dependency confusion;
- typosquatting;
- maintainer takeover;
- postinstall script;
- unpinned Docker base image;
- unverified binary release;
- fork PR with secrets;
- CI config disables security checks.

## Rule

A new dependency in a PR must be treated as code, not just metadata.

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
