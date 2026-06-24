from commission_calculator import calculate_commission, update_agent_dashboard
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

def test_calculate_commission():
    program = Program('Test Program', 0.1)
    agent = Agent('Test Agent', {'Test Program': program})
    agents = {'Test Agent': agent}
    enrollment = Enrollment('Test Program', 1000.0, 0.0, 'Test Agent')
    commission = calculate_commission(enrollment, agents)
    assert commission == 100.0

def test_calculate_commission_with_discount():
    program = Program('Test Program', 0.1)
    agent = Agent('Test Agent', {'Test Program': program})
    agents = {'Test Agent': agent}
    enrollment = Enrollment('Test Program', 1000.0, 200.0, 'Test Agent')
    commission = calculate_commission(enrollment, agents)
    assert commission == 80.0

def test_calculate_commission_with_zero_tuition():
    program = Program('Test Program', 0.1)
    agent = Agent('Test Agent', {'Test Program': program})
    agents = {'Test Agent': agent}
    enrollment = Enrollment('Test Program', 0.0, 0.0, 'Test Agent')
    commission = calculate_commission(enrollment, agents)
    assert commission == 0.0

def test_update_agent_dashboard():
    program = Program('Test Program', 0.1)
    agent = Agent('Test Agent', {'Test Program': program})
    agents = {'Test Agent': agent}
    enrollment = Enrollment('Test Program', 1000.0, 0.0, 'Test Agent')
    commission = calculate_commission(enrollment, agents)
    update_agent_dashboard(enrollment.agent_name, commission, agents)
    assert hasattr(agents['Test Agent'], 'commissions')
    assert agents['Test Agent'].commissions == [100.0]
