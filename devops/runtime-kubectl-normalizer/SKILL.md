---
name: runtime-kubectl-normalizer
description: Implement and review kubectl normalizer for verbs, resources, namespace, context, kubeconfig, production hints,
  exec/port-forward/apply/delete risks and dry-run flags.
---

# Runtime Kubectl Normalizer

Extracts verb, resource, name, namespace, context, kubeconfig, dry-run mode and high-risk verbs.

## Runtime enforcement rule

This skill belongs to the tool-specific normalizer layer.

The normalizer must produce a deterministic `NormalizedAction` before policy evaluation. It must preserve raw input, extract tool/operation/target/environment, detect side effects, detect sensitive data hints, and avoid executing anything.

## Required output

End with:

- tool normalizer;
- parsed operation;
- target/environment extraction;
- side effects;
- sensitive data flag;
- tests required;
- known parser limitations.
