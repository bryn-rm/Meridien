from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="health-agent")


class AgentTask(BaseModel):
    task_id: str
    intent: str
    context: dict = {}


@app.get('/healthz')
def healthz() -> dict:
    return {"status": "ok", "agent": "health"}


@app.post('/task')
def task(task: AgentTask) -> dict:
    return {
        "task_id": task.task_id,
        "agent_target": "health_agent",
        "summary": "Sleep: 6h 18m, HRV is 78% of baseline. Recommend lower cognitive load in morning.",
        "data": {
            "sleep_hours": 6.3,
            "hrv": 42,
            "hrv_baseline": 54,
            "readiness": 61,
            "generated_at": datetime.utcnow().isoformat(),
        },
    }
