"""A class representing a chequing account""" 

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy
from datetime import date

class ChequingAccount(BankAccount):
    """Represents a chequing account, which allows overdraft."""

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date,
                 overdraft_limit: float, overdraft_rate: float) -> None:
        """Initializes a new instance of the ChequingAccount class.

        Args:
            account_number (int): The unique identifier for the account.
            client_number (int): The unique identifier for the client.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            overdraft_limit (float): The maximum negative balance 
                allowed.
            overdraft_rate (float): The interest rate charged on 
                overdraft usage.
        """
    
        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)
        
        super().__init__(account_number, client_number, balance, date_created, self.__strategy)

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def get_service_charge(self) -> float:
        """Calculates the service charge based on overdraft strategy.

        Returns:
            float: The calculated service charge.
        """
        
        return self.__strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Returns a string representation of the ChequingAccount object.

        Returns:
            str: A formatted string containing account details.
        """
        
        return (f"Account Number: {self.account_number} "
                f"Balance: ${self.balance:.2f}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:.2f}\n"
                f"Overdraft Rate: {self.__overdraft_rate:.2%}\n"
                f"Account Type: Chequing")
