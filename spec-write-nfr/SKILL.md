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
    -   Measurement: Metric, Target, Threshold.
    -   Verification: Test, Audit, or Inspection.
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
relationships:          # Required: Structured array of affected FRs
  - target: "ix://org/repo/FR-XXX"
    type: "constrains"
    cardinality: "1:N"
---
```
