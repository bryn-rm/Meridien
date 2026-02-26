from __future__ import annotations

import asyncio
from typing import Iterable

import httpx

from .models import AgentTask, AgentTaskResult


class A2AClient:
    def __init__(self, base_urls: dict[str, str], timeout: float = 8.0) -> None:
        self.base_urls = base_urls
        self.timeout = timeout

    async def send_task(self, task: AgentTask) -> AgentTaskResult:
        if task.agent_target not in self.base_urls:
            raise ValueError(f"Unknown agent target: {task.agent_target}")
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                f"{self.base_urls[task.agent_target]}/task",
                json=task.model_dump(mode="json"),
            )
            response.raise_for_status()
        return AgentTaskResult.model_validate(response.json())

    async def send_many(self, tasks: Iterable[AgentTask]) -> list[AgentTaskResult]:
        return await asyncio.gather(*(self.send_task(task) for task in tasks))
