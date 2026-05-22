---
id: StR-XXX
title: "<Stakeholder Requirement Title>"
type: StR
---
# [StR-XXX] [Stakeholder Requirement Title]

---

## Stakeholder Need

A concise, declarative statement describing **what the stakeholder needs or expects**.

The statement:
- Describes **intent and desired outcome**
- Is written from a stakeholder perspective (user, business, regulator, operator)
- Avoids system behavior, mechanisms, or solutions
- Avoids implementation detail

Example patterns (illustrative only):
- “Stakeholders require the ability to …”
- “The organization needs assurance that …”
- “Users need to be able to …”

---

## Stakeholder(s)

| Attribute | Value |
|---------|-------|
| Role / Group | [User / Business / Regulator / Operator / Other] |
| Organization / Domain | [If applicable] |
| Interest / Authority | [Decision-maker / Influencer / Affected party] |

---

## Rationale

Explanation of **why this need exists**.

May include:
- Business value or opportunity
- Operational necessity
- Legal, regulatory, or contractual driver
- Risk or impact if unmet

This section provides **context**, not prescriptions.

---

## Context and Assumptions

Background information that frames the stakeholder need.

May include:
- Operational environment
- Existing systems or processes
- Known assumptions, constraints, or uncertainties

Items listed here are **inputs for later analysis and refinement**.

---

## Indicators of Success (Informative)

Observable outcomes that would indicate the stakeholder need has been addressed.

These indicators:
- Are illustrative
- Are not verification criteria
- Are not test cases

| ID | Indicator | Explanation |
|----|-----------|-------------|
| StR-XXX-IS-1 | [Outcome] | [Why this indicates success] |
| StR-XXX-IS-2 | [Outcome] | [Why this indicates success] |

---

## Stakeholder Constraints (Contextual)

Limits, obligations, or conditions expressed by stakeholders.

| ID | Constraint | Source | Notes |
|----|-----------|--------|------|
| StR-XXX-CON-1 | [Constraint] | [Business / Legal / Policy] | [Clarification or context] |

These constraints:
- Provide context at the stakeholder level
- May be validated, refined, or transformed later
- Are not yet system or functional constraints

---

## Dependencies and Relationships

| Type | Reference | Description |
|----|-----------|-------------|
| Upstream | [Policy / Regulation / Contract] | [Relationship] |
| Lateral | [Other StR] | [Relationship] |
| Downstream | [Expected FR / NFR] | [Anticipated derivation] |

---

## Priority and Risk (Informative)

| Attribute | Value |
|---------|-------|
| Business Value | High / Medium / Low |
| Urgency | High / Medium / Low |
| Risk if Unmet | High / Medium / Low |

Used for planning and sequencing only.

---

## Notes (Informative)

Clarifications, examples, open questions, or discussion points.

- May include scenarios or illustrations
- May highlight areas needing further analysis
- Does not introduce new requirements

---

## Traceability

| From | To |
|----|----|
| Stakeholder Need | StR-XXX |
| Derived Functional Requirements | [FR-XXX] |
| Derived Non-Functional Requirements | [NFR-XXX] |

Traceability links may be added incrementally as the specification evolves.
