---
id: NFR-XXX
title: "<Non-Functional Requirement Title>"
artifact_type: NFR
quality_attribute: performance_efficiency  # ISO 25010 enum — see nfr-frontmatter.schema.json
---
# [NFR-XXX] [Non-Functional Requirement Title]

---

## Statement

A single, atomic, normative statement.

- The system **SHALL** …
- The system **SHALL NOT** …

The statement MUST:
- Be measurable or objectively assessable
- Avoid describing functional behavior
- Avoid implementation details

---

## Scope

> OPTIONAL section.

| Item | Value |
|----|------|
| Applies To | [System / Subsystem / Interface / Deployment] |
| Operational Context | [Normal / Peak / Degraded / Failure] |
| Environment | [Prod / Staging / Dev / All] |

---

## Rationale

> OPTIONAL section.

Explain **why** this quality requirement exists.

- Business need
- Risk mitigation
- Regulatory obligation
- Operational necessity

This section is **informative**.

---

## Measurement and Evaluation

Define **how compliance is determined**.

| Metric | Target | Threshold | Method |
|------|--------|-----------|--------|
| [metric] | [value] | [min/max] | [test / monitoring / audit] |

> At least one metric MUST exist.

---

## Constraints and Assumptions

| ID | Constraint / Assumption | Type | Notes |
|----|-------------------------|------|------|
| NFR-XXX-CON-1 | [Item] | Technical / Regulatory / Operational | [Explanation] |

---

## Impacted Functional Requirements

| FR ID | Impact Description |
|----|--------------------|
| FR-XXX | [How this NFR constrains the FR] |

> NFRs constrain FRs; FRs MUST NOT redefine NFRs.

---

## Verification

| ID | Verification Activity | Evidence |
|----|-----------------------|---------|
| NFR-XXX-VR-1 | [Test / Audit / Review] | [Log / Report / Artifact] |

Verification MUST be objective and repeatable.

---

## Dependencies

> OPTIONAL section.

| Type | Reference | Description |
|----|-----------|-------------|
| Upstream | [StR / Regulation] | [Why required] |
| Downstream | [FR / System Component] | [Affected area] |

---

## Notes (Non-Normative)

Clarifications, examples, edge cases, or interpretation guidance.

- MUST NOT introduce new requirements
- MAY reference external standards or documents
