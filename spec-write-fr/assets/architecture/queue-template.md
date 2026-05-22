---
id: FR-XXX
title: "[Queue/Topic Name] Message Queue"
artifact_type: FR
object: queue
---
# [FR-XXX] [Queue/Topic Name] Message Queue

## Description
The system **SHALL** define a message queue/topic `[queue.name]` for [purpose].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Payload
```json
{
  "type": "object",
  "properties": {
    "entity_id": {"type": "string", "format": "uuid"},
    "action": {"type": "string"},
    "timestamp": {"type": "string", "format": "date-time"}
  },
  "required": ["entity_id", "action", "timestamp"]
}
```

## Producers
- [Service A]: Publishes when [trigger]
- [Service B]: Publishes when [trigger]

## Consumers
- [Service C]: Processes [action] by [behavior]
- [Service D]: Updates [state] based on [payload]

## Delivery Guarantee
At-least-once delivery. Consumers **SHALL** be idempotent.

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | [constraint] | Technical | [why] | [how verified] |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Producer publishes valid payload to [queue] on [trigger] | Integration Test |
| FR-XXX-AC-2 | Consumer processes messages idempotently | Integration Test |

## Dependencies
- **Upstream**: [event bus infrastructure]
- **Downstream**: [consumer services]
