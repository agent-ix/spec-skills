---
id: FR-XXX
title: "[Migration Name] Migration"
artifact_type: FR
object: migration
---
# [FR-XXX] [Migration Name] Migration

## Description
The system **SHALL** provide a migration that [purpose, e.g., adds column X to table Y].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Forward Migration
1. [Step 1: e.g., ALTER TABLE ... ADD COLUMN ...]
2. [Step 2: e.g., CREATE INDEX ...]
3. [Step 3: e.g., UPDATE ... SET ... WHERE ...]

## Rollback
1. [Step 1: e.g., DROP INDEX ...]
2. [Step 2: e.g., ALTER TABLE ... DROP COLUMN ...]

## Data Transformations
- [Description of any data transformation required, e.g., backfill column X from table Y]
- [Estimated row count / performance impact]

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Migration **SHALL** be idempotent | Operational | Safe re-runs | Integration Test |
| FR-XXX-CON-2 | Rollback **SHALL** not lose data | Data | Reversibility | Integration Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Forward migration applies cleanly to current schema | Migration Test |
| FR-XXX-AC-2 | Rollback reverts schema to pre-migration state | Migration Test |
| FR-XXX-AC-3 | Data transformations complete without data loss | Integration Test |

## Dependencies
- **Upstream**: [data schema FR, entity FR]
- **Downstream**: [service deployment]
