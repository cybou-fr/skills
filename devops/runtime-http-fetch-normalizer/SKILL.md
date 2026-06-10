---
name: runtime-http-fetch-normalizer
description: Implement and review HTTP fetch normalizer for curl/wget/URLs, method detection, headers/body sensitivity, file
  downloads, pipe-to-shell handoff and host allowlist context.
---

# Runtime HTTP Fetch Normalizer

Extracts method, URL, host, headers/body flags, output file, follow redirects and pipe-to-shell risks.

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
