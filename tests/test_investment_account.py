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
    # Arrange
    self.account_number = 123456
    self.client_number = 654321
    self.balance = 1000.0
    self.management_fee = 50.0

  def test_attributes_set_to_parameter_values(self):
    # Arrange
    ten_years_ago = date.today() - timedelta(days=10 * 365.25)
    account = InvestmentAccount(self.account_number, 
                                self.client_number, self.balance, 
                                ten_years_ago, self.management_fee)
    
    # Assert
    self.assertEqual(account.account_number, self.account_number)
    self.assertEqual(account.client_number, self.client_number)
    self.assertEqual(account.balance, self.balance)
    self.assertEqual(account.management_fee, self.management_fee)

  def test_management_fee_invalid_type(self):
    # Arrange
    ten_years_ago = date.today() - timedelta(days=10 * 365.25)
    
    # Act
    account = InvestmentAccount(self.account_number, self.client_number, 
                                self.balance, ten_years_ago, "invalid_fee")
    
    # Assert
    self.assertEqual(account.management_fee, 2.55)

  def test_date_created_more_than_10_years_ago(self):
    # Arrange
    more_than_ten_years_ago = date.today() - timedelta(days=11 * 365.25)
    
    # Act
    account = InvestmentAccount(self.account_number, self.client_number, 
                                self.balance, more_than_ten_years_ago, 
                                self.management_fee)
    
    # Assert
    self.assertTrue(account._date_created <= account.TEN_YEARS_AGO)

  def test_date_created_within_last_10_years(self):
    # Arrange
    within_last_ten_years = date.today() - timedelta(days=5 * 365.25)
    
    # Act
    account = InvestmentAccount(self.account_number, self.client_number, 
                                self.balance, within_last_ten_years, 
                                self.management_fee)
    
    # Assert
    self.assertTrue(account._date_created > account.TEN_YEARS_AGO)

  def test_displays_waived_management_fee_when_date_created_more_than_10_years_ago(self):
    # Arrange
    more_than_ten_years_ago = date.today() - timedelta(days=11 * 365.25)
    
    # Act
    account = InvestmentAccount(self.account_number, self.client_number, 
                                self.balance, more_than_ten_years_ago, 
                                self.management_fee)
    result = str(account)
    
    # Assert
    self.assertIn("Management Fee: Waived", result)

  def test_displays_management_fee_when_date_created_within_last_10_years(self):
    # Arrange
    within_last_ten_years = date.today() - timedelta(days=5 * 365.25)
    
    # Act
    account = InvestmentAccount(self.account_number, self.client_number, 
                                self.balance, within_last_ten_years, 
                                self.management_fee)
    result = str(account)
    
    # Assert
    self.assertIn(f"Management Fee: ${self.management_fee:.2f}", result)

if __name__ == '__main__':
  unittest.main()


