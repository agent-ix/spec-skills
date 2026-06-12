---
name: spec-write-nfr
description: Define a normative Non-Functional Requirement (NFR) or quality constraint.
---

# Write Non-Functional Requirement

Use this skill to define constraints on *how well* the system performs (quality attributes).

## Rules

-   One Attribute: One quality per NFR (e.g., Security, Performance).
-   Measurable: Must be objectively assessable.
-   No Behavior: Do not define *what* the system does, but *how* it does it.
-   Normative: Use `SHALL`.
-   Traceable: Impacted FRs must be defined in the YAML frontmatter `relationships:` array.

## Attributes (ISO 25010)

-   Performance Efficiency
-   Reliability / Availability
-   Security
-   Usability
-   Maintainability
-   Portability
-   Scalability
-   Compliance

## Process

1.  Select Attribute: Choose primary quality attribute.
2.  Use Template:
    -   Source: `assets/nonfunctional-requirement-template.md`
3.  Define:
    -   Statement: Atomic normative constraint.
    -   Measurement: Metric, Target, Threshold, Method (required table).
    -   Verification: objective, repeatable check of the table.
    -   Impact: List affected FRs (`FR-XXX`).
4.  Output: Save to correct location.
    -   Single Repo: `spec/non-functional/NFR-XXX-description.md`
    -   Multi-Repo: `specs/<category>/<component>/spec/non-functional/NFR-XXX-description.md`

## Frontmatter (Required)

Every NFR file MUST contain the following YAML frontmatter:

```yaml
---
id: NFR-XXX
title: "<Title>"
artifact_type: NFR
quality_attribute: performance_efficiency   # ISO 25010 enum (snake_case) — replaces the retired "## Quality Attribute" section
relationships:          # Required: Structured array of affected FRs
  - target: "ix://org/repo/FR-XXX"
    type: "constrains"
    cardinality: "1:N"
---
```

## Body Shape (spec-artifacts-iso v0.2.0)

- REQUIRED (level 2): `## Statement`, `## Measurement and Evaluation`
  (table headers exactly `Metric | Target | Threshold | Method`, ≥1 row),
  `## Verification`.
- OPTIONAL: `## Scope`, `## Rationale`, `## Acceptance Criteria`,
  `## Dependencies`. The Measurement table IS the acceptance-criteria
  equivalent for measurable NFRs; use the optional AC section only for
  policy NFRs whose compliance checks don't reduce to metrics.
- `quality_attribute` lives in FRONTMATTER (enum), not as a body section.
