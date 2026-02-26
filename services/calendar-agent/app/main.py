from datetime import date, datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="calendar-agent")


class AgentTask(BaseModel):
    task_id: str
    intent: str
    context: dict = {}


@app.get('/healthz')
def healthz() -> dict:
    return {"status": "ok", "agent": "calendar"}


@app.post('/task')
def task(task: AgentTask) -> dict:
    today = date.today().isoformat()
    meetings = [
        {"title": "Team Standup", "start": f"{today}T09:30:00", "duration_minutes": 30},
        {"title": "Roadmap Review", "start": f"{today}T14:00:00", "duration_minutes": 60},
    ]
    return {
        "task_id": task.task_id,
        "agent_target": "calendar_agent",
        "summary": "2 meetings today, with one focus gap available at 11:00.",
        "data": {"meetings": meetings, "generated_at": datetime.utcnow().isoformat()},
    }
