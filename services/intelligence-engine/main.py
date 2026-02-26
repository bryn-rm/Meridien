from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Insight:
    user_id: str
    insight_type: str
    message: str
    recommendation: str


class CrossDomainAnalyser:
    def analyse(self, user_id: str) -> list[Insight]:
        return [
            Insight(
                user_id=user_id,
                insight_type="stress_spending_correlation",
                message="Spending rises on days with 5+ hours of meetings.",
                recommendation="Enable a no-spend rule on overloaded days.",
            ),
            Insight(
                user_id=user_id,
                insight_type="goal_calendar_misalignment",
                message="Only 45 minutes were scheduled for your top weekly goal.",
                recommendation="Block two 90-minute focus sessions this week.",
            ),
        ]


if __name__ == '__main__':
    analyser = CrossDomainAnalyser()
    for insight in analyser.analyse('demo-user'):
        print(f"[{insight.insight_type}] {insight.message} -> {insight.recommendation}")
