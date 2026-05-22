# [US-001] Catalog Project Ingestion

## Story
**As a** platform operator
**I want** to ingest GitHub repositories or local filesystem paths into the catalog
**So that** I can discover and manage deployable components across multiple projects

## Context
The Catalog Service needs to accept project sources (GitHub repos or local paths), scan their contents, identify Kubernetes-based deployable components, and maintain a normalized inventory. This is the foundational capability enabling all downstream configuration, deployment, and observability features.

## Acceptance Criteria

### [US-001-AC-1] GitHub Repository Ingestion
- **Given**: A valid GitHub repository URL with Kubernetes configurations
- **When**: The operator submits the repository for ingestion
- **Then**: The system clones the repository, scans for components, and stores the inventory

### [US-001-AC-2] Local Filesystem Ingestion
- **Given**: A valid local filesystem path with Kubernetes configurations
- **When**: The operator submits the path for ingestion
- **Then**: The system scans the directory, identifies components, and stores the inventory

### [US-001-AC-3] Component Classification
- **Given**: A project has been ingested
- **When**: The system scans Kubernetes configurations
- **Then**: Each component is correctly classified (service, worker, database, UI, etc.)

## Options
| ID | Option | Description | Trade-offs |
|----|--------|-------------|------------|
| US-001-OPT-A | Sync Ingestion | Process ingestion synchronously in API request | Simple but blocks API; not suitable for large repos |
| US-001-OPT-B | Async Ingestion | Emit event and process via worker | Scalable and responsive but requires event infrastructure |

## Constraints
| ID | Constraint | Rationale | Impact |
|----|------------|-----------|--------|
| US-001-CON-1 | Read-only access to source repositories | Never modify user's code | Must use git clone --depth 1 or equivalent |
| US-001-CON-2 | Must detect Kubernetes config directories | Focus on K8s deployable components | Ignore non-K8s projects |

## Dependencies
- None (foundational capability)

## Priority
- **Business Value**: High (foundational feature)
- **Implementation Effort**: High (complex scanning logic)
- **Risk**: Medium (depends on GitHub API availability)

## Notes
- Should support private repositories with authentication
- Consider rate limiting for GitHub API calls
- May need to handle monorepos with multiple deployable components
- Edge case: What if a repository has no Kubernetes configurations?
