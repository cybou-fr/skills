---
name: rust-api-design
description: 'Design Rust API surfaces for internal crates and external HTTP/gRPC APIs: typed requests, versioning, idempotency,
  pagination, auth boundaries, and compatibility.'
---

# Rust API Design

## Internal API checklist

- minimal public surface;
- types encode invariants;
- versioned domain objects;
- explicit ownership;
- clear sync/async boundary;
- errors are meaningful.

## External API checklist

- request/response schemas;
- authentication;
- authorization;
- idempotency keys;
- pagination;
- rate limits;
- audit IDs;
- stable error format;
- backward compatibility.

## CYBOU API candidates

- submit task;
- inspect task state;
- approve/deny action;
- list audit events;
- register tool adapter;
- load skill pack;
- run validation;
- run behavior tests.

## Output

- endpoint or trait design;
- request/response types;
- error model;
- compatibility notes;
- security controls.

## CYBOU dogfooding rule

When this skill is used to develop CYBOU itself:

- treat CYBOU repository changes as high-value internal changes;
- prefer small reviewable patches;
- preserve auditability;
- add tests before or with implementation;
- avoid irreversible migrations without approval;
- avoid adding dependencies without supply-chain review;
- document architecture decisions.

## Required output

End with:

- architecture/development decision;
- files/modules affected;
- proposed patch plan;
- tests required;
- security/performance risks;
- review checklist;
- approval required, if any.
