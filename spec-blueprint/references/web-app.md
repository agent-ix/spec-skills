# Web-App Architectural Patterns

This guide documents the core architectural patterns expected when building `web-app` archetype applications in the Agent-IX ecosystem.

## 1. The Thin Routing Wrapper (Monolith Deconstruction Pattern)

When building web applications that compose domain-specific UI packages or shared component libraries, **do not embed routing logic (`useParams`, `useNavigate`) directly in the shared domain packages**.

Instead, use the **Thin Routing Wrapper** pattern in your web app's `src/pages/` or `src/views/` directory:

1. Create a "wrapper" component in the web app.
2. Extract URL parameters (e.g., `useParams`) and navigation hooks (e.g., `useNavigate`) inside the wrapper.
3. Pass these routing primitives as simple props (`id`, `onBack`, `onSelect`) to the pure domain component imported from a shared package.

### Why use this pattern?
- **Decoupling**: The shared domain packages remain completely pure and agnostic to the host application's routing strategy (e.g., `react-router-dom`).
- **Resiliency**: The packages do not assume the host application always uses the exact same URL structures.
- **Portability**: The components can be easily reused in environments without traditional URL routing (like an Electron window, an embedded IDE pane, or a strictly state-driven dashboard app).

### Example Implementation:

```tsx
import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { DomainEntityDetail } from '@agent-ix/domain-package';

export const EntityDetailView = () => {
    // 1. Extract routing context exclusively in the wrapper
    const { entityId } = useParams();
    const navigate = useNavigate();

    // 2. Pass down to the pure component as generic props
    return (
        <DomainEntityDetail 
            id={entityId} 
            onClose={() => navigate('/entities')} 
        />
    );
};
```
