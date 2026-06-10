---
name: rust-fuzzing-and-property-testing
description: Design safe fuzzing and property testing for Rust parsers, normalizers, policy decisions, registry loading, and
  security boundaries using cargo-fuzz, proptest, or quickcheck.
---

# Rust Fuzzing and Property Testing

## Purpose

Find edge cases in Rust parsing and decision logic.

## Tools

- `cargo fuzz`;
- `proptest`;
- `quickcheck`;
- corpus minimization;
- crash reproduction.

## Good CYBOU targets

- command normalization;
- shell wrapper detection;
- policy rule parser;
- registry parser;
- YAML/JSON schema loader;
- redaction logic;
- URL/host normalization;
- scope matching.

## Safety

- fuzz in sandbox;
- no production data;
- no real secrets;
- no external network;
- cap CPU/time;
- store crash reproducers safely.

## Property examples

- normalization is deterministic;
- redaction never reveals matched secret;
- denied actions remain denied after whitespace/quote variations;
- registry validation is stable across file order.

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
