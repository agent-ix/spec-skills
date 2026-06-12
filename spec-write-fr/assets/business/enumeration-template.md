---
id: FR-XXX
title: "[Vocabulary Name] Enumeration"
artifact_type: FR
object: enumeration
relationships:
  - target: "ix://org/repo/FR-YYY"
    type: "specifies"
---
# [FR-XXX] [Vocabulary Name] Enumeration

## Description
The system **SHALL** use the controlled `[vocabulary_name]` label set below.
[Where the labels appear — persisted columns, metrics labels, manifests — and
the change policy.] Use this kind for system-wide label sets other artifacts
reference by exact string; a DDD value object with behavior belongs in
`value_object` instead.

## Related User Stories
- [US-XXX]: [Story Title]

---

## Values

| Value | Description |
|-------|-------------|
| [label] | [meaning; terminal/initial state notes if a lifecycle] |
| [label] | [meaning] |

---

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Code matches the table exactly (no unlisted labels emitted) | Test |

## Dependencies
- **Upstream**: [FRs whose behavior produces these labels]
- **Downstream**: [FRs/dashboards that consume them]
