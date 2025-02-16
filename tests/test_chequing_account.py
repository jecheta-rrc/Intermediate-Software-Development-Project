"""Tests for the ChequingAccount class."""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

import unittest
from datetime import date
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    """Tests the ChequingAccount class."""

    def setUp(self) -> None:
        # Arrange
        self.account_number = 123456
        self.client_number = 98765
        self.balance = 500.00
        self.date_created = date(2025, 2, 13)
        self.overdraft_limit = 100.00
        self.overdraft_rate = 0.05
    
        # Act
        self.account = ChequingAccount(
        self.account_number, self.client_number, self.balance,
        self.date_created, self.overdraft_limit, self.overdraft_rate
        )

    def test_init_initialize_state(self):
        # Assert
        self.assertEqual(self.account._BankAccount__account_number, self.account_number)
        self.assertEqual(self.account._BankAccount__client_number, self.client_number)
        self.assertEqual(self.account._BankAccount__balance, self.balance)
        self.assertEqual(self.account._date_created, self.date_created)
        self.assertEqual(self.account._ChequingAccount__overdraft_limit, self.overdraft_limit)
        self.assertEqual(self.account._ChequingAccount__overdraft_rate, self.overdraft_rate)

    def test_init_overdraft_limit_invalid_type(self):
        account = ChequingAccount(self.account_number, self.client_number, self.balance, 
                                self.date_created, "invalid", self.overdraft_rate)
        self.assertEqual(account.overdraft_limit, -100.00)
  
    def test_init_overdraft_rate_invalid_type(self):
        # Act
        account = ChequingAccount(self.account_number, self.client_number, self.balance, 
                                self.date_created, self.overdraft_limit, "invalid")
    
        # Assert 
        self.assertEqual(account.overdraft_rate, 0.05)

    def test_get_service_charge_balance_above_overdraft_limit(self):
        # Arrange
        self.account._BankAccount__balance = 50.00
    
        # Act and Assert
        self.assertEqual(self.account.get_service_charge(), ChequingAccount.BASE_SERVICE_CHARGE)

    def test_get_service_charge_balance_below_overdraft_limit(self):
        # Arrange
        self.account._BankAccount__balance = -150.00 
    
        # Act
        expected_charge = ChequingAccount.BASE_SERVICE_CHARGE + ((self.account.overdraft_limit - 
                                                                self.account.balance) * 
                                                                self.account.overdraft_rate)
    
        # Assert
        self.assertEqual(self.account.get_service_charge(), expected_charge)
    
    def test_get_service_charge_balance_at_overdraft_limit(self):
        # Arrange
        self.account._BankAccount__balance = -self.overdraft_limit 
    
        # Act
        expected_charge = ChequingAccount.BASE_SERVICE_CHARGE + ((self.overdraft_limit - 
                                                                self.account.balance) * 
                                                                self.account.overdraft_rate)
    
        # Assert
        self.assertEqual(self.account.get_service_charge(), expected_charge)

if __name__ == '__main__':
  unittest.main()
