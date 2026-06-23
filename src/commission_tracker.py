import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Commission:
    amount: float
    status: str

class CommissionTracker:
    def __init__(self):
        self.commissions = []

    def add_commission(self, amount, status):
        self.commissions.append(Commission(amount, status))

    def get_total_commissions(self):
        return sum(commission.amount for commission in self.commissions if commission.status == 'paid')

    def get_pending_commissions(self):
        return sum(commission.amount for commission in self.commissions if commission.status == 'pending')

    def get_paid_commissions(self):
        return sum(commission.amount for commission in self.commissions if commission.status == 'paid')

    def update_commission_status(self, index, status):
        if index < len(self.commissions):
            self.commissions[index].status = status

    def generate_pdf_statement(self):
        statement = {
            'total': self.get_total_commissions(),
            'pending': self.get_pending_commissions(),
            'paid': self.get_paid_commissions(),
            'commissions': [{'amount': commission.amount, 'status': commission.status} for commission in self.commissions]
        }
        return json.dumps(statement, indent=4)
