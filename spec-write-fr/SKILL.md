---
name: spec-write-fr
description: Define a normative Functional Requirement (FR) with complete specification.
---

# Create Functional Requirement

## Canonical Templates (FR-035)

> **Source of truth for Functional Requirement templates, frontmatter schemas, and
> required sections lives in the `spec-artifacts-iso` Filament Module**
> (`agent-ix/spec-artifacts-iso`, `spec_artifacts_iso/manifest.yaml`).
> This skill provides authoring guidance ("how to write a good Functional Requirement");
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


Specify detailed system behavior and technical implementation requirements.

## Rules

- Specific: Unambiguous definitions.
- Normative: Use `SHALL` / `SHALL NOT`.
- Complete: Inputs, outputs, errors, dependencies.
- **Separation of Concerns**: Domain-typed FRs must be purely structural (defining schemas, payloads, or endpoints). Behavioral triggers and validations (the "when", "if", and "why") must remain in non-domain Source FRs. Do NOT copy behavioral Acceptance Criteria into Domain FRs.

## Process

1. Select ID: Next available `FR-XXX`.
2. Determine domain type. See [object-type-guide.md](references/object-type-guide.md).
3. Use template:
   - Domain-typed FR: select template from the guide.
   - Standard behavioral FR: `assets/functional-requirement-template.md`
   - Example: `assets/FR-001-example.md`
4. Specify sections:
   - Domain-typed FRs: use domain-specific sections from the template.
   - Standard FRs: Inputs, Outputs, Behavior, States.
   - Options: Implementation alternatives (`FR-XXX-OPT-A`).
   - Constraints: Limiters (`FR-XXX-CON-1`).
   - Errors: Conditions, codes, recovery.
   - Acceptance Criteria: Verifiable checks (`FR-XXX-AC-1`).
5. Save to correct location:
   - Single Repo: `spec/functional/FR-XXX-description.md`
   - Multi-Repo: `specs/<category>/<component>/spec/functional/FR-XXX-description.md`

> [!IMPORTANT]
> Domain-typed FRs use domain-specific top-level sections (e.g. `## Properties`, `## Event Types`, `## Endpoint`). For dependencies, you MUST use the `relationships:` YAML frontmatter array instead of plain text under a `## Dependencies` section. For Domain-typed FRs, **Acceptance Criteria must only test structural compliance** (e.g. schema validation).

## Frontmatter (Required)

Every FR file MUST contain the following YAML frontmatter:

```yaml
---
id: FR-XXX
title: "<Title>"
artifact_type: FR
relationships:          # Required: Structured array of all dependencies
  - target: "ix://org/repo/Target"
    type: "calls"       # Valid types: calls, implements, publishes, consumes, reads, writes, triggers, requires, depends_on
    cardinality: "1:1"
---
```

When defining dependencies, use precise semantic verbs. For example, if a process makes a synchronous API call to another system, use a `calls` relationship. If an endpoint publishes an event to a broker, use a `publishes` relationship. If an endpoint is secured by a specific permission, use a `requires` relationship to the scope FR.

## Structure

Define all fields with types, validation rules, and descriptions.

Domain-typed FRs additionally include `object:` and optionally `parent_process:` (see [object-type-guide](references/object-type-guide.md)).
