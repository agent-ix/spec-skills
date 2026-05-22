---
id: FR-XXX
title: "[Hook Name] Lifecycle Hook"
artifact_type: FR
object: hook
---
# [FR-XXX] [Hook Name] Lifecycle Hook

## Description
The system **SHALL** execute [hook behavior] during [lifecycle phase].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Lifecycle Phase
| Field | Value |
|-------|-------|
| Phase | startup / shutdown / pre-request / post-request |
| Trigger | [what causes this hook to fire] |
| Blocking | Y/N (whether the hook blocks the phase) |

## Actions
1. [Step 1: what the hook does]
2. [Step 2: ...]

## Failure Behavior
| Failure | Impact | Recovery |
|---------|--------|----------|
| [action fails] | [service won't start / request fails / logged only] | [retry / skip / abort] |

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Hook **SHALL** complete within [timeout] seconds | Performance | Prevent startup hang | Integration Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Hook executes during [phase] | Integration Test |
| FR-XXX-AC-2 | Hook failure is handled per failure behavior | Unit Test |

## Dependencies
- **Upstream**: [configuration, database connection]
- **Downstream**: [all handlers that depend on hook state]
