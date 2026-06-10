---
name: malicious-dependency-review
description: Review suspected malicious or risky dependencies. Use for typosquatting, dependency confusion, postinstall scripts, package takeover, suspicious maintainers, untrusted binaries, npm/pypi/rubygems/maven/cargo package risk, and dependency incident triage.
---

# Malicious Dependency Review

## Default mode

Read-only.

## Rule

Do not install a suspicious package to inspect it. Inspect metadata/source in an isolated environment only.

## Review signals

- package name similar to popular package;
- recently published package;
- maintainer changed;
- postinstall/preinstall scripts;
- obfuscated code;
- network calls during install;
- credential access;
- binary blob;
- package downloads external executable;
- no repository or suspicious repository;
- sudden new dependency in PR.

## Procedure

1. Identify package and version.
2. Check why it was added.
3. Inspect install scripts.
4. Inspect changed lockfile.
5. Check runtime import/use.
6. Identify network/file/credential behavior.
7. Recommend removal, pinning, or replacement.

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
