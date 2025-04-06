"""This module defines the TestSavingsAccount class.

Usage: 
    To execute all tests in the terminal execute the following command:
    
    $ python -m unittest tests/test_savings_account.py
"""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class TestSavingsAccount(unittest.TestCase):
    """Tests the SavingsAccount class."""

    def setUp(self):
        """Set up test data before each test."""
        
        self.account_number = 123456
        self.client_number = 654321
        self.balance = 500.0
        self.minimum_balance = 50.0
        self.date_created = date(2025, 2, 13)

        # Assign the strategy and create account instance
        self.account = SavingsAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.minimum_balance
        )

    def test_init_initialize_state(self):
        # Assert: Verify attributes through public accessors
        self.assertEqual(self.account.account_number, self.account_number)
        self.assertEqual(self.account.client_number, self.client_number)
        self.assertEqual(self.account.balance, self.balance)
        self.assertEqual(self.account.get_service_charges(), self.account._service_charge_strategy.calculate_service_charges(self.account))

    def test_get_service_charge_balance_greater_than_minimum(self):
        # Act
        expected_charge = self.account._service_charge_strategy.calculate_service_charges(self.account)
        
        # Assert
        self.assertEqual(self.account.get_service_charges(), expected_charge)

    def test_get_service_charge_balance_equal_to_minimum(self):
        # Arrange
        self.account.update_balance(-self.balance + self.minimum_balance)
        
        # Act
        expected_charge = self.account._service_charge_strategy.calculate_service_charges(self.account)
        
        # Assert
        self.assertEqual(self.account.get_service_charges(), expected_charge)

    def test_get_service_charge_balance_less_than_minimum(self):
        # Arrange
        self.account.update_balance(-self.balance + self.minimum_balance - 1)
        
        # Act
        expected_charge = self.account._service_charge_strategy.calculate_service_charges(self.account)
        
        # Assert
        self.assertEqual(self.account.get_service_charges(), expected_charge)

    def test_str_returns_string_representation(self):
        # Act
        expected = (f"Account Number: {self.account_number} "
                    f"Balance: ${self.balance:.2f}\n"
                    f"Minimum Balance: ${self.minimum_balance:.2f}\n"
                    f"Account Type: Savings")
        
        # Assert
        self.assertEqual(str(self.account), expected)

if __name__ == '__main__':
    unittest.main()
