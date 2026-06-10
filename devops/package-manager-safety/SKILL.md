---
name: package-manager-safety
description: Safely review package manager operations before installing, updating, removing, or executing dependencies. Use
  for npm, pnpm, yarn, pip, poetry, cargo, go modules, maven, gradle, apt, apk, brew, and package install risks.
---

# Package Manager Safety

## Default mode

Draft/review only. Installation requires policy check and often approval.

## Risks

- malicious package;
- typosquatting;
- dependency confusion;
- postinstall scripts;
- lockfile poisoning;
- untrusted binary download;
- production mutation;
- build-time secret exposure.

## Safe review

Inspect:
- package name;
- version;
- registry;
- lockfile diff;
- install scripts;
- transitive dependencies;
- source/repository;
- reason for adding package.

## Commands requiring approval

- `npm install`;
- `pip install`;
- `poetry add`;
- `cargo add`;
- `apt install`;
- `apk add`;
- `brew install`;
- global installs;
- production installs.

## Escalate

Use `malicious-dependency-review` if suspicious.

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
