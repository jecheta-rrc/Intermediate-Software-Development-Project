"""Tests for the ChequingAccount class."""

_author_ = "Nkechi Echeta"
_version_ = "1.1.0"
_credits_ = "ACE Faculty"

import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest.TestCase):
    """Tests the ChequingAccount class."""

    def setUp(self) -> None:
        """Arrange: Set up a ChequingAccount instance for testing."""
        self.account_number = 123456
        self.client_number = 98765
        self.initial_balance = 500.00
        self.date_created = date(2025, 2, 13)
        self.overdraft_limit = 100.00
        self.overdraft_rate = 0.05

        self.account = ChequingAccount(
            self.account_number, self.client_number, self.initial_balance,
            self.date_created, self.overdraft_limit, self.overdraft_rate
        )

    def test_init_initialize_state(self):
        """Assert: Ensure attributes are correctly assigned."""
        self.assertEqual(self.account.account_number, self.account_number)
        self.assertEqual(self.account.client_number, self.client_number)
        self.assertEqual(self.account.balance, self.initial_balance)
        self.assertEqual(self.account.overdraft_limit, self.overdraft_limit)
        self.assertEqual(self.account.overdraft_rate, self.overdraft_rate)

    def test_init_date_created_invalid_type(self):
        """Assert: If date_created is invalid, should default to today."""
        account = ChequingAccount(
            self.account_number, self.client_number, self.initial_balance, "invalid",
            self.overdraft_limit, self.overdraft_rate
        )
        self.assertEqual(account.date_created, date.today())

    def test_get_service_charge_balance_above_overdraft_limit(self):
        """Assert: If balance is above overdraft limit, return base service charge."""
        account = ChequingAccount(self.account_number, self.client_number, 50.00,
                                  self.date_created, self.overdraft_limit, self.overdraft_rate)
        self.assertEqual(account.get_service_charge(), account.BASE_SERVICE_CHARGE)

    def test_get_service_charge_balance_below_overdraft_limit(self):
        """Assert: If balance is below overdraft limit, apply overdraft penalty."""
        account = ChequingAccount(self.account_number, self.client_number, -150.00,
                                  self.date_created, self.overdraft_limit, self.overdraft_rate)
        expected_charge = (
            account.BASE_SERVICE_CHARGE +
            ((account.overdraft_limit - account.balance) * account.overdraft_rate)
        )
        self.assertEqual(account.get_service_charge(), expected_charge)

    def test_get_service_charge_balance_at_overdraft_limit(self):
        """Assert: If balance is exactly at overdraft limit, apply standard charge."""
        account = ChequingAccount(self.account_number, self.client_number, -self.overdraft_limit,
                                  self.date_created, self.overdraft_limit, self.overdraft_rate)
        expected_charge = (
            account.BASE_SERVICE_CHARGE +
            ((account.overdraft_limit - account.balance) * account.overdraft_rate)
        )
        self.assertEqual(account.get_service_charge(), expected_charge)

    def test_get_service_charge_balance_at_zero(self):
        """Assert: If balance is zero, return base service charge."""
        account = ChequingAccount(self.account_number, self.client_number, 0.00,
                                  self.date_created, self.overdraft_limit, self.overdraft_rate)
        self.assertEqual(account.get_service_charge(), account.BASE_SERVICE_CHARGE)

    def test_get_service_charge_invalid_balance_type(self):
        """Assert: If balance is an invalid type, should raise ValueError."""
        with self.assertRaises(ValueError):
            account = ChequingAccount(self.account_number, self.client_number, "invalid",
                                      self.date_created, self.overdraft_limit, self.overdraft_rate)
            account.get_service_charge()

    def test_str_representation(self):
        """Assert: String representation contains correct details."""
        expected_str = (
            f"Account Number: {self.account_number} "
            f"\nBalance: {self.initial_balance:.2f} "
            f"\nOverdraft Limit: {self.overdraft_limit:.2f} "
            f"\nOverdraft Rate: {self.overdraft_rate * 100:.2f}% "
            "\nAccount Type: Chequing"
        )
        self.assertEqual(str(self.account), expected_str)

if _name_ == "_main_":
    unittest.main()
