"""Tests for the ChequingAccount class."""

_author_ = "Nkechi Echeta"
_version_ = "1.1.0"
_credits_ = "ACE Faculty"

import unittest
from bank_account.chequing_account import ChequingAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy
from datetime import date

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
        self.assertEqual(self.account.account_number, self.account_number)
        self.assertEqual(self.account.client_number, self.client_number)
        self.assertEqual(self.account.balance, self.balance)
        self.assertEqual(self.account._date_created, self.date_created)
        self.assertEqual(
            self.account._ChequingAccount__overdraft_limit,
            self.overdraft_limit
        )
        self.assertEqual(
            self.account._ChequingAccount__overdraft_rate, 
            self.overdraft_rate
        )

    def test_get_service_charge_balance_above_overdraft_limit(self):
        # Act
        expected_charge = self.account.get_service_charge()
        
        # Assert
        self.assertGreaterEqual(expected_charge, 0)

    def test_get_service_charge_balance_below_overdraft_limit(self):
        # Arrange
        self.account.withdraw(600.00)
        
        # Act
        expected_charge = self.account.get_service_charge()
        
        # Assert
        self.assertGreater(expected_charge, 0)

    def test_get_service_charge_balance_at_overdraft_limit(self):
        # Arrange
        self.account.withdraw(400.00) 
        
        # Act
        expected_charge = self.account.get_service_charge()
        
        # Assert
        self.assertGreater(expected_charge, 0)

if __name__ == '__main__':
    unittest.main()
