# Handoff: Backport spec.md Frontmatter — `name`, `org`, `depends_on`

## Context

The `spec-create-spec` skill template now requires three new frontmatter fields in every repo's `spec/spec.md`:

```yaml
name: <component-name>    # Required: matches repo name
org: agent-ix              # Required: owning organization
depends_on:                # Components this depends on
  - <dependency-name>
```

**Completed**: `agent-duncan` (commit `81ae3c3`), `agent_skills` skill + template (commit `4391eb9`).

## Instructions

For each repo below:

1. Open `spec/spec.md`
2. Add `name` and `org` immediately after `artifact_type: master-requirements`
3. Add `depends_on` before `standards_alignment` (or at end of frontmatter if no `standards_alignment`)
4. `depends_on` values are name — use the repo basename
5. **Verify** each dependency is an agent-ix repo by checking it exists in `~/dev`. Only include internal components, NOT third-party packages (e.g. pydantic, tenacity, otel are NOT agent-ix repos). Match package names to repo directories — some differ (e.g. package `observability` → repo `py-observability`).
if not in spec, check pyproject.toml or package.json for component name
6. If no dependencies, use `depends_on: []`
7. Commit: `git add spec/spec.md && git commit -m "Add name, org, and depends_on to spec.md frontmatter"`

### Example Diff

```diff
 ---
 artifact_type: master-requirements
+name: config-overlay
+org: agent-ix
 component_type: python-lib
 tags:
   - json-merge-patch
 implementation_language: python
+depends_on: []

 standards_alignment:
   - iso-iec-ieee-29148
 ---
```

## Repo Inventory

> [!TIP]
> `depends_on` values should come from `pyproject.toml` (Python) or `package.json` (TS/React) — only list **internal** Agent-IX components, not third-party packages.

### ✅ Done

| Repo | Status |
|------|--------|
| agent-duncan | ✅ `81ae3c3` |

### 📋 Pending — Platform & Templates

| Repo | `component_type` |
|------|-------------------|
| local | platform |
| fastapi-cookiecutter | template |
| faststream-worker-cookiecutter | template |
| pg-data-service-cookiecutter | template |
| python-lib-cookiecutter | template |
| typescript-lib-cookiecutter | template |
| typescript-react-lib-cookiecutter | template |
| web-app-cookiecutter | template |

### 📋 Pending — Python Libraries

| Repo | `component_type` |
|------|-------------------|
| auth-py | python-lib |
| auth-fastapi | python-lib |
| config-overlay | python-lib |
| cloud-manager-integrations | python-lib |
| data-store | python-lib |
| event-models | python-lib |
| event-schema-registry | python-lib |
| ix-agent-comms | python-lib |
| ix-agent-core | python-lib |
| ix-agent-extensions | python-lib |
| ix-agent-hitl | python-lib |
| ix-agent-tools | python-lib |
| ix-sandbox-backend | python-lib |
| job-execution | python-lib |
| k8s-orchestration | python-lib |
| naming-lib | python-lib |
| platform-test-kit | python-lib |
| py-observability | python-lib |
| py-permissions | python-lib |
| py-project | python-lib |
| py-state-machine | python-lib |
| pytest-results | python-lib |
| pytest-sqlmodel | python-lib |
| pytest-summary | python-lib |
| python-lib | python-lib |
| secrets-ref | python-lib |
| spec-parser-lib | python-lib |
| sqlmodel-fixtures | python-lib |
| sqlmodel-publisher | python-lib |
| workflow-execution | python-lib |
| ix-agent-fastapi | python-lib |

### 📋 Pending — Python Services

| Repo | `component_type` |
|------|-------------------|
| auth-service | pg-data-service |
| catalog-service | pg-data-service |
| config-service | pg-data-service |
| cloud-manager | fastapi-service |
| cloudmanager-local-sync | fastapi-service |
| identity | pg-data-service |
| ix-agent-browser-control | fastapi-service |
| ix-agent-chat | pg-data-service |
| ix-agent-messaging-bridge | fastapi-service |
| ix-agent-sandbox-control | python-lib |
| ix-agent-terminal-control | python-lib |
| k8s-gateway | fastapi-service |
| orchestrator-service | pg-data-service |
| py_code | pg-data-service |
| review-service | pg-data-service |
| scenario-service | pg-data-service |
| scheduler-service | pg-data-service |
| secrets-injector-webhook | fastapi-service |
| spec-core-service | pg-data-service |
| spec-editor-gateway | fastapi-service |
| status-service | fastapi-service |

### 📋 Pending — Workers

| Repo | `component_type` |
|------|-------------------|
| deploy-worker | faststream-worker |
| event-monitor | faststream-worker |
| faststream-worker | faststream-worker |
| scenario-runner | faststream-worker |
| secret-refresh-controller | faststream-worker |

### 📋 Pending — TypeScript / React Libraries

| Repo | `component_type` |
|------|-------------------|
| chat-input | react-lib |
| chat-window | react-lib |
| cloud-manager-ui-components | react-lib |
| cloud-manager-ui-config | react-lib |
| cloud-manager-ui-core | react-lib |
| cloud-manager-ui-dashboard | react-lib |
| cloud-manager-ui-domain | react-lib |
| cloud-manager-ui-flow-editor | react-lib |
| cloud-manager-ui-repos | react-lib |
| cloud-manager-ui-services | react-lib |
| cloud-manager-ui-types | typescript-lib |
| code-block-editor | react-lib |
| code-block-renderer | react-lib |
| code-diff-editor | react-lib |
| code-diff-renderer | react-lib |
| frame | react-lib |
| ix-agent-client | typescript-react-lib |
| ix-themes | react-lib |
| jest-results | typescript-lib |
| markdown-editor | react-lib |
| rjsf-ix-theme | react-lib |
| spec-comments | react-lib |
| spec-editor | react-lib |
| spec-editor-repos | react-lib |
| spec-editor-ui | react-lib |
| spec-hierarchy | react-lib |
| spec-reports | react-lib |
| spec-reviews | react-lib |
| spec-ui-shared | react-lib |
| spec-view-compare | react-lib |
| spec-view-editor | react-lib |
| spec-view-project | react-lib |
| spec-view-review | react-lib |
| typesetter | react-lib |
| ui-data-table | react-lib |

### 📋 Pending — Web Apps

| Repo | `component_type` |
|------|-------------------|
| cloud-manager-ui | web-app |
| core-web-ui | web-app |
| ix-agent-canvas-ui | web-app |
| ix-agent-chat-app | web-app |

### 📋 Pending — GitHub Actions

| Repo | `component_type` |
|------|-------------------|
| docker-actions | github-actions |
| git-actions | github-actions |
| nodejs-actions | github-actions |
| python-lib-actions | github-actions |
| python-service-actions | github-actions |

### 📋 Pending — Other

| Repo | `component_type` |
|------|-------------------|
| agent_skills | agent-skills |
| glitchtip-mcp | mcp-server |
| loki-mcp | mcp-server |
| spec-domain-events | event-schema-library |
| workflow-service | fastapi-service |
