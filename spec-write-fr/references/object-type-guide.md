# Domain Type Decision Guide

When an FR defines a domain object, set the `object:` frontmatter field and use the matching template.

## Business Objects (spec-objects-business)

- `entity` / `aggregate_root` / `nested_entity`: Data entity, model, or aggregate → `assets/business/entity-template.md`
- `value_object`: Immutable value type or enum → `assets/business/value-object-template.md`
- `event`: Domain events emitted by a service → `assets/business/event-template.md`
- `process`: End-to-end process spanning multiple FRs → `assets/business/process-template.md`
- `state_machine`: Lifecycle with states/transitions → `assets/business/state-machine-template.md`
- `repository`: Data access layer for an entity → `assets/business/repository-template.md`
- `domain`: Bounded context definition → `assets/business/domain-template.md`

## Architecture Objects (spec-objects-architecture)

- `api_endpoint`: REST/HTTP endpoint → `assets/architecture/api-endpoint-template.md`
- `queue`: Message queue or topic → `assets/architecture/queue-template.md`
- `data_schema`: Database table/schema → `assets/architecture/data-schema-template.md`
- `action`: Command/action (CLI, job, task) → `assets/architecture/action-template.md`
- `ui_component`: UI component with props → `assets/architecture/ui-component-template.md`
- `page`: Full page, route, or view → `assets/architecture/page-template.md`
- `dto`: API request/response schema (Pydantic/Zod model) → `assets/architecture/dto-template.md`
- `middleware`: Cross-cutting concern (auth, logging, validation) → `assets/architecture/middleware-template.md`

## Operational Objects (spec-objects-operational)

- `configuration`: Configuration parameters / env vars → `assets/operational/configuration-template.md`
- `migration`: Database migration → `assets/operational/migration-template.md`
- `hook`: Lifecycle event (startup, shutdown, pre/post) → `assets/operational/hook-template.md`
- `job`: Scheduled or recurring task → `assets/operational/job-template.md`

## Standard Behavioral FR

If the FR does not define a domain object, omit the `object:` field and use `assets/functional-requirement-template.md`.

## Tags (Discovery Dimensions)

Tags are cross-cutting concerns — they define how an FR is **used** or **discovered**, not what it structurally IS. Set tags in the `tags:` frontmatter field.

> **Important**: `integration` is a **tag**, not an object type. Never use `object: integration`.

Common tags:
- `integration`: Consumer-facing integration contracts, SDKs, connection guides → appears in Integration tab
- `consumer-facing`: Endpoints or APIs intended for external consumers
- `internal`: Internal service-to-service contracts
- `security`: Security-critical functionality → appears in Security tab

Example: An FR for an integration guide with no structural object:
```yaml
---
id: FR-007
title: "Consumer Integration Contract"
artifact_type: FR
tags: [integration]
---
```

Example: An endpoint that is both structural and consumer-facing:
```yaml
---
id: FR-001
title: "Login Endpoint"
artifact_type: FR
object: api_endpoint
tags: [consumer-facing]
---
```

## Semantic Graph Linkages (Verbs vs Nouns)

The Agent-IX ecosystem uses a strictly typed relationship graph to link specifications. 

The domain objects defined above act as the **Nouns** (Nodes) in the graph. The connections between them must be pure **Verbs** (Edges), defined in the `relationships:` array of the YAML frontmatter.

> **CRITICAL**: Do NOT bake the noun into the verb! (e.g., do not use `publishes_event` or `uses_api`). The database already knows the target is an `event` or an `api_endpoint` based on its domain type. 

### Valid Relationship Verbs
When linking specs, you must use one of the following strict semantic primitives:

**1. Operational & Flow:**
- `calls`: Synchronous invocation (e.g., an endpoint `calls` an external API).
- `publishes`: Asynchronous emission (e.g., a process `publishes` a domain event).
- `consumes`: Asynchronous reception (e.g., a worker process `consumes` a domain event).
- `triggers`: Process initiation (e.g., a scheduler `triggers` a job or macro-flow).

**2. Data & State:**
- `reads`: Safe, read-only data consumption (e.g., a component `reads` an entity).
- `writes`: Mutating data access (e.g., an endpoint `writes` an entity).

**3. Contracts & Constraints:**
- `requires`: Security and configuration bounds (e.g., an endpoint `requires` a specific permission scope or configuration).
- `implements`: Interface/contract fulfillment.

**4. Generic Structure:**
- `depends_on`: Library/package dependencies.
- `contains`: Composition (e.g., UI component `contains` sub-components, or Aggregate Root `contains` Entities).
- `transitions_to`: State machine flows.
- `references` / `related_to`: Loose general linkages (use only if no specific verb applies).
