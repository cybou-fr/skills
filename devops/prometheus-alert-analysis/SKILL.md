---
name: prometheus-alert-analysis
description: Analyze Prometheus or Alertmanager alerts and produce safe triage summaries. Use for alert labels, firing alerts,
  SLO burn rate, latency, error rate, saturation, Kubernetes alerts, and incident routing.
---

# Prometheus Alert Analysis

## Default mode

Read-only.

## Inputs

- alert name;
- labels;
- annotations;
- firing time;
- related metrics;
- dashboard links;
- service owner.

## Procedure

1. Identify alert type:
   - latency;
   - error rate;
   - saturation;
   - availability;
   - resource;
   - Kubernetes;
   - security-like anomaly.
2. Determine impact.
3. Check duration and trend.
4. Correlate with deployments/incidents.
5. Recommend next diagnostic skill.

## Do not

- silence alerts without approval;
- change alert rules without approval;
- restart services without approval.

## Output

```md
## Alert analysis
Alert:
Severity:
Service:
Likely impact:
Evidence:
Suggested diagnostics:
Approval required:
```

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
