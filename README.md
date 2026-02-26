# MERIDIAN — AI Life Operating System

This repository is a working scaffold for the Meridian architecture: a multi-agent personal AI Chief of Staff with an orchestrator, specialist agents, MCP server stubs, a voice gateway skeleton, and a runnable dashboard.

## What is implemented

- **Python FastAPI agent mesh**
  - Orchestrator service that fans out tasks to five domain agents in parallel.
  - Calendar, Finance, Health, Goals, and Comms agents with `/task` and `/healthz` endpoints.
- **Shared A2A models/client** in `packages/python-shared`.
- **TypeScript packages**
  - Shared `packages/types` interfaces.
  - Calendar MCP server stub (`packages/mcp-servers/calendar`).
  - Voice gateway websocket stub (`services/voice-gateway`).
- **Frontend**
  - Simple dashboard at `frontend/index.html` to request daily briefings.
- **Infra bootstrap**
  - Basic Terraform provider + Cloud Run service resource.
  - GitHub Actions CI smoke check.

## Quick start

### 1) Run all services

```bash
docker compose up --build
```

Services:
- Orchestrator: `http://localhost:8000`
- Calendar: `http://localhost:8001`
- Finance: `http://localhost:8002`
- Health: `http://localhost:8003`
- Goals: `http://localhost:8004`
- Comms: `http://localhost:8005`
- Frontend: `http://localhost:3000`

### 2) Generate a briefing via API

```bash
curl -X POST http://localhost:8000/briefing
```

### 3) Use the dashboard
Open `http://localhost:3000`, click **Generate briefing**.

## Architecture notes

This codebase follows the requested design direction:

- **A2A for agent-to-agent orchestration** via `AgentTask` and `A2AClient`.
- **MCP for integration boundary** with a Calendar MCP server stub.
- **Daily briefing synthesis** in orchestrator endpoint `/chat` + `/briefing`.
- **Cross-domain intelligence service** scaffold in `services/intelligence-engine/main.py`.

## Next production steps

1. Replace mock agent responses with ADK-based tool execution.
2. Add Firestore session persistence and user profiles.
3. Connect real MCP servers (Google Calendar, Gmail, Plaid, Health).
4. Upgrade frontend to Next.js app router implementation.
5. Add auth (Firebase Auth) and tenant-aware data isolation.
