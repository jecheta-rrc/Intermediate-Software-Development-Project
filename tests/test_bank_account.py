"""Unit tests for the BankAccount class.

Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """Unit tests for the BankAccount class"""

    def setUp(self):

        # Set up runs before each test method runs
        # Create a valid instance of the BankAccount class
        account_number = 2222
        client_number = 1
        balance = 100.0

        self.bank_account = BankAccount(account_number, client_number, balance)

    def test_init_valid_instance(self):
        # Arrange
        account_number = 2222
        client_number = 1
        balance = 100.0

        # Act
        self.bank_account = BankAccount(account_number, client_number, balance)

        # Assert
        self.assertEqual(2222, self.bank_account.account_number)
        self.assertEqual(1, self.bank_account.client_number)
        self.assertEqual(100.0, self.bank_account.balance)


    def test_init_invalid_account_number(self):
        # Arrange
        account_number = "2222"
        client_number = 1
        balance = 100.0

        # Assert
        with self.assertRaises(ValueError):
            BankAccount(account_number, client_number, balance)

    def test_init_invalid_client_number(self):
        # Arrange
        account_number = 2222
        client_number = "1"
        balance = 100.0

        # Assert
        with self.assertRaises(ValueError):
            BankAccount(account_number, client_number, balance)

    def test_init_invalid_balance(self):
        # Arrange
        account_number = 2222
        client_number = 1
        balance = "invalid_balance"

        # Assert
        with self.assertRaises(ValueError):
            BankAccount(account_number, client_number, balance)

    def test_deposit_valid_amount(self):
        # Act
        self.bank_account.deposit(100.0)

        # Assert
        self.assertEqual(200.0, self.bank_account.balance)

    def test_deposit_invalid_amount(self):
        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit("100.0")

    def test_deposit_negative_amount(self):
        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-100.0)

    def test_withdraw_valid_amount(self):
        # Act
        self.bank_account.withdraw(50.0)

        # Assert
        self.assertEqual(50.0, self.bank_account.balance)

    def test_withdraw_invalid_amount(self):
        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw("50.0")

    def test_withdraw_negative_amount(self):
        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-50.0)

    def test_update_balance_valid_amount(self):
        # Act
        self.bank_account.update_balance(100.0)

        # Assert
        self.assertEqual(200.0, self.bank_account.balance)

    def test_update_balance_invalid_amount(self):
        # Assert
        with self.assertRaises(ValueError):
            self.bank_account.update_balance("100.0")

if __name__ == '__main__':
    unittest.main()
