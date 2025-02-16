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

class TestSavingsAccount(unittest.TestCase):
    """Tests the SavingsAccount class."""

    def setUp(self):
        self.account_number = 123456
        self.client_number = 654321
        self.balance = 500.0
        self.minimum_balance = 50.0
        self.date_created = date(2025, 2, 13)

    def test_init_initialize_state(self):
    
        account = SavingsAccount(self.account_number, 
                                self.client_number, 
                                self.balance, 
                                self.date_created, 
                                self.minimum_balance)

        self.assertEqual(account._BankAccount__account_number, self.account_number)
        self.assertEqual(account._BankAccount__client_number, self.client_number)
        self.assertEqual(account._BankAccount__balance, self.balance)
        self.assertEqual(account._SavingsAccount__minimum_balance, self.minimum_balance)
  
    def test_init_minimum_balance_invalid_type(self):
        # Arrange
        account = SavingsAccount(self.account_number, 
                                self.client_number, 
                                self.balance, 
                                self.date_created, "invalid")
       
        # Assert
        self.assertEqual(account.minimum_balance, 50.00)

    def test_get_service_charge_balance_greater_than_minimum(self):
        # Arrange
        account = SavingsAccount(self.account_number, 
                                self.client_number, 
                                self.balance, 
                                self.date_created, 
                                self.minimum_balance)
    
        # Assert
        self.assertEqual(account.get_service_charge(), account.BASE_SERVICE_CHARGE)
  
    def test_get_service_charge_balance_equal_to_minimum(self):
        # Arrange
        account = SavingsAccount(self.account_number, 
                                self.client_number, 
                                self.minimum_balance, 
                                self.date_created, 
                                self.minimum_balance)
    
        # Assert
        self.assertEqual(account.get_service_charge(), account.BASE_SERVICE_CHARGE)

    def test_get_service_charge_balance_less_than_minimum(self):
        # Arrange
        account = SavingsAccount(self.account_number, 
                                self.client_number, 
                                self.minimum_balance - 1, 
                                self.date_created, 
                                self.minimum_balance)
    
        # Act
        expected_charge = account.BASE_SERVICE_CHARGE * account.SERVICE_CHARGE_PREMIUM
    
        # Assert
        self.assertEqual(account.get_service_charge(), expected_charge)
  
    def test_str_returns_string_representation(self):
        # Arrange
        account = SavingsAccount(self.account_number, 
                                self.client_number, 
                                self.balance, 
                                self.date_created, 
                                self.minimum_balance)
    
        # Act
        expected = (f"Account Number: {self.account_number} Balance: ${self.balance:.2f}\n"
                    f"Minimum Balance: ${self.minimum_balance:.2f} Account Type: Savings")
    
        # Assert
        self.assertEqual(str(account), expected)
      
if __name__ == '__main__':
  unittest.main()
