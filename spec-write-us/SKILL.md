---
name: spec-write-us
description: Write or format an ISO-compatible User Story (US) artifact.
---

# Write User Story

## Canonical Templates (FR-035)

> **Source of truth for User Story templates, frontmatter schemas, and
> required sections lives in the `spec-artifacts-iso` Filament Module**
> (`agent-ix/spec-artifacts-iso`, `spec_artifacts_iso/manifest.yaml`).
> This skill provides authoring guidance ("how to write a good User Story");
> the **data** (template, schema, allowed links, examples) is shipped by
> the module and consumed by:
>
> - `minijinja-cli` (agent CLI generation, the hot path)
> - `nunjucks` (spec-editor live preview)
> - `Jinja2` (Python validation / lint)
>
> See filament-core-service FR-035 for the manifest schema, FR-036 for the
> blessed archetype kinds, and NFR-005/NFR-006 for the rendering safety +
> performance constraints. When a template needs to change, edit the
> `.md.j2` in `spec-artifacts-iso/spec_artifacts_iso/templates/`,
> not the legacy `assets/` here (kept transitionally during migration).


Use this skill to capture informative, non-normative user intent.

## Rules

-   Informative Only: Do not use normative language (`SHALL`).
-   No System Behavior: Describe intent, not implementation.
-   Format: As a [Role], I want [Goal], So that [Value].

## Process

1.  Identify: Role, Goal, Value.
2.  Format: Use the standard template.
    -   Template: `assets/user-story-template.md`
    -   Example: `assets/US-001-example.md`
3.  Extract Acceptance: Defined as Given/When/Then scenarios.
4.  Context: Capture options and constraints as informative context.
5.  Output: Save to correct location.
    -   Single Repo: `spec/usecase/US-XXX-description.md`
    -   Multi-Repo: `specs/<category>/<component>/spec/usecase/US-XXX-description.md`

## Structure

-   Title: `[US-XXX] Title`
-   Story: Role/Goal/Value
-   Acceptance Criteria: `US-XXX-AC-N`

## Frontmatter (Required)

Every US file MUST contain the following YAML frontmatter:

```yaml
---
id: US-XXX
title: "<Title>"
artifact_type: US
relationships:          # Structured array of related FRs or StRs
  - target: "ix://org/repo/FR-XXX"
    type: "derives_into"
    cardinality: "1:N"
---
```
