export type AgentTarget =
  | 'calendar_agent'
  | 'finance_agent'
  | 'health_agent'
  | 'goals_agent'
  | 'comms_agent';

export interface AgentTask {
  task_id: string;
  agent_target: AgentTarget;
  intent: string;
  context: Record<string, unknown>;
  priority: 'urgent' | 'normal' | 'background';
  deadline_ms: number;
  require_action: boolean;
}
