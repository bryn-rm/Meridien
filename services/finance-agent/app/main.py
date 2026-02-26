from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="finance-agent")


class AgentTask(BaseModel):
    task_id: str
    intent: str
    context: dict = {}


@app.get('/healthz')
def healthz() -> dict:
    return {"status": "ok", "agent": "finance"}


@app.post('/task')
def task(task: AgentTask) -> dict:
    return {
        "task_id": task.task_id,
        "agent_target": "finance_agent",
        "summary": "Cash position is stable; one unusual $82 subscription charge detected.",
        "data": {
            "balances": {"checking": 4210.25, "savings": 16240.11},
            "anomalies": [{"merchant": "AppSuite Pro", "amount": 82.00}],
            "generated_at": datetime.utcnow().isoformat(),
        },
    }
