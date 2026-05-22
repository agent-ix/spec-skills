---
id: FR-XXX
title: "[Service Name] Configuration"
artifact_type: FR
object: configuration
---
# [FR-XXX] [Service Name] Configuration

## Description
The system **SHALL** support the following configuration parameters for [scope].

## Related User Stories
- [US-XXX]: [Story Title]

---

## Parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|
| [param_name] | [type] | Y/N | [description] |

## Environment Variables
| Variable | Maps To | Default |
|----------|---------|---------|
| [ENV_VAR_NAME] | [param_name] | [default value or "required"] |

## Defaults
- `[param_name]`: `[default_value]` — [rationale for default]

---

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | Required parameters **SHALL** cause startup failure if missing | Operational | Fail-fast | Integration Test |

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | Service starts with all required parameters set | Integration Test |
| FR-XXX-AC-2 | Service fails to start when required parameter is missing | Integration Test |
| FR-XXX-AC-3 | Default values are applied when optional parameters are omitted | Unit Test |

## Dependencies
- **Upstream**: [deployment infrastructure]
- **Downstream**: [all service FRs that consume config]
