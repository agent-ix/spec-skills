---
name: spec-task-generation-readiness
description: Final readiness check before generating implementation tasks.
---

# Task Generation Readiness Criteria

This skill acts as the final gate validation before task generation begins.

## Process

1.  **Verify Pre-conditions**:
    -   Task generation MAY begin only when:
        -   All requirements are atomic and testable.
        -   Ownership is assigned.
        -   Dependencies are known.
        -   Risks are classified.
        -   Verification strategy is defined.
        -   `spec-failure-domain-analysis` checklist is complete.

2.  **Failure Consequence**:
    -   Failure to meet these conditions WILL result in unstable tasking.
