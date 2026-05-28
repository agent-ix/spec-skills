# spec-skills

ISO-style specification authoring, review, and analysis skills for use with [Claude Code](https://docs.claude.com/en/docs/claude-code) (and any agent framework that supports the Anthropic skill format).

Maintained by [agent-ix](https://github.com/agent-ix); extracted from `agent-ix/agent-skills`. Org-agnostic — drop the directory into your own agent skill loader and use under any org.

## Skills

### Authoring
- `spec` — top-level spec reference
- `specify` — initialize and manage specifications
- `spec-blueprint` — apply spec blueprints for application archetypes
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

## Conventions

Specs authored with these skills use:

- An `org:` frontmatter field naming the owning GitHub org/group. Templates ship with `<your-org>` as a placeholder — replace with your org's slug.
- An `ix://<org>/<repo>/<artifact-id>` URI scheme for cross-repo spec references (the `ix://` prefix is the spec cross-reference scheme, independent of any particular org).

## License

MIT — see [LICENSE](./LICENSE).
