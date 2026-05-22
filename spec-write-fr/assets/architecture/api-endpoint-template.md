---
id: FR-XXX
title: "[Endpoint Name] API Endpoint"
artifact_type: FR
object: api_endpoint
---
# [FR-XXX] [Endpoint Name] API Endpoint

## Description
The system **SHALL** expose an HTTP endpoint that [purpose].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Endpoint
| Method | Path | Description |
|--------|------|-------------|
| GET / POST | /api/v1/[resource] | [Description of the endpoint action] |

## Error Codes
| Code | Description |
|------|-------------|
| 400 | Invalid request body or parameters |
| 401 | Missing or invalid authentication |
| 403 | Insufficient permissions |
| 404 | Resource not found |
| 422 | Validation failure |

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | [constraint] | Technical | [why] | [how verified] |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | [endpoint] returns [expected response] for valid input | Integration Test |
| FR-XXX-AC-2 | [endpoint] returns [error code] for [invalid input] | Integration Test |

## Dependencies
- **Upstream**: [auth service, entity FRs]
- **Downstream**: [consumers, UI components]
