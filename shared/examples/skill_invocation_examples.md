# Skill Invocation Examples

## CrashLoopBackOff in production

Selected skills:
- task-classification
- environment-detection
- risk-and-approval
- kubernetes-readonly-triage
- devops-incident-triage

Mode: read-only  
Risk: high  
Approval required for: rollback, restart, apply, delete, scale.

## Token leaked in CI logs

Selected skills:
- cicd-failure-analysis
- secret-detection
- redaction
- evidence-handling
- secret-rotation-playbook
- secops-incident-response

Mode: read-only until rotation approval.  
Never print full token.

## Terraform opens SSH to the world

Selected skills:
- terraform-plan-review
- cloud-readonly-triage

Mode: read-only.  
Decision: flag public exposure and recommend safer CIDR.

## PR modifies Dockerfile and GitHub Actions

Selected skills:
- pull-request-review
- container-security-review
- supply-chain-security
- cicd-failure-analysis

Mode: read-only review comment.
