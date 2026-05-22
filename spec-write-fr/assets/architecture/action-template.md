---
id: FR-XXX
title: "[Action Name] Action"
artifact_type: FR
object: action
---
# [FR-XXX] [Action Name] Action

## Description
The system **SHALL** provide a `[ActionName]` action/command that [purpose].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Inputs
| Name | Type | Required | Description |
|------|------|----------|-------------|
| [param] | [type] | Y/N | [description] |

## Outputs
| Name | Type | Description |
|------|------|-------------|
| [field] | [type] | [description] |

## Error Handling
| Error | Response |
|-------|----------|
| [condition] | [behavior] |

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | [constraint] | Technical | [why] | [how verified] |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Given [input], action produces [output] | Unit Test |
| FR-XXX-AC-2 | Given [error condition], action returns [error] | Unit Test |

## Dependencies
- **Upstream**: [prerequisites]
- **Downstream**: [dependents]
