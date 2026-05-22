---
id: FR-XXX
title: "[Middleware Name] Middleware"
artifact_type: FR
object: middleware
---
# [FR-XXX] [Middleware Name] Middleware

## Description
The system **SHALL** apply `[MiddlewareName]` middleware that [purpose] on [scope: all routes / specific routes].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Behavior
| Phase | Action |
|-------|--------|
| Request (before handler) | [what happens on incoming request] |
| Response (after handler) | [what happens on outgoing response] |
| Error | [what happens on exception] |

## Scope
| Applied To | Excluded |
|------------|----------|
| [route pattern or "all"] | [routes excluded, e.g. /health] |

## Configuration
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| [param] | [type] | [default] | [description] |

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Middleware **SHALL** not modify request body | Data Integrity | Transparency | Unit Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Middleware executes on matching routes | Integration Test |
| FR-XXX-AC-2 | Middleware is skipped for excluded routes | Integration Test |

## Dependencies
- **Upstream**: [configuration, auth provider]
- **Downstream**: [all route handlers in scope]
