---
name: spec-analysis-dependency
description: Analyze dependencies and separate enablement from feature work.
---

# Dependency & Ordering Analysis

This skill identifies prerequisite relationships and sequences work effectively.

## Process

1.  **Requirement Dependency Graph**:
    -   Identify prerequisite relationships.
    -   Identify foundational vs derived capabilities.
    -   **Deliverable**: Directed acyclic graph (logical order, not schedule).

2.  **Enablement vs Feature Separation**:
    -   Classify requirements as:
        -   **Enablement** (frameworks, abstractions, scaffolding).
        -   **Feature** (business or user-visible behavior).
    -   **Rule**: Enablement requirements MUST be tasked first.
