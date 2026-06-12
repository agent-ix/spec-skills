---
id: FR-XXX
title: "[Service Name] Domain Events"
artifact_type: FR
object: event
---
# [FR-XXX] [Service Name] Domain Events

## Description
The system **SHALL** emit domain events for [scope of events]. Events adhere to the CloudEvent envelope standard.

## Related User Stories
- [US-XXX]: [Story Title]

---

## Event Types
| Event Type | Trigger | Payload |
|------------|---------|---------|
| [entity].[action] | [what causes it] | [key payload fields] |

## Schema
```json
{
  "type": "object",
  "properties": {
    "event_type": {"type": "string"},
    "entity_id": {"type": "string", "format": "uuid"},
    "timestamp": {"type": "string", "format": "date-time"}
  },
  "required": ["event_type", "entity_id", "timestamp"]
}
```

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Events **SHALL** be emitted post-commit | Consistency | No premature events | Integration Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | When [trigger], [event_type] event is published with [payload fields] | Integration Test |

## Dependencies
- **Upstream**: [event bus, triggering FRs]
- **Downstream**: [consumers]
