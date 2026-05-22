---
name: spec-analysis-risk-complexity
description: Identify technical risks and volatility in requirements before tasking.
---

# Risk & Complexity Analysis

This skill assesses the technical risk and stability of requirements to prevent implementation issues.

## Process

1.  **Technical Risk Identification**:
    -   Flag requirements involving:
        -   New or unproven technology.
        -   Concurrency or distributed systems.
        -   Security or compliance constraints.
        -   Hard performance guarantees.
    -   Classify risk: **High / Medium / Low**.

2.  **Volatility Assessment**:
    -   Identify requirements likely to change due to:
        -   Policy evolution.
        -   External contracts.
        -   Product discovery.
    -   **Action**: Mark high-volatility requirements for smaller, iterative tasks.

## Failure Domain Check
Gaps in failure domains increase risk. Reference `spec-failure-domain-analysis` for:
- Extension failures, Identity keys, Evaluation purity, Topological robustness.
