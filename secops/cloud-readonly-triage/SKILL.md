---
name: cloud-readonly-triage
description: Perform read-only cloud security triage for AWS, GCP, or Azure. Use for suspicious cloud activity, public exposure, security group/firewall review, storage exposure, IAM changes, audit log checks, cloud incident evidence, and cloud configuration review.
---

# Cloud Read-only Triage

## Default mode

Read-only.

## AWS read-only examples

```bash
aws sts get-caller-identity
aws cloudtrail lookup-events --max-results 10
aws iam get-account-summary
```

## GCP read-only examples

```bash
gcloud auth list
gcloud config list
gcloud logging read 'protoPayload.methodName:*' --limit=10
```

## Azure read-only examples

```bash
az account show
az monitor activity-log list --max-events 10
```

## Caution

Cloud CLI output may include sensitive resource names or metadata. Redact if necessary.

## Approval required

- disabling keys;
- changing IAM;
- changing firewall;
- making bucket private;
- deleting resources;
- rotating secrets.

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
