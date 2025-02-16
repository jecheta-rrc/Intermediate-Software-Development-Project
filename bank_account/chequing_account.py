"""A class representimg a chequing account""" 

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "Nkechi Echeta"

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """A class representing a chequing account."""

    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number: int, client_number: int, 
                balance: float, date_created: date, 
                overdraft_limit, overdraft_rate):
        """Initialize a chequing account object.
    
        Args: 
        account_number (int): The account number.
        client_number (int): The client number.
        balance (float): The initial balance of the account.
        date_created (date): The date when the account was created.
        overdraft_limit: The overdraft limit (validated as a float or 
            default to -100).
        overdraft_rate: The overdraft rate (validated as a float or 
            default to 0.05).
        
        Raises:
            ValueError: If overdraft_limit or overdraft_rate cannot be converted 
            to float.
            TypeError: If overdraft_limit or overdraft_rate is not a number.
            ValueError: If date_created is not an instance of the date class.
        """
      
        super().__init__(account_number, client_number, balance, date_created)
    
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.00
    
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

    @property
    def overdraft_limit(self) -> float:
        """Return the overdraft limit."""
        return self.__overdraft_limit

    @property
    def overdraft_rate(self) -> float:
        """Return the overdraft rate."""
        return self.__overdraft_rate

    def __str__(self) -> str:
        """Return a string representation of the chequing account."""
        return (super().__str__() +
                f"\nOverdraft Limit: ${self.__overdraft_limit:.2f} "
                f"\nOverdraft Rate: {self.__overdraft_rate * 100:.2f}% "
                f"\nAccount Type: Chequing")

    def get_service_charge(self) -> float:
        """Return the service charge based on the overdraft limit and rate."""
    
        if self.balance >= -self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + ((self.__overdraft_limit - 
            self.balance) * self.__overdraft_rate)