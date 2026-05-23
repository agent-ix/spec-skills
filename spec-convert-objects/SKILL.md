---
name: spec-convert-objects
description: Convert existing specs to parser-compatible object format.
---

# Convert Existing Specs to Object Format

Identify and convert existing domain content buried in specs into parser-compatible domain-typed FRs.

## When to Use

- Repo specs define entities, events, state machines, or processes in old format (inline `### Data Models`, scattered event lists, state diagrams in master spec).
- Parser yields zero domain objects for a repo with obvious domain concepts.

## Process

1. Scan `spec/` for domain content patterns:
   - `class X(SQLModel)` in `### Data Models` → `entity`
   - `class X(BaseModel)` in `### Data Models` → `value_object`
   - `class X(str, Enum)` in `### Data Models` → `value_object`
   - `### Events Emitted` table or bullet list → `event`
   - `stateDiagram-v2` in spec.md § 8 → `state_machine`
   - `### States` inline table in FR → `state_machine`
   - Multi-FR workflow in prose → `process`
   - `### Endpoints` table → `api_endpoint`
   - Queue/exchange config in spec → `queue`
   - `### Data Models` with SQL column info → `data_schema`
   - CRUD endpoint FR with repository pattern → `repository`
   - Env var tables / config sections → `configuration`
   - Alembic/migration references → `migration`
   - `erDiagram` in master spec § 8 → `domain`

2. Create new domain-typed FRs using `spec-write-fr` templates:
   - Assign next available FR-XXX IDs.
   - Set `object:` frontmatter. See [object-type-guide.md](../spec-write-fr/references/object-type-guide.md).
   - Use parser-expected section headings and table columns.
   - Cross-reference the source FR in Dependencies.

3. Distribute Acceptance Criteria (ACs) and Constraints cleanly to avoid duplication:
   - **Source FR (Behavioral)**: Keeps all ACs related to *when*, *if*, and *why* an action occurs (e.g., "When ingestion starts, emit event X", "If user lacks admin role, return 403").
   - **New Domain FR (Structural)**: Keeps only ACs and Constraints related to *what* the structure or schema is (e.g., "The event payload MUST contain `repo_id`", "The API MUST validate against the provided JSON schema").
   - If a Domain FR template includes default ACs that overlap with the Source FR's behavioral triggers, **delete the overlapping ACs from the new Domain FR**. Do not duplicate them.

4. Update source FRs:
   - Replace inline domain definitions with references to new dedicated FRs.
   - Keep behavioral content (Behavior, ACs) in the source FR, strictly following the separation of concerns above.
   - Add tracing to the new domain FR in Dependencies.

4. Update `spec.md`:
   - § 8 "Domain Model" is **only** for `object: domain` FRs (bounded context definitions). Do NOT add § 8 for other domain types (`ui_component`, `entity`, `value_object`, etc.).
   - § 9 "Events and Signals" references `object: event` and `object: state_machine` FRs.
   - All other domain-typed FRs are referenced via the § 4 Functional Requirements table only.

5. Verify with the parser using the verification script:

```bash
python3 <path-to>/spec-convert-objects/scripts/verify_objects.py spec/
```

The script groups domain objects by type, reports FRs without domain frontmatter, and exits non-zero if no domain objects are found. **Run this after every conversion.**
