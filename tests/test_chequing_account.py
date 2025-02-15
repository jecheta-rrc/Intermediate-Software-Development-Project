"""TODO"""

import unittest
from datetime import date
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount

class TestChequingAccount(unittest, TestCase):
    """TODO"""


    def setUP(self) -> None:
        """TODO"""

        self.account_number = 9876
        self.client_number = 56789
        self.balance = 1000.00
        self.date_created = date(2021, 3, 15)
        self.overdraft_limit = 500
        self.overdraft_rate = 0.10

    #Arrange
    self.chequing_account = ChequingAccount(self.account_number, 
                                            self.client_number, 
                                            self.balance,
                                            self.date_created, 
                                            self.overdraft_limit, 
                                            self.overdraft_rate)

    def test_init_initialize_correct_state(self):
        """TODO"""

        #Assert
        self.assertEqual(self.account_number, self.chequing_account._ChequingAccount__account_number)
        self.assertEqual(self.client_number, self.chequing_account._ChequingAccount__client_number)
        self.assertEqual(self.balance, self.chequing_account._ChequingAccount__balance)
        self.assertEqual(self.date_created, self.chequing_account.date_created)
        self.assertEqual(self.overdraft_limit, self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(self.overdraft_rate, self.chequing_account._ChequingAccount__overdraft_rate)

    def test_init_overdraft_limit_is_invalid_type(self):
        """TODO"""

        #arrange
        ChequingAccount = ChequingAccount(self.account_number, 
                                          self.client_number, 
                                          self.balance, self.date_created, 
                                          "4567", 
                                          self.overdraft_rate)

        self.assertEqual(chequing_account.overdraft_limit, -100)

    def test_init_overdraft_rate_is_invalid_type(self):
        """TODO"""

        #Act
        ChequingAccount = ChequingAccount(self.account_number, 
                                          self.client_number, 
                                          self.balance, self.date_created, 
                                          self.overdraft_limit, 
                                          "something else")

        #Assert
        self.assertEqual(chequing_account.overdraft_rate, 0.05)


    def test_get_service_charge_the_balance_is_above_the_overdraft_limit(self):
        """TODO"""

        #ARR
        self.chequing_account._BankAccount__balance = 200

        # Assert
        self.assertEqual(self.chequing_account.get_service_charge(), 
                         ChequingAccount.BASE_SERVICE_CHARGE)

    