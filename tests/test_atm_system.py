# test_atm_system.py
import pytest
from src.atm_system import ATMUser

@pytest.fixture
def active_user():
    """Fixture to create a fresh user for each test."""
    return ATMUser(name="Vinayak", pin=1234, balance=1000.0)

def test_authentication(active_user):
    # Test correct PIN
    assert active_user.verify_pin(1234) is True
    assert active_user.is_authenticated is True

    # Test wrong PIN
    active_user.logout()
    assert active_user.verify_pin(9999) is False
    assert active_user.is_authenticated is False

def test_unauthorized_access(active_user):
    # Attempting to check balance without login
    assert active_user.get_balance() == "Authentication Required"
    
    # Attempting to withdraw without login
    assert active_user.withdraw(100) == "Authentication Required"

def test_deposit_logic(active_user):
    active_user.verify_pin(1234)
    
    # Standard deposit
    assert active_user.deposit(500) == 15.0
    # Negative deposit check
    assert active_user.deposit(-50) == "Invalid Amount"

def test_withdraw_logic(active_user):
    active_user.verify_pin(1234)
    
    # Standard withdrawal
    assert active_user.withdraw(200) == 80.0
    # Overdraft attempt
    assert active_user.withdraw(2000) == "Insufficient Funds"
    # Zero/Negative withdrawal
    assert active_user.withdraw(0) == "Invalid Amount"

def test_logout(active_user):
    active_user.verify_pin(1234)
    active_user.logout()
    assert active_user.is_authenticated is False
    assert active_user.get_balance() == "Authentication Required"
