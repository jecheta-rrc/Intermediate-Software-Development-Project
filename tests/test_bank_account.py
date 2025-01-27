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

    def test_init_sets_attributes(self):
        # Arrange
        account_number = 12345
        client_number = 1010
        balance = 500.50

        # Act
        account = BankAccount(account_number, client_number, balance)

        # Assert
        self.assertEqual(account.account_number, account_number)
        self.assertEqual(account.client_number, client_number)
        self.assertEqual(round(account.balance, 2), round(balance, 2))

    def test_init_balance_set_to_zero_for_invalid(self):
        # Arrange
        account_number = 12345
        client_number = 1010
        invalid_balance = "invalid"

        # Act
        account = BankAccount(account_number, client_number, invalid_balance)

        # Assert
        self.assertEqual(account.balance, 0)

    def test_init_raises_error_for_non_numeric_account_number(self):
        # Arrange
        invalid_account_number = "invalid"
        client_number = 1010
        balance = 500.50

        # Act
        with self.assertRaises(ValueError) as context:
            BankAccount(invalid_account_number, client_number, balance)

        # Assert
        expected_message = "Account number must be an integer."
        self.assertEqual(str(context.exception), expected_message)

    def test_init_raises_error_for_non_numeric_client_number(self):
        # Arrange
        account_number = 12345
        invalid_client_number = "invalid"
        balance = 500.50

        # Act
        with self.assertRaises(ValueError) as context:
            BankAccount(account_number, invalid_client_number, balance)

        # Assert
        expected_message = "Client number must be an integer."
        self.assertEqual(str(context.exception), expected_message)

    def test_account_number_getter(self):
        # Arrange
        account_number = 12345
        client_number = 1010
        balance = 500.50
        account = BankAccount(account_number, client_number, balance)

        # Act
        result = account.account_number

        # Assert
        self.assertEqual(result, account_number)

    def test_client_number_getter(self):
        # Arrange
        account_number = 12345
        client_number = 1010
        balance = 500.50
        account = BankAccount(account_number, client_number, balance)

        # Act
        result = account.client_number

        # Assert
        self.assertEqual(result, client_number)

    def test_balance_getter(self):
        # Arrange
        account_number = 12345
        client_number = 1010
        balance = 500.50
        account = BankAccount(account_number, client_number, balance)

        # Act
        result = account.balance

        # Assert
        self.assertEqual(result, balance)

    def test_update_balance_positive_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        amount = 200.00

        # Act
        account.update_balance(amount)

        # Assert
        self.assertEqual(round(account.balance, 2), 700.00)

    def test_update_balance_negative_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        amount = -200.00

        # Act
        account.update_balance(amount)

        # Assert
        self.assertEqual(round(account.balance, 2), 300.00)

    def test_update_balance_invalid_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        invalid_amount = "invalid"

        # Act
        account.update_balance(invalid_amount)

        # Assert
        self.assertEqual(round(account.balance, 2), 500.00)

    def test_deposit_valid_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        amount = 100.00

        # Act
        account.deposit(amount)

        # Assert
        self.assertEqual(round(account.balance, 2), 600.00)

    def test_deposit_negative_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        invalid_amount = -50.00

        # Act
        with self.assertRaises(ValueError) as context:
            account.deposit(invalid_amount)

        # Assert
        expected_message = "Deposit amount: $-50.00 must be positive."
        self.assertEqual(str(context.exception), expected_message)

    def test_deposit_non_numeric_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        invalid_amount = "invalid"

        # Act
        with self.assertRaises(ValueError) as context:
            account.deposit(invalid_amount)

        # Assert
        expected_message = "Deposit amount: invalid must be numeric."
        self.assertEqual(str(context.exception), expected_message)

    def test_withdraw_valid_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        amount = 200.00

        # Act
        account.withdraw(amount)

        # Assert
        self.assertEqual(round(account.balance, 2), 300.00)

    def test_withdraw_exceeds_balance(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        invalid_amount = 600.00

        # Act
        with self.assertRaises(ValueError) as context:
            account.withdraw(invalid_amount)

        # Assert
        expected_message = "Withdrawal amount: $600.00 must not exceed the account balance: $500.00"
        self.assertEqual(str(context.exception), expected_message)

    def test_withdraw_negative_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        invalid_amount = -50.00

        # Act
        with self.assertRaises(ValueError) as context:
            account.withdraw(invalid_amount)

        # Assert
        expected_message = "Withdrawal amount: $-50.00 must be positive."
        self.assertEqual(str(context.exception), expected_message)

    def test_withdraw_non_numeric_amount(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)
        invalid_amount = "invalid"

        # Act
        with self.assertRaises(ValueError) as context:
            account.withdraw(invalid_amount)

        # Assert
        expected_message = "Withdrawal amount: invalid must be numeric."
        self.assertEqual(str(context.exception), expected_message)

    def test_str_method(self):
        # Arrange
        account = BankAccount(12345, 1010, 500.00)

        # Act
        result = str(account)

        # Assert
        expected = "Account Number: 12345 Balance: $500.00\n"
        self.assertEqual(result, expected)
