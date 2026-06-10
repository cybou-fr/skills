---
name: git-repository-review
description: Review Git repositories safely using read-only operations. Use for operational repository hygiene, branch state,
  diffs, commit history, ignored files, suspicious changes, config review, and safe patch recommendations.
---

# Git Repository Review

## Default mode

Read-only.

## Safe commands

```bash
git status
git diff
git diff --stat
git diff --name-only
git log --oneline -n 20
git show --stat
git branch --show-current
git remote -v
git ls-files
```

## Review checklist

- current branch;
- uncommitted changes;
- changed files;
- sensitive files accidentally tracked;
- large binary files;
- suspicious scripts;
- CI/CD changes;
- dependency changes;
- Docker/Terraform/Kubernetes changes.

## Approval required

```bash
git commit
git push
git reset
git clean
git rebase
git merge
```

## Escalate to other skills

- dependency change -> `supply-chain-security`;
- Dockerfile -> `container-security-review`;
- Terraform -> `terraform-plan-review`;
- CI config -> `cicd-failure-analysis`;
- secrets -> `secret-detection`.

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
