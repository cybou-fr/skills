---
name: runtime-terraform-normalizer
description: Implement and review Terraform/OpenTofu normalizer for plan/apply/destroy/state/import/workspace operations,
  chdir, var-files, auto-approve, state risks and workspace target.
---

# Runtime Terraform Normalizer

Extracts operation, chdir, workspace, var-files, auto-approve, state manipulation and destructive/apply risks.

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
