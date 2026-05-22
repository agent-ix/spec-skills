---
id: FR-XXX
title: "[System Name] Integration"
artifact_type: FR
tags: [integration]
---
# [FR-XXX] [System Name] Integration

## Description
The system **SHALL** integrate with [external system] to [purpose].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Connection
| Field | Value |
|-------|-------|
| Protocol | HTTP / gRPC / SDK / WebSocket |
| Base URL | [configurable endpoint] |
| Auth | API Key / OAuth / mTLS / None |
| Timeout | [default timeout in seconds] |

## Operations
| Operation | Method | Description |
|-----------|--------|-------------|
| [operation_name] | [HTTP method or SDK call] | [what it does] |

## Error Handling
| Error | Retry | Fallback |
|-------|-------|----------|
| Connection timeout | Y (3 attempts, exponential backoff) | [fallback behavior] |
| Auth failure | N | Raise / log and skip |
| Rate limit (429) | Y (respect Retry-After) | Queue for later |

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Integration **SHALL** use circuit breaker pattern | Resilience | Prevent cascade failure | Integration Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Successful [operation] returns expected data | Integration Test |
| FR-XXX-AC-2 | Connection failure is handled gracefully | Unit Test |

## Dependencies
- **Upstream**: [configuration, auth]
- **Downstream**: [services that consume integration data]
