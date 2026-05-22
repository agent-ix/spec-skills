---
id: FR-XXX
title: "[Model Name] DTO"
artifact_type: FR
object: dto
---
# [FR-XXX] [Model Name] DTO

## Description
The system **SHALL** define a `[ModelName]` data transfer object for [API endpoint or use case].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Schema
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| [field_name] | [type] | Y/N | [description] |

## Variants
| Variant | Purpose | Differences from Base |
|---------|---------|----------------------|
| [ModelName]Create | Request body for creation | Omits `id`, `created_at` |
| [ModelName]Read | Response body | Includes all fields |
| [ModelName]Update | Partial update request | All fields optional |

## Validation Rules
| Field | Rule | Error |
|-------|------|-------|
| [field_name] | [constraint, e.g. max_length=256] | 422 Validation Error |

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Schema **SHALL** be serializable to JSON | Technical | API compatibility | Unit Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Valid payload passes validation | Unit Test |
| FR-XXX-AC-2 | Invalid payload returns 422 with field errors | Unit Test |

## Dependencies
- **Upstream**: [entity FRs that define the domain model]
- **Downstream**: [API endpoint FRs that use this DTO]
