---
id: FR-XXX
title: "[Extension Point Name]"
artifact_type: FR
object: extension_point
relationships:
  - target: "ix://org/repo/FR-YYY"
    type: "references"
---
# [FR-XXX] [Extension Point Name]

## Description
The system **SHALL** expose `[extension point]` so [who] can contribute
[what] without modifying [host]. Use this kind only when pluggability itself
needs to be a node (external authors, compatibility guarantees); an internal
contract with known implementations is just an `interface` plus `implements`
edges.

## Related User Stories
- [US-XXX]: [Story Title]

---

## Contract

[The interface the extension point exposes to plug-ins — name the
`interface` FR it publishes and what a conforming contribution provides.]

## Registration

> Optional — how implementations register and are discovered/selected.

- [registration call/convention, collision policy, fallback behavior]

## Stability

> Optional — compatibility window and deprecation guarantees offered to
> implementers.

- [semver policy, deprecation window]

---

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | A conforming contribution registers and is used without host changes | Test |

## Dependencies
- **Upstream**: [the published interface FR]
- **Downstream**: [contributing modules]
