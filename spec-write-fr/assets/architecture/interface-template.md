---
id: FR-XXX
title: "[Contract Name] Interface"
artifact_type: FR
object: interface
relationships:
  - target: "ix://org/repo/FR-YYY"
    type: "specifies"
---
# [FR-XXX] [Contract Name] Interface

## Description
The system **SHALL** define the `[ContractName]` operations contract that all
[implementations — codecs/drivers/plugins/renderers] satisfy.

## Related User Stories
- [US-XXX]: [Story Title]

---

## Contract

> Required: a fenced ```yaml block with the LANGUAGE-NEUTRAL operations
> contract — design-level YAML, never source code. Implementations are NOT
> enumerated here: each implementation is its own FR linked via an
> `implements` relationship edge. Heavy selection/dispatch machinery belongs
> in a `process` object. Boundary: `interface` covers contracts WITHIN the
> system; a contract with an external system is an `external_contract`.

```yaml
name: [ContractName]
associated_types: [[AssociatedType]]
operations:
  - name: [operation_name]
    inputs: [[input descriptions]]
    output: [output description]
    semantics: [what callers may rely on]
invariants:
  - [property every implementation must preserve]
dispatch: [how an implementation is selected, if trivial]
```

---

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Every implementation FR links here via `implements` | Inspection |
| FR-XXX-AC-2 | [conformance property, e.g. cross-implementation agreement] | Test |

## Dependencies
- **Upstream**: [behavioral FR this contract specifies]
- **Downstream**: [implementation FRs]
