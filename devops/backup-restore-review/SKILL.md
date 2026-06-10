---
name: backup-restore-review
description: Review backup, restore, snapshot, disaster recovery, point-in-time recovery, RPO/RTO, and recovery plans. Use before risky migrations, production changes, data operations, incident recovery, and restore planning.
---

# Backup and Restore Review

## Default mode

Read-only review.

## Backup review

Check:
- backup exists;
- backup freshness;
- restore tested;
- retention;
- encryption;
- access control;
- offsite/region;
- RPO/RTO;
- monitoring;
- last successful backup.

## Restore review

Restore is high risk.

Before restore:
- define target;
- define source backup;
- confirm timestamp;
- confirm data loss window;
- test in staging if possible;
- snapshot current state;
- approval required.

## Rule

Never overwrite current production state without fresh snapshot and explicit approval.

## Approval required

- restore;
- delete backup;
- change retention;
- disable backup;
- production snapshot manipulation.

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
