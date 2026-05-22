---
name: spec-write-str
description: Write an authoritative Stakeholder Requirement (StR).
---

# Write Stakeholder Requirement

Use this skill to capture normative, outcome-focused stakeholder needs.

## Rules

-   Outcome Focused: What must be satisfied, not how.
-   Implementation Agnostic: No system internals or APIs.
-   Normative: May use `SHALL` to express stakeholder obligation.

## Process

1.  Identify Need: Source from users, policies, or contracts.
2.  Use Template:
    -   Source: `assets/stakeholder-requirement-template.md`
3.  Define Sections:
    -   Statement: Concise, clear expectation.
    -   Rationale: Why it matters (value, risk).
    -   Context: Operating environment/constraints.
    -   Success Indicators: Illustrative outcomes (not test steps).
4.  Output: Save to correct location.
    -   Single Repo: `spec/stakeholder/StR-XXX-description.md`
    -   Multi-Repo: `specs/<category>/<component>/spec/stakeholder/StR-XXX-description.md`

## Validation

-   Is it authoritative?
-   Is it implementation-free?
-   Are dependencies documented strictly in the YAML frontmatter `relationships` array?

## Frontmatter (Required)

Every StR file MUST contain the following YAML frontmatter:

```yaml
---
id: StR-XXX
title: "<Title>"
artifact_type: StR
relationships:          # Structured array of impacted features
  - target: "ix://org/repo/FR-XXX"
    type: "satisfied_by"
    cardinality: "1:N"
---
```
