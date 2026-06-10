---
name: runtime-database-normalizer
description: Implement and review database/SQL normalizer for SELECT versus INSERT/UPDATE/DELETE/DROP/TRUNCATE/ALTER, migration commands, target database and sensitive data hints.
---

# Runtime Database Normalizer

Classifies SQL statements and DB CLI commands. `SELECT` may still require redaction; `DROP`, `TRUNCATE`, `ALTER`, `DELETE`, migrations and writes are high-risk.

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
