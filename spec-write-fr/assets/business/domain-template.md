---
id: FR-XXX
title: "[Domain Name] Bounded Context"
artifact_type: FR
object: domain
---
# [FR-XXX] [Domain Name] Bounded Context

## Description
This FR defines the `[Domain Name]` bounded context, establishing its scope, ubiquitous language, and the domain objects it contains.

## Related User Stories
- [US-XXX]: [Story Title]

---

## Bounded Context
| Field | Type | Description |
|-------|------|-------------|
| Name | string | [domain name] |
| Scope | string | [what this domain owns] |
| Owner | string | [service or team] |

## Ubiquitous Language
| Term | Definition |
|------|------------|
| [term] | [precise definition within this domain] |

## Contained Objects
- [FR-A](../functional/FR-A.md): Entity — [name]
- [FR-B](../functional/FR-B.md): Value Object — [name]
- [FR-C](../functional/FR-C.md): Event — [name]
- [FR-D](../functional/FR-D.md): Process — [name]

---

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | All contained objects reference this domain | Inspection |

## Dependencies
- **Upstream**: [StR-XXX]
- **Downstream**: [all contained object FRs]
