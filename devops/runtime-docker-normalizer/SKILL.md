---
name: runtime-docker-normalizer
description: Implement and review Docker/Compose normalizer for container/image/network/volume operations, privileged flags,
  socket mounts, destructive actions and production hints.
---

# Runtime Docker Normalizer

Extracts Docker operation, subcommand, target, compose usage, privileged flags, volume/socket mounts and destructive actions.

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
