---
id: FR-XXX
title: "[Entity] Repository"
artifact_type: FR
object: repository
---
# [FR-XXX] [Entity] Repository

## Description
The system **SHALL** provide a repository for `[Entity]` that encapsulates data access operations.

## Related User Stories
- [US-XXX]: [Story Title]

---

## Target Entity
This repository serves the `[Entity]` entity defined in [FR-YYY](../functional/FR-YYY-entity-name.md).

## Operations
| Name | Inputs | Output | Description |
|------|--------|--------|-------------|
| create | [Entity]Create | [Entity] | Persist a new entity |
| get_by_id | UUID | [Entity] \| None | Retrieve by primary key |
| list | filters, offset, limit | list[[Entity]], total | Paginated filtered query |
| update | UUID, [Entity]Update | [Entity] | Partial update |
| delete | UUID | None | Remove entity |

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | [constraint] | Technical | [why] | [how verified] |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | [operation] returns expected result | Unit Test |

## Dependencies
- **Upstream**: [entity FR-YYY]
- **Downstream**: [service layer FRs]
