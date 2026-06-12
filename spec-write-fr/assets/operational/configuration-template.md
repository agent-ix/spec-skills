---
id: FR-XXX
title: "[Service Name] Configuration"
artifact_type: FR
object: configuration
---
# [FR-XXX] [Service Name] Configuration

## Description
The system **SHALL** support the following configuration for [scope].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Configuration

> One required table — headers exactly `Name | Scope | Type | Default |
> Description`. Scope carries the semantic as data (checked by the
> `configuration-scope` lint rule):
> - `creation` — fixed when the instance/object is created (reloptions,
>   deploy values, build flags); changing it means rebuild/redeploy.
> - `runtime` — tunable on a running system (GUCs, env-reloadable values,
>   admin toggles).
> - `session` — per-session/per-request overrides.

| Name | Scope | Type | Default | Description |
|------|-------|------|---------|-------------|
| [param_name] | creation | [type] | [default or "required"] | [description] |
| [knob_name] | runtime | [type] | [default] | [description] |

## Behavior

[Load/reload semantics, validation, precedence rules — e.g. config loads at
startup, re-reads on SIGHUP, failed reloads are rejected atomically.]

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Required parameters **SHALL** cause startup failure if missing | Operational | Fail-fast | Integration Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Service starts with all required parameters set | Test |
| FR-XXX-AC-2 | Service fails to start when required parameter is missing | Test |
| FR-XXX-AC-3 | Default values are applied when optional parameters are omitted | Test |

## Dependencies
- **Upstream**: [deployment infrastructure]
- **Downstream**: [all service FRs that consume config]
