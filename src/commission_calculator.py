from dataclasses import dataclass
from typing import Dict

@dataclass
class Program:
    name: str
    commission_rate: float

@dataclass
class Agent:
    name: str
    programs: Dict[str, Program]

@dataclass
class Enrollment:
    program_name: str
    tuition_amount: float
    discount_amount: float
    agent_name: str

def calculate_commission(enrollment: Enrollment, agents: Dict[str, Agent]) -> float:
    agent = agents.get(enrollment.agent_name)
    if agent:
        program = agent.programs.get(enrollment.program_name)
        if program:
            final_tuition_amount = enrollment.tuition_amount - enrollment.discount_amount
            commission = final_tuition_amount * program.commission_rate
            return commission
    return 0.0

def update_agent_dashboard(agent_name: str, commission: float, agents: Dict[str, Agent]) -> None:
    agent = agents.get(agent_name)
    if agent:
        agent.commissions = agent.commissions + [commission] if hasattr(agent, 'commissions') else [commission]
