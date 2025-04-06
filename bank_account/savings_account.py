"""This module defines the SavingsAccount class."""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from datetime import date

class SavingsAccount(BankAccount):
    """Represents a savings account with a minimum balance requirement."""

    def __init__(self, account_number: int, client_number: int, balance: float, 
                date_created: date, minimum_balance: float) -> None:
        """Initializes a new instance of the SavingsAccount class.

        Args:
            account_number (int): The unique identifier for the account.
            client_number (int): The unique identifier for the client.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            minimum_balance (float): The required minimum balance for 
                account.
        """
        
        service_charge_strategy = MinimumBalanceStrategy(minimum_balance)

        super().__init__(account_number, client_number, balance, date_created, 
                        service_charge_strategy)

        self.__minimum_balance = minimum_balance

    def get_service_charges(self) -> float:
        """Calculates the service charge based on minimum balance 
        strategy.

        Returns:
            float: The calculated service charge.
        """
        
        return self._service_charge_strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Returns a string representation of the SavingsAccount object.

        Returns:
            str: A formatted string containing account details.
        """
        
        return (f"Account Number: {self.account_number} "
                f"Balance: ${self.balance:.2f}\n"
                f"Minimum Balance: ${self.__minimum_balance:.2f}\n"
                f"Account Type: Savings")
