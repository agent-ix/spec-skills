---
id: FR-XXX
title: "[Component Name] UI Component"
artifact_type: FR
object: ui_component
---
# [FR-XXX] [Component Name] UI Component

## Description
The system **SHALL** provide a `[ComponentName]` UI component that [purpose].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Props
| Name | Type | Required | Description |
|------|------|----------|-------------|
| [prop] | [TypeScript type] | Y/N | [description] |

## Test IDs
- `[component-name]-root`: Root container element
- `[component-name]-[element]`: [purpose]

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Component **SHALL** be accessible (WCAG 2.1 AA) | Accessibility | Compliance | Audit |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Component renders with required props | Unit Test |
| FR-XXX-AC-2 | Component handles [interaction] correctly | Unit Test |

## Dependencies
- **Upstream**: [design system, data source]
- **Downstream**: [parent components, pages]
