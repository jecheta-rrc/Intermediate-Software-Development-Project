"""A class representing a chequing account""" 

_author_ = "Nkechi Echeta"
_version_ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """A class representing a chequing account with overdraft protection."""

    def _init_(self, account_number: int, client_number: int, 
                balance: float, date_created: date, 
                overdraft_limit: float, overdraft_rate: float):
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
                to float, or if date_created is not an instance of the date 
                class.
            TypeError: If overdraft_limit or overdraft_rate is not a number.
        """
      
        super()._init_(account_number, client_number, balance, date_created)
    
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.__overdraft_limit = -100.00
    
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.__overdraft_rate = 0.05

        self._strategy = OverdraftStrategy(self._overdraft_limit, 
        self.__overdraft_rate)

    @property
    def overdraft_limit(self) -> float:
        """Returns the overdraft limit.
        
        Returns:
            float: The overdraft limit.
        """
        
        return self.__overdraft_limit

    @property
    def overdraft_rate(self) -> float:
        """Returns the overdraft rate.
        
        Returns:
            float: The overdraft rate.
        """
        
        return self.__overdraft_rate

    def _str_(self) -> str:
        """Returns a string representation of the chequing account.
        
        Returns:
            str: A formatted string with account details.
        """
        
        return (super()._str_() +
                f"\nOverdraft Limit: ${self.__overdraft_limit:.2f} "
                f"\nOverdraft Rate: {self.__overdraft_rate * 100:.2f}% "
                f"\nAccount Type: Chequing")

    def get_service_charge(self) -> float:
        """Returns the service charge using the OverdraftStrategy.
    
        
        Return:
            float: The service charge was applied to the account.
        """
    
        return self.__strategy.calculate_service_charges(self)
        