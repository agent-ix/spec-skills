# spec-skills

ISO-style specification authoring, review, and analysis skills for use with [Claude Code](https://docs.claude.com/en/docs/claude-code) (and any agent framework that supports the Anthropic skill format).

Maintained by [agent-ix](https://github.com/agent-ix); extracted from `agent-ix/agent-skills`. Org-agnostic — drop the directory into your own agent skill loader and use under any org.

## Skills

### Authoring
- `spec` — top-level spec reference
- `spec-create-spec` — initialize and manage specifications
- `spec-blueprint` — apply spec blueprints for application archetypes
- `spec-write-str` — Stakeholder Requirements
- `spec-write-us` — User Stories
- `spec-write-fr` — Functional Requirements
- `spec-write-nfr` — Non-Functional Requirements
- `spec-write-it` — Integration Tests
- `spec-us-to-fr` — derive FRs from User Stories
- `spec-convert-objects` — convert specs to parser-compatible object format

### Review & Analysis
- `spec-review` — quality, consistency, completeness review
- `spec-app-review` — application-type spec review
- `spec-object-review` — domain object audit
- `spec-matrix` — Test Matrix coverage
- `spec-security-analysis` — security standards compliance
- `spec-analysis-dependency` — dependency analysis
- `spec-analysis-evidence` — verification methods and evidence
- `spec-analysis-failure-domain` — unstated failure modes
- `spec-analysis-integrity` — completeness, consistency, atomicity gates
- `spec-analysis-risk-complexity` — technical risk and volatility
- `spec-analysis-scope-boundary` — system boundaries and responsibilities

### Downstream
- `spec-task-generation-readiness` — final readiness check
- `spec-to-plan` — convert spec to TDD project plan

## Conventions

Specs authored with these skills use:

- An `org:` frontmatter field naming the owning GitHub org/group. Templates ship with `<your-org>` as a placeholder — replace with your org's slug.
- An `ix://<org>/<repo>/<artifact-id>` URI scheme for cross-repo spec references (the `ix://` prefix is the spec cross-reference scheme, independent of any particular org).

## Optional upstream dependency

`spec-convert-objects` ships with `scripts/verify_objects.py`, which imports [`spec_parser_lib`](https://github.com/agent-ix/spec-parser-lib). That library is currently published only to agent-ix internal indexes; installing it from source is required to run the verifier. The rest of the skills in this repo have no runtime dependencies.

## License

MIT — see [LICENSE](./LICENSE).
