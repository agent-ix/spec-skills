# [FR-XXX] [Requirement Title]

## Description
A clear, specific, **normative** description of the functional requirement.  
The description **SHALL** state externally observable behavior using deterministic language.

---

## Related User Stories
- [US-XXX]: [Story Title]

---

## Specification

### Inputs
| Field | Type | Required | Validation | Description |
|------|------|----------|------------|-------------|
| [field] | [type / enum] | Y/N | [rules / allowed values] | [description] |

> **Note:** Enumerated values define **mandatory constrained choices**, not optional behavior.

---

### Outputs
| Field | Type | Description |
|------|------|-------------|
| [field] | [type] | [description] |

---

### Behavior
Normative description of expected system behavior.

- The system **SHALL** …
- When `[input] = [value]`, the system **SHALL** …
- The system **SHALL NOT** …

---

### States (if applicable)
| State | Description | Transitions |
|------|-------------|-------------|
| [state] | [description] | [valid transitions] |

---

## Constraints
Constraints define mandatory limits, rules, or selections that govern this requirement.

| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-XXX-CON-1 | [Constraint statement using SHALL] | Technical / Business / Regulatory | [Why] | [How verified] |

---

## Error Handling
| Error Condition | Error Code | Response | Recovery |
|-----------------|------------|----------|----------|
| [condition] | [code] | [behavior] | [recovery action] |

---

## Security Considerations
Security, authentication, authorization, and data protection requirements associated with this functional behavior.

---

## Acceptance Criteria
Each criterion **SHALL** be independently verifiable.

| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-XXX-AC-1 | [observable outcome] | Unit / Integration / System Test |

---

## Dependencies
- **Upstream**: [prerequisites]
- **Downstream**: [dependent functions or requirements]

---

## Notes (Non-Normative)
Implementation hints, edge cases, rationale, or open questions.  
This section **SHALL NOT** introduce new requirements.
