"""This module defines the TestInvestmentAccount class.

Usage:
  To execute all tests in the terminal execute the following command:
  
  $ python -m unittest tests/test_investment_account.py
"""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):
    """Tests the InvestmentAccount class."""

    def setUp(self):
        """Set up test data before each test."""
        
        self.account_number = 123456
        self.client_number = 654321
        self.balance = 1000.0
        self.management_fee = 50.0
        self.ten_years_ago = date.today() - timedelta(days=10 * 365.25)

    def test_attributes_set_to_parameter_values(self):
        
        account = InvestmentAccount(
            self.account_number, self.client_number, self.balance, 
            self.ten_years_ago, self.management_fee
        )
        
        self.assertEqual(account.account_number, self.account_number)
        self.assertEqual(account.client_number, self.client_number)
        self.assertEqual(account.balance, self.balance)

    def test_date_created_more_than_10_years_ago(self):
        
        more_than_ten_years_ago = date.today() - timedelta(days=11 * 365.25)
        
        account = InvestmentAccount(
            self.account_number, self.client_number, self.balance, 
            more_than_ten_years_ago, self.management_fee
        )
        
        self.assertTrue(account._date_created <= InvestmentAccount.TEN_YEARS_AGO)

    def test_date_created_within_last_10_years(self):
        
        within_last_ten_years = date.today() - timedelta(days=5 * 365.25)
        
        account = InvestmentAccount(
            self.account_number, self.client_number, self.balance, 
            within_last_ten_years, self.management_fee
        )
        
        self.assertTrue(account._date_created > InvestmentAccount.TEN_YEARS_AGO)

    def test_displays_management_fee_when_date_created_more_than_10_years_ago(self):
        
        more_than_ten_years_ago = date.today() - timedelta(days=11 * 365.25)
        
        account = InvestmentAccount(
            self.account_number, self.client_number, self.balance, 
            more_than_ten_years_ago, self.management_fee
        )
        
        result = str(account)
        
        self.assertIn(f"Management Fee: ${self.management_fee:.2f}", result)

    def test_displays_management_fee_when_date_created_within_last_10_years(self):
        
        within_last_ten_years = date.today() - timedelta(days=5 * 365.25)
        
        account = InvestmentAccount(
            self.account_number, self.client_number, self.balance, 
            within_last_ten_years, self.management_fee
        )
        
        result = str(account)
        
        self.assertIn(f"Management Fee: ${self.management_fee:.2f}", result)

if __name__ == '__main__':
    unittest.main()
