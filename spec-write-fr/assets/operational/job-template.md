---
id: FR-XXX
title: "[Job Name] Scheduled Job"
artifact_type: FR
object: job
---
# [FR-XXX] [Job Name] Scheduled Job

## Description
The system **SHALL** execute [job behavior] on [schedule].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Schedule
| Field | Value |
|-------|-------|
| Cron | [cron expression, e.g. `0 */6 * * *`] |
| Timezone | UTC |
| Concurrency | Allow / Skip if running / Queue |

## Execution
1. [Step 1: what the job does]
2. [Step 2: ...]

## Outputs
| Output | Destination | Description |
|--------|-------------|-------------|
| [result] | [database / queue / log] | [what gets produced] |

## Failure Behavior
| Failure | Retry | Alert |
|---------|-------|-------|
| [step fails] | Y (N attempts) / N | [notification channel] |

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Job **SHALL** be idempotent | Data Integrity | Safe re-execution | Unit Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Job executes successfully on schedule trigger | Integration Test |
| FR-XXX-AC-2 | Job handles partial failure gracefully | Unit Test |

## Dependencies
- **Upstream**: [data sources, configuration]
- **Downstream**: [consumers of job output]
