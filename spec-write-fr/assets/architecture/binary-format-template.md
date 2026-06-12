---
id: FR-XXX
title: "[Format Name] Binary Layout"
artifact_type: FR
object: binary_format
relationships:
  - target: "ix://org/repo/FR-YYY"
    type: "specifies"
---
# [FR-XXX] [Format Name] Binary Layout

## Description
The system **SHALL** persist [what] in the binary layout below. [Versioning /
compatibility rules.]

## Related User Stories
- [US-XXX]: [Story Title]

---

## Layout

> Required: a fenced ```yaml block describing the persisted binary layout —
> one or more record types, each with per-field name/offset/size/type (and
> endianness where it matters). This kind exists because JSON Schema has no
> offsets/strides/endianness vocabulary; use `data_schema` for genuinely
> JSON-shaped data.

```yaml
format: [format-name]
endianness: little
record_types:
  - name: [record_type]
    magic: [0x...]        # when applicable
    size: [bytes]         # fixed-size records
    fields:
      - { name: [field], offset: 0, size: 4, type: u32 }
      - { name: [field], offset: 4, size: 2, type: u16 }
  - name: [variable_record]
    tag: [0x..]
    fields:
      - { name: tag,     offset: 0, size: 1, type: u8 }
      - { name: payload, offset: 1, size: [expr], type: bytes }
```

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | [e.g. magic/version checked before any decode] | Data | [why] | Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | A record round-trips encode→decode byte-identically | Test |
| FR-XXX-AC-2 | Layout is independently decodable from this spec alone | Inspection |

## Dependencies
- **Upstream**: [behavioral FR that reads/writes this format]
- **Downstream**: [migration/compat FRs]
