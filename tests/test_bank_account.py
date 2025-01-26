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
    """
    Unit tests for the BankAccount class.
    """

    def test_update_balance_valid_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        update_amount = 50.0
        expected_balance = 150.0
        account = BankAccount(account_number, client_number, initial_balance)

        # Act
        account.update_balance(update_amount)

        # Assert
        self.assertEqual(account.balance, expected_balance)

    def test_update_balance_invalid_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        invalid_amount = "invalid"
        account = BankAccount(account_number, client_number, initial_balance)

        # Act
        with self.assertRaises(ValueError) as context:
            account.update_balance(invalid_amount)

        # Assert
        self.assertEqual(str(context.exception), "Update amount must be numeric.")

    def test_deposit_valid_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        deposit_amount = 50.0
        expected_balance = 150.0
        account = BankAccount(account_number, client_number, initial_balance)

        # Act
        account.deposit(deposit_amount)

        # Assert
        self.assertEqual(account.balance, expected_balance)

    def test_deposit_invalid_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        invalid_amount = "invalid"
        account = BankAccount(account_number, client_number, initial_balance)

        # Act
        with self.assertRaises(ValueError) as context:
            account.deposit(invalid_amount)

        # Assert
        self.assertEqual(str(context.exception), "Deposit amount: invalid must be numeric.")

    def test_deposit_negative_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        negative_amount = -50.0
        account = BankAccount(account_number, client_number, initial_balance)

        # Act
        with self.assertRaises(ValueError) as context:
            account.deposit(negative_amount)

        # Assert
        self.assertIn("must be positive", str(context.exception))

    def test_withdraw_valid_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        withdraw_amount = 50.0
        expected_balance = 50.0
        account = BankAccount(account_number, client_number, initial_balance)

        # Act
        account.withdraw(withdraw_amount)

        # Assert
        self.assertEqual(account.balance, expected_balance)

    def test_withdraw_exceeding_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        exceeding_amount = 150.0
        account = BankAccount(account_number, client_number, initial_balance)

        # Act
        with self.assertRaises(ValueError) as context:
            account.withdraw(exceeding_amount)

        # Assert
        self.assertIn("must not exceed the account balance", str(context.exception))

    def test_withdraw_invalid_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        invalid_amount = "invalid"
        account = BankAccount(account_number, client_number, initial_balance)

        # Act
        with self.assertRaises(ValueError) as context:
            account.withdraw(invalid_amount)

        # Assert
        self.assertEqual(str(context.exception), "Withdraw amount: invalid must be numeric.")

    def test_withdraw_negative_amount(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        initial_balance = 100.0
        negative_amount = -50.0
        account = BankAccount(account_number, client_number, initial_balance)

        # Act 
        with self.assertRaises(ValueError) as context:
            account.withdraw(negative_amount)

        # Assert
        self.assertIn("must be positive", str(context.exception))

    def test_str_method(self):
        # Arrange
        account_number = 20019
        client_number = 1010
        balance = 6764.67
        account = BankAccount(account_number, client_number, balance)
        expected_str = "Account Number: 20019 Balance: $6,764.67"

        # Act
        result = str(account)

        # Assert
        self.assertEqual(result, expected_str)


if __name__ == "__main__":
    unittest.main()
