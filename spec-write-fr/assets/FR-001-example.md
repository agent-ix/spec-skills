---
id: FR-001
title: "GitHub Repository Discovery"
type: FR
---
# [FR-001] GitHub Repository Discovery

## Description
Implement the capability to clone a GitHub repository, scan for Kubernetes configuration directories, and extract component metadata including deployment manifests, service definitions, and configuration templates.

## Related User Stories
- [US-001](../examples/US-001-example.md): Catalog Project Ingestion

## Specification

### Inputs
| Field | Type | Required | Validation | Description |
|-------|------|----------|------------|-------------|
| repository_url | string | Y | Valid GitHub URL | The GitHub repository URL (https or git format) |
| branch | string | N | Valid git ref | Branch to clone (default: main) |
| auth_token | string | N | Valid PAT | Personal access token for private repos |
| scan_paths | list[string] | N | Valid paths | Specific paths to scan (default: scan entire repo) |

### Outputs
| Field | Type | Description |
|-------|------|-------------|
| project_id | string | Unique identifier for the ingested project |
| components | list[Component] | List of discovered components with metadata |
| scan_summary | ScanSummary | Summary of scan results (files scanned, components found, errors) |

### Behavior
1. Clone the repository using `git clone --depth 1` to minimize bandwidth
2. Scan for directories containing Kubernetes configuration files (*.yaml, *.yml)
3. Parse YAML files to identify resource types (Deployment, Service, StatefulSet, etc.)
4. Extract component metadata:
   - Component name (from metadata.name)
   - Component type (inferred from resource kind and labels)
   - Configuration surfaces (environment variables, volume mounts, config maps)
   - Dependencies (service references, database connections)
5. Store normalized component inventory in database
6. Emit `ProjectIngested` event

### States (if applicable)
| State | Description | Transitions |
|-------|-------------|-------------|
| Pending | Ingestion request received | → Cloning |
| Cloning | Repository being cloned | → Scanning, Failed |
| Scanning | Scanning for components | → Complete, Failed |
| Complete | Ingestion successful | Terminal state |
| Failed | Ingestion failed | Terminal state |

## Options
| ID | Option | Description | Default | Impact |
|----|--------|-------------|---------|--------|
| FR-001-OPT-A | Shallow Clone | Use git clone --depth 1 | Y | Faster, less disk space; can't access full history |
| FR-001-OPT-B | Full Clone | Clone entire repository history | N | Slower, more disk space; full history available |

## Constraints
| ID | Constraint | Type | Rationale | Validation |
|----|------------|------|-----------|------------|
| FR-001-CON-1 | Max repo size: 1GB | Technical | Prevent excessive disk/memory usage | Check repo size via GitHub API before cloning |
| FR-001-CON-2 | Clone timeout: 5 minutes | Technical | Prevent hanging operations | Terminate clone operation after timeout |
| FR-001-CON-3 | Must use read-only access | Business | Never modify user's code | Verify git remote is read-only |

## Error Handling
| Error Condition | Error Code | Response | Recovery |
|-----------------|------------|----------|----------|
| Invalid repository URL | CATALOG-001 | Return 400 with validation message | User corrects URL |
| Authentication failure | CATALOG-002 | Return 401, prompt for valid token | User provides valid credentials |
| Repository not found | CATALOG-003 | Return 404 with helpful message | User verifies repository exists |
| Repository too large | CATALOG-004 | Return 413, suggest alternatives | User contacts support or uses local path |
| Clone timeout | CATALOG-005 | Return 504, log partial results | Retry with longer timeout or shallow clone |
| No Kubernetes configs found | CATALOG-006 | Return 200 with empty components list | User verifies repository has K8s configs |

## Performance Requirements
- **Response Time**: Ingestion initiation < 500ms (async processing)
- **Throughput**: Handle 10 concurrent ingestions
- **Resource Limits**: Max 1GB memory per ingestion, 10GB disk space total

## Security Considerations
- Store auth tokens in Vault, never in database
- Use secure git protocol (HTTPS or SSH)
- Sanitize file paths to prevent directory traversal
- Validate YAML files to prevent malicious content
- Rate limit ingestion requests to prevent abuse

## Acceptance Criteria
| ID | Criteria | Verification Method |
|----|----------|---------------------|
| FR-001-AC-1 | Can clone public GitHub repository | Integration test |
| FR-001-AC-2 | Can clone private GitHub repository with auth token | Integration test |
| FR-001-AC-3 | Correctly identifies Deployment resources | Unit test |
| FR-001-AC-4 | Correctly identifies Service resources | Unit test |
| FR-001-AC-5 | Extracts environment variables from deployment manifests | Unit test |
| FR-001-AC-6 | Handles repositories with no Kubernetes configs gracefully | Integration test |
| FR-001-AC-7 | Enforces size limit and returns appropriate error | Integration test |
| FR-001-AC-8 | Enforces timeout and returns appropriate error | Integration test |

## Dependencies
- **Upstream**: None (foundational capability)
- **Downstream**: 
  - Config Service (uses discovered components)
  - Scenario Service (references discovered components)
  - Orchestrator Service (deploys discovered components)

## Notes
- Consider using libgit2 for better performance than shelling out to git
- May want to cache cloned repositories to avoid re-cloning
- Edge case: Monorepo with multiple projects - may need to support multiple scan roots
- Consider supporting GitLab and Bitbucket in the future
