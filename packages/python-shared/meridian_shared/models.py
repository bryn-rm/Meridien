from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


class AgentTask(BaseModel):
    task_id: str
    agent_target: Literal[
        "calendar_agent", "finance_agent", "health_agent", "goals_agent", "comms_agent"
    ]
    intent: str
    context: dict[str, Any] = Field(default_factory=dict)
    priority: Literal["urgent", "normal", "background"] = "normal"
    deadline_ms: int = 5000
    require_action: bool = False


class AgentTaskResult(BaseModel):
    task_id: str
    agent_target: str
    summary: str
    data: dict[str, Any] = Field(default_factory=dict)
    generated_at: datetime = Field(default_factory=datetime.utcnow)
