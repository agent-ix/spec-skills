---
id: FR-XXX
title: "[External System] Contract"
artifact_type: FR
object: external_contract
relationships:
  - target: "ix://org/repo/FR-YYY"
    type: "consumes"
---
# [FR-XXX] [External System] Contract

## Description
The system consumes `[external system]` as [role]. This FR records the
contract both sides rely on. Boundary: contracts WITHIN the system are
`interface` objects; this kind is for systems outside it (vendors, peer
services whose contract this repo does not own).

## Related User Stories
- [US-XXX]: [Story Title]

---

## Contract

[What the external system guarantees (invariants, versioning expectations,
isolation boundaries) and what this system guarantees back (usage limits,
caching rules, retry discipline).]

## Endpoints

> Optional — the concrete surface consumed/exposed.

- `[METHOD /path]` — [purpose]

## Behavior

> Optional — interaction semantics and failure modes.

- [e.g. fail-closed on non-200; timeout surfaces as 503, never auth success]

---

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | [contract property verified against the real/stubbed system] | Test |

## Dependencies
- **Upstream**: [the external system / its published API version]
- **Downstream**: [FRs consuming this contract]
