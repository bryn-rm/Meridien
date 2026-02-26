from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="comms-agent")


class AgentTask(BaseModel):
    task_id: str
    intent: str
    context: dict = {}


@app.get('/healthz')
def healthz() -> dict:
    return {"status": "ok", "agent": "comms"}


@app.post('/task')
def task(task: AgentTask) -> dict:
    return {
        "task_id": task.task_id,
        "agent_target": "comms_agent",
        "summary": "3 high-priority messages need replies today, including one from your VP.",
        "data": {
            "urgent_threads": [
                {"from": "vp@company.com", "subject": "Q2 planning sync"},
                {"from": "client@acme.com", "subject": "Contract redlines"},
            ],
            "generated_at": datetime.utcnow().isoformat(),
        },
    }
