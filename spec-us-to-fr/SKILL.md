---
name: spec-us-to-fr
description: Derive normative Functional Requirements (FR) from User Stories (US).
---

# Convert User Story to Functional Requirement

Transform informative user intent into normative system behavior.

## Rules

- Atomic: Decompose story into specific atomic behaviors.
- Normative: Use `SHALL` / `SHALL NOT`.
- No copying: Translate to technical specification, do not copy story text.
- Verifiable: Must have independent acceptance criteria.

## Process

1. Analyze: Identify system responsibilities in the `US-XXX`.
2. Decompose into typed FRs:
   - Behavioral: API logic, business rules (standard template).
   - Entity: Data models with typed fields (`domain: entity`).
   - Event: Domain events emitted (`domain: event`).
   - API Endpoint: REST endpoints (`domain: api_endpoint`).
   - Queue: Message contracts (`domain: queue`).
   - Process: End-to-end workflows (`domain: process`).
   - State Machine: Entity lifecycles (`domain: state_machine`).
   - Config: Configuration schemas (`domain: configuration`).
   - Full list: `spec-write-fr` [object-type-guide.md](../spec-write-fr/references/object-type-guide.md).
3. Create FRs:
   - Use `spec-write-fr` with the appropriate domain template.
   - Link back to `US-XXX`.
4. Define:
   - Inputs/Outputs: Typed and validated.
   - Error Handling: Failure modes.
   - Constraints: Technical limits (not options).
5. Save to correct location:
   - Single Repo: `spec/functional/FR-XXX-description.md`
   - Multi-Repo: `specs/<category>/<component>/spec/functional/FR-XXX-description.md`
