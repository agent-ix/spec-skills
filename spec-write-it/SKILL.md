---
name: spec-write-it
description: Generate required integration test cases to cover integrations with all external services. These tests will be run in a real env with real services.
---

# Generate Integration Test Cases

Use this skill to specify integration test cases that verify connectivity and behavior with external services. These tests run in real environments (e.g., KIND cluster) against actual service dependencies.

## Scope

- HTTP client integrations (API calls to other services)
- Event bus connections (Kafka, RabbitMQ)
- Database connections (Postgres, Redis)
- External APIs (cloud providers, third-party services)

## ID Schema

- IT-XXX: Integration Test identifier
- IT-XXX-SC-XX: Success Criteria within a test
- TD-XXX: Test Data fixture identifier

Each test case is a separate file. Sequential numbering within the service spec.

## Cross-Component References

ISO 29148 supports bidirectional traceability across system boundaries. You can reference requirements from other service specs:
- `catalog-service/FR-001`: Reference to another service's functional requirement
- `config-service/NFR-002`: Reference to another service's non-functional requirement

This is best practice for integration verification where your test validates behavior defined in another service's specification.

## Process

1. Identify Integration Points: List all external service dependencies from the codebase.
2. Select ID: Next available `IT-XXX`.
3. Use Template (REQUIRED): `assets/integration-test-template.md`
4. Document Each Section:
   - Dependencies: Other IT-XXX tests and cross-component FR/NFR references
   - Target Integration: Service and protocol
   - Preconditions: Environment and data state
   - Test Data: TD-XXX fixtures with rationale
   - Execution Plan: Atomic steps with timeout and criteria
   - Expected Outcome: Success condition and failure modes
   - Traceability: Link to FR/StR/NFR/TD
5. Output: Save to `spec/integration/IT-XXX-description.md`

## Output Location

- Single Repo: `spec/integration/IT-XXX-description.md`
- Multi-Repo: `specs/<category>/<component>/spec/integration/IT-XXX-description.md`

## Rules

- No Code Examples: Describe behavior, not implementation
- Technical Prose: Explain WHY and WHAT data at each step
- Atomic Steps: One action per step with independent success criteria
- Explicit Timeouts: Every action step must have a timeout
- Traceability Required: Every test links to at least one FR/StR/NFR
- Cross-Component OK: Reference requirements from other service specs

## IT Reality Testing Rules

> [!CAUTION]
> Integration tests are **ALWAYS REAL** by default. Nothing is mocked unless
> the spec explicitly says so. An IT that only checks imports or constructs
> models without exercising real behavior is a **GAP**.

### Mandatory AC Categories

Every IT specification MUST include acceptance criteria from BOTH categories:

#### Category 1: Real Setup ACs
Verify the real, non-mocked environment is correctly established:
- Service under test is running and healthy (real health endpoint, real HTTP response)
- Dependencies are available (real database, real message bus, real external service)
- Test data fixtures are loaded into real stores
- Configuration is applied through real config loading paths

#### Category 2: Real Output ACs
Verify REAL OUTPUT from REAL SERVICES — not mocked return values:
- HTTP responses from real endpoints (status codes, headers, body structure)
- Database state changes from real queries (rows inserted, updated, deleted)
- Event messages published to real event bus topics
- File system state from real tool execution (files created, content correct)
- SSE/WebSocket streams from real connections (event types, data payloads)
- LLM responses through real provider chains (token streaming, tool calls)

### What "Real" Means

| Real (Required) | Not Real (GAP) |
|-----------------|----------------|
| POST to API endpoint, assert response body | `assert MyModel is not None` |
| Query database after write, verify rows changed | `MyModel(field="value")` without DB |
| Publish event, consume from real bus, verify payload | `assert EventSchema is not None` |
| GET /health, verify HTTP 200 with status body | `assert app is not None` |
| Load config from file, call API, verify behavior | `assert config.key == "value"` |
| Connect WebSocket, send message, read response | `assert MessageType.TEXT exists` |

### Mocking Policy

- **Default: NO MOCKS.** ITs exercise real service boundaries.
- **Approved mock targets** (only when the spec explicitly requires it):
  - External third-party APIs (payment, auth, cloud) → use test doubles with real HTTP
  - External services outside the test boundary → use contract-faithful stubs
- **Never mock:** HTTP transport, config loading, database connections, file I/O,
  session storage, event publishing, health endpoints, WebSocket/SSE connections.
- When a mock IS used, the IT MUST state:
  - WHY the real service cannot be used
  - WHAT the mock replaces (specific boundary)
  - HOW the mock is verified to be faithful (contract tests, schema validation)

### Common IT Patterns by Service Type

#### API Services (FastAPI, REST)
- **CRUD ITs** MUST POST/GET/PUT/DELETE to real endpoints, verify response codes,
  body structure, and database state after each operation.
- **Validation ITs** MUST send invalid payloads and verify real 4xx error responses.
- **Auth ITs** MUST send requests with/without credentials, verify real 401/403.

#### Database Services (pg-data-service)
- **Migration ITs** MUST run real Alembic migrations, verify schema state.
- **Query ITs** MUST insert/query/update/delete against real PostgreSQL, verify row state.
- **Constraint ITs** MUST violate unique/FK constraints, verify real DB errors propagated.

#### Event-Driven Services (FastStream workers)
- **Publish ITs** MUST publish to real Kafka/AMQP topic, consume, verify payload.
- **Consume ITs** MUST produce test event, verify service processes it and side-effects visible.

#### Worker Services (deploy-worker, scenario-runner)
- **Job ITs** MUST submit real job, verify execution, verify completion state in store.
- **Timeout ITs** MUST submit slow job, verify timeout and cleanup behavior.

#### Agent Services (LLM orchestration)
- **LLM ITs** MUST use a deterministic scripted LLM (e.g., `ScenarioChatModel`),
  invoke via real API, verify tool calls executed and results returned.
- **Tool ITs** MUST execute real tools, verify real file/process state.
- **Streaming ITs** MUST connect real SSE/WS endpoints, verify event sequence.

## Frontmatter (Required)

Every IT file MUST begin with YAML frontmatter:

```yaml
---
id: IT-XXX
title: "<Title>"
type: IT
status: DRAFT              # DRAFT | APPROVED | IMPLEMENTED | VERIFIED | DEPRECATED
relationships:             # Required: FR/StR/NFR references
  - target: "ix://org/repo/FR-XXX"
    type: "verifies"
    cardinality: "1:1"
---
```

## References

- Template: [assets/integration-test-template.md](assets/integration-test-template.md)
- Example: [assets/integration-test-example.md](assets/integration-test-example.md)
