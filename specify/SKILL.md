---
name: specify
description: Initialize and manage requirements specifications with component-type instructions.
---

# Create Requirements Specification

Create the `spec.md` and manage the requirements lifecycle.

## Workflow

1. Initialize: Create `spec.md` from `assets/spec-template.md`.
2. Capture Requirements:
   - `spec-write-str`: Stakeholder needs.
   - `spec-write-us`: User stories.
3. Specify Behavior:
   - `spec-us-to-fr`: Derive FRs from stories.
   - `spec-write-fr`: System behavior.
   - `spec-write-nfr`: Quality constraints.
4. Define Domain Model:
   - Identify domain objects from master spec § 8-9.
   - Create typed FRs for entities, events, state machines, processes.
   - Create architecture FRs for API endpoints, queues, schemas, UI components.
   - Create operational FRs for configuration, migrations.
   - See `spec-write-fr` [object-type-guide.md](../spec-write-fr/references/object-type-guide.md).
5. Verify Coverage:
   - `spec-matrix`: Test matrix.
6. Review (required):
   - `spec-review`: Validate quality.

## Process

1. Check prerequisites:
   - Single Repo: `spec/`
   - Multi-Repo: `specs/<category>/<component>/spec/`
2. Copy template: `assets/spec-template.md`
3. Set frontmatter:
   - `artifact_type`: Must be `master-requirements`.
   - `name`: Component name matching the repo.
   - `org`: Organization owning the component.
   - `component_type`: Authoritative type (e.g., `fastapi-service`, `react-lib`).
   - `tags`: Optional capabilities (e.g., `[postgres, sqlmodel]`).
   - `relationships`: Structured array of relationship objects (target, type, cardinality). Do NOT use `depends_on`. Specify exact semantic linkages such as `calls`, `implements`, `publishes`, `consumes`, `reads`, `writes`, `triggers`, or `requires`.

> [!IMPORTANT]
> Individual artifacts (FR, NFR, StR, US, IT) also require YAML frontmatter with `id`, `title`, and `type`. See each writing skill's **Frontmatter** section.
4. Customize: Processes, states, diagrams.
5. Apply component instructions from `golden-path/components/<component-type>/agent-instructions.md`.

## Repository Structure

```
spec/
├── spec.md                     # Master specification
├── stakeholder/                # StR-XXX
├── usecase/                    # US-XXX
├── functional/                 # FR-XXX (behavioral + domain-typed)
├── non-functional/             # NFR-XXX
├── tests.md                    # Test Matrix
└── assets/                     # Diagrams, POCs
```

## ID Schema

- Stakeholder: `StR-XXX`
- User Story: `US-XXX`
- Functional: `FR-XXX`
- Non-Functional: `NFR-XXX`
- Test Case: `TC-XXX`

---

## Application-Type Specifications

> [!IMPORTANT]
> When `component_type: application`, use `assets/app-spec-template.md` instead of `assets/spec-template.md`. The application spec standard is fundamentally different from a service or library spec.

### What the Application Spec Owns

An application spec describes how multiple component repositories compose into a coherent system. It owns **only cross-service concerns** — things that cannot be expressed within any single component's spec.

| Section | What to Write |
|---|---|
| **Architecture Rationale (ADRs)** | Why this architecture? Why these trade-offs? One ADR entry per major decision that shaped the system shape. |
| **Cross-service Sequence Diagrams** | End-to-end flows that span >1 service (Login, Checkout, Deploy). No single service can own these. |
| **System-level NFRs** | SLA/uptime, scale limits, RTO/RPO — targets for the *composed* system, not individual services. |
| **External Consumer Contract** | How does an integrating engineer use this application as a whole? Aggregate "quickstart" across components. |
| **Scope Boundaries** | What the system explicitly does NOT do. Deliberate exclusions, not future work. |
| **Security Model** | Actor roles, trust hierarchy, capability matrix. Cross-cutting — not owned by any single service. |
| **Deployment Topology** | Namespace layout, ingress routes, service discovery, shared secrets/config. |
| **Observability Strategy** | Dashboard names, alert policies for the system. Per-service metrics stay in service specs. |

### What Stays at Service Level

- Per-endpoint API contracts (routes, schemas)
- Database schema and data models
- Per-service latency/throughput NFRs
- Events and signals (defined at service or domain level — never pulled to app level)
- Per-service error codes and test matrix
- Environment variables beyond shared/cross-service ones

### Required Functional Requirements

For `component_type: application`, every spec MUST include:

| FR Object Type | Purpose | Example |
|---|---|---|
| `domain` | Bounded context, ER diagram, subdomain map | FR-001 Auth Domain |
| `process` | One FR per major cross-service workflow | FR-002 Login Process |
| `configuration` | Shared config across multiple services | FR-006 Auth Configuration |
| `integration` | External consumer contract (how to integrate) | FR-007 Consumer Integration Contract |

### Required Non-Functional Requirements

| NFR | Purpose |
|---|---|
| Security Constraints | Cryptography, transport, error handling standards |
| System Reliability | Uptime SLA, p99 latency, scale limits, RTO/RPO |
| Deployment Topology | Namespace, ingress, service discovery, secret mounts |

### Reference Implementation

Refer to a known well-formed application spec in your org as a model when authoring a new one.
