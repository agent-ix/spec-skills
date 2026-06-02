# spec-skills

ISO-style specification authoring, review, and analysis skills for use with [Claude Code](https://docs.claude.com/en/docs/claude-code) (and any agent framework that supports the Anthropic skill format).

Maintained by [agent-ix](https://github.com/agent-ix);  Org-agnostic — drop the directory into your own agent skill loader and use under any org.


## Quickstart

1. Add skills to claude config ~/.claude/skills

## Usage

1. Generate user stories, requirements, and a full spec.

```
/specify A note taking app based on
```

2. Review your work with `/spec-review` and other analysis skils

```
/spec-review
```

3. Generate test matrix and plan
```
/spec-matrix /spec-to-plan
```

4. Build!

```
Implement plan
```



## Skills

### Authoring
- `spec` — top-level spec reference
- `specify` — initialize and manage specifications

##### Artifacts
- `spec-write-str` — Stakeholder Requirements
- `spec-write-us` — User Stories
- `spec-write-fr` — Functional Requirements
- `spec-write-nfr` — Non-Functional Requirements
- `spec-write-it` — Integration Tests
- `spec-us-to-fr` — derive FRs from User Stories

### Review & Analysis
- `spec-review` — quality, consistency, completeness review
- `spec-app-review` — application-type spec review
- `spec-object-review` — domain object audit
- `spec-matrix` — Test Matrix coverage
- `spec-security-analysis` — security standards compliance
- `spec-dependency-analysis` — dependency analysis
- `spec-evidence-analysis` — verification methods and evidence
- `spec-failure-domain-analysis` — unstated failure modes
- `spec-integrity-analysis` — completeness, consistency, atomicity gates
- `spec-risk-complexity-analysis` — technical risk and volatility
- `spec-scope-boundary-analysis` — system boundaries and responsibilities

### Downstream
- `spec-to-plan` — convert spec to TDD project plan (includes the pre-tasking readiness gate)

## Helpers
- `spec-blueprint` — build a spec for an archtype from a golden reference implementation

## License

MIT — see [LICENSE](./LICENSE).
