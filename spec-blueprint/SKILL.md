---
description: Query and apply spec blueprints for application archetypes. Use when starting a new spec, auditing existing FRs, or scaffolding domain objects.
---

# Spec Blueprint Skill

Use this skill to determine the **expected FR composition** for a given application archetype (e.g., `pg-data-service`, `web-app`, `faststream-worker`).

## When to Use

- Starting a new spec for a known archetype
- Auditing existing FRs for completeness
- Scaffolding missing domain objects

## Workflow

### 1. Identify the Archetype

Determine the Element type from one of:
- The repo's `element_id` in catalog-service
- The `repo_type` field
- User input (e.g., "this is a data service")

Known archetypes with blueprints:
- `fastapi-service` — REST API services
- `pg-data-service` — Data services (extends `fastapi-service`)
- `faststream-worker` — Message queue workers
- `web-app` — React web applications
- `react-lib` — React component libraries
- `application` — Logical application groupings

### 2. Fetch the Blueprint

**Via API** (if catalog-service is running):
```
GET /api/v1/elements/{element_id}/resolved-pattern
```

**Via seed data** (offline reference; the canonical source is the `spec-artifacts-*` modules for archetypes / artifact_types and the `spec-objects-*` modules for object_types — both contribute via the Module Manifest, filament-core FR-035. Treat the table below as a cached projection, not the authority):

| Archetype | Expected FR Types |
|---|---|
| `fastapi-service` | `api_endpoint`(1+), `dto`(1+), `configuration`(1), `middleware`(0+), `hook`(0-1) |
| `pg-data-service` | inherits `fastapi-service` + `entity`(1+), `repository`(1/entity), `data_schema`(1+), `migration`(1+) |
| `faststream-worker` | `queue`(1+), `action`(1+), `event`(1+), `configuration`(1), `hook`(0-1) |
| `web-app` | `page`(1+), `ui_component`(1+), `configuration`(1) |
| `react-lib` | `ui_component`(1+) |
| `application` | `domain`(1), `configuration`(1), `process`(0+), `event`(0+) |

> **Note:** `integration` is a **tag**, not an object type. FRs defining integration contracts
> should use `tags: [integration]` in frontmatter (no `object:` field). The Application Detail
> View discovers integration content via tag filtering. Recommend at least one FR tagged
> `integration` for `application` and `web-app` archetypes.

### 3. Audit Existing FRs

For each entry in the blueprint:
1. Scan `spec/functional/` for FRs with matching `object:` frontmatter
2. Count matches against `cardinality`
3. Report gaps

Output format:
```
✅ entity: 3 found (required: 1+)
✅ repository: 3 found (required: 1-per-entity)
❌ migration: 0 found (required: 1+) — MISSING
⚠️ middleware: 0 found (optional: 0+)
```

### 4. Generate Missing FRs

For each gap marked `❌`:
1. Look up the object type in [object-type-guide.md](../spec-write-fr/references/object-type-guide.md) — each row maps 1:1 to a `spec-objects-*` module repo (the canonical definition).
2. Use the `spec-write-fr` skill to generate the FR (templates resolved from the relevant `spec-artifacts-*` module per filament-core FR-035 `artifact_types[]`).
3. Assign the next available FR ID.

## Related Skills

- **spec-write-fr**: Write individual FRs using domain-typed templates
- **specify**: Initialize a new spec container
- **spec-object-review**: Post-audit domain object integrity check
