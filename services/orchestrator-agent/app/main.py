from __future__ import annotations

import os
import uuid
from datetime import datetime

from fastapi import FastAPI
from meridian_shared import A2AClient, AgentTask
from pydantic import BaseModel

app = FastAPI(title="meridian-orchestrator")


class UserMessage(BaseModel):
    user_id: str = "demo-user"
    message: str


def build_client() -> A2AClient:
    return A2AClient(
        {
            "calendar_agent": os.getenv("CALENDAR_AGENT_URL", "http://calendar-agent:8001"),
            "finance_agent": os.getenv("FINANCE_AGENT_URL", "http://finance-agent:8002"),
            "health_agent": os.getenv("HEALTH_AGENT_URL", "http://health-agent:8003"),
            "goals_agent": os.getenv("GOALS_AGENT_URL", "http://goals-agent:8004"),
            "comms_agent": os.getenv("COMMS_AGENT_URL", "http://comms-agent:8005"),
        }
    )


@app.get('/healthz')
def healthz() -> dict:
    return {"status": "ok", "agent": "orchestrator"}


@app.post('/chat')
async def chat(user_message: UserMessage) -> dict:
    task_id = str(uuid.uuid4())
    client = build_client()
    tasks = [
        AgentTask(task_id=task_id, agent_target="calendar_agent", intent="get_today_schedule"),
        AgentTask(task_id=task_id, agent_target="finance_agent", intent="get_cash_position"),
        AgentTask(task_id=task_id, agent_target="health_agent", intent="get_sleep_readiness"),
        AgentTask(task_id=task_id, agent_target="goals_agent", intent="get_goal_momentum"),
        AgentTask(task_id=task_id, agent_target="comms_agent", intent="get_urgent_messages"),
    ]
    results = await client.send_many(tasks)
    synthesis = " ".join(result.summary for result in results)
    response = (
        f"Morning brief for {user_message.user_id}: {synthesis} "
        "Top actions: protect one deep-work block and reply to urgent VP/client messages."
    )
    return {
        "task_id": task_id,
        "user_message": user_message.message,
        "response": response,
        "agent_results": [result.model_dump(mode='json') for result in results],
        "generated_at": datetime.utcnow().isoformat(),
    }


@app.post('/briefing')
async def briefing(user_id: str = "demo-user") -> dict:
    payload = await chat(UserMessage(user_id=user_id, message="Generate daily briefing"))
    return {"briefing_text": payload["response"], "generated_at": payload["generated_at"]}
