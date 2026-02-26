from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="goals-agent")


class AgentTask(BaseModel):
    task_id: str
    intent: str
    context: dict = {}


@app.get('/healthz')
def healthz() -> dict:
    return {"status": "ok", "agent": "goals"}


@app.post('/task')
def task(task: AgentTask) -> dict:
    return {
        "task_id": task.task_id,
        "agent_target": "goals_agent",
        "summary": "Your Q2 shipping goal is behind pace; schedule two 90-minute build blocks this week.",
        "data": {
            "goals": [
                {"title": "Ship v1 Meridian MVP", "progress": 0.55, "target": "2026-04-15"}
            ],
            "generated_at": datetime.utcnow().isoformat(),
        },
    }
