---
name: rust-release-and-semver
description: 'Plan Rust releases: semver, changelog, cargo package/publish gates, MSRV impact, migration notes, compatibility,
  and release approval.'
---

# Rust Release and Semver

## Purpose

Release Rust crates and CYBOU components safely.

## Tools

- `cargo package`;
- `cargo publish`;
- `cargo semver-checks`;
- changelog;
- release notes;
- MSRV checks.

## Procedure

1. Determine version bump.
2. Check public API changes.
3. Run release quality gates.
4. Check MSRV impact.
5. Update changelog.
6. Generate migration notes.
7. Require approval before publish.
8. Verify package contents.

## CYBOU rule

Publishing crates or release artifacts requires explicit approval.

## CYBOU dogfooding rule

When this skill is used for CYBOU itself:

- keep changes small and reviewable;
- add or update tests with implementation;
- prefer dry-run/read-only commands first;
- do not add dependencies without supply-chain review;
- do not publish, release, deploy, or modify production without explicit approval;
- document quality gates in CI.

## Required output

End with:

- toolchain decision;
- config/files affected;
- commands to run;
- CI quality gates;
- risks;
- approval required, if any.
