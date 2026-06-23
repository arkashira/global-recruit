import pytest
from commission_tracker import CommissionTracker, Commission

def test_add_commission():
    tracker = CommissionTracker()
    tracker.add_commission(100.0, 'pending')
    assert len(tracker.commissions) == 1
    assert tracker.commissions[0].amount == 100.0
    assert tracker.commissions[0].status == 'pending'

def test_get_total_commissions():
    tracker = CommissionTracker()
    tracker.add_commission(100.0, 'paid')
    tracker.add_commission(200.0, 'pending')
    assert tracker.get_total_commissions() == 100.0

def test_get_pending_commissions():
    tracker = CommissionTracker()
    tracker.add_commission(100.0, 'pending')
    tracker.add_commission(200.0, 'paid')
    assert tracker.get_pending_commissions() == 100.0

def test_get_paid_commissions():
    tracker = CommissionTracker()
    tracker.add_commission(100.0, 'paid')
    tracker.add_commission(200.0, 'pending')
    assert tracker.get_paid_commissions() == 100.0

def test_update_commission_status():
    tracker = CommissionTracker()
    tracker.add_commission(100.0, 'pending')
    tracker.update_commission_status(0, 'paid')
    assert tracker.commissions[0].status == 'paid'

def test_generate_pdf_statement():
    tracker = CommissionTracker()
    tracker.add_commission(100.0, 'paid')
    tracker.add_commission(200.0, 'pending')
    statement = tracker.generate_pdf_statement()
    assert 'total' in statement
    assert 'pending' in statement
    assert 'paid' in statement
    assert 'commissions' in statement

def test_edge_case_empty_commissions():
    tracker = CommissionTracker()
    assert tracker.get_total_commissions() == 0
    assert tracker.get_pending_commissions() == 0
    assert tracker.get_paid_commissions() == 0
