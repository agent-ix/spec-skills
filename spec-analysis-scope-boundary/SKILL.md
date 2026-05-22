---
name: spec-analysis-scope-boundary
description: Define system boundaries and allocate responsibilities for ISO-style specifications.
---

# Scope & Boundary Analysis

This skill defines the system context and allocates technical responsibilities to components.

## Process

1.  **System Boundary Definition**:
    -   Explicitly define in-scope system responsibilities.
    -   Identify external dependencies.
    -   Distinguish assumed vs guaranteed behavior.
    -   **Deliverable**: System context diagram.

2.  **Responsibility Allocation**:
    -   For each FR/SR, assign ownership to a logical component or subsystem.
    -   Classify responsibility as:
        -   Core logic
        -   Infrastructure
        -   Cross-cutting concern (auth, logging, metrics)
    -   **Note**: This step defines *where* work belongs, not *how* it is done.
