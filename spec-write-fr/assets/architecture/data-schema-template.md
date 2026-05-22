---
id: FR-XXX
title: "[Table Name] Data Schema"
artifact_type: FR
object: data_schema
---
# [FR-XXX] [Table Name] Data Schema

## Description
The system **SHALL** define a `[table_name]` database table/schema that [purpose].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Columns
| Name | Type | Nullable | Description |
|------|------|----------|-------------|
| id | UUID | N | Primary key |
| [column] | [SQL type] | Y/N | [description] |
| created_at | TIMESTAMPTZ | N | Creation timestamp |
| updated_at | TIMESTAMPTZ | N | Last modification timestamp |

## Indexes
- `idx_[table]_[column]`: B-tree index on `[column]` for [query pattern]
- `uq_[table]_[column]`: Unique constraint on `[column]`

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | [constraint] | Data | [why] | [how verified] |

---

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Table schema matches column definitions | Migration Test |
| FR-XXX-AC-2 | Indexes are present and functional | Integration Test |

## Dependencies
- **Upstream**: [entity FR defining the domain model]
- **Downstream**: [repository FRs, migration FRs]
