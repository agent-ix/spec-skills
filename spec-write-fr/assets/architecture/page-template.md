---
id: FR-XXX
title: "[Page Name] Page"
artifact_type: FR
object: page
---
# [FR-XXX] [Page Name] Page

## Description
The system **SHALL** provide a `[PageName]` page that [purpose].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Route
| Field | Value |
|-------|-------|
| Path | /[route-path] |
| Auth Required | Y/N |
| Layout | [layout name or "default"] |

## Sections
| Section | Component | Description |
|---------|-----------|-------------|
| [section] | [ComponentName] | [what this section shows] |

## Navigation
- **Entry Points**: [how user reaches this page]
- **Exit Points**: [where user can navigate to from here]

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Page **SHALL** be responsive (mobile + desktop) | Accessibility | UX | Visual Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Page renders all sections with required data | Integration Test |
| FR-XXX-AC-2 | Page handles loading and error states | Unit Test |

## Dependencies
- **Upstream**: [data sources, API endpoints, auth]
- **Downstream**: [child components]
