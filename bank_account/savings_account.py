"""This module defines the SavingsAccount class."""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """Represents a savings account, a specialized type of BankAccount."""

    SERVICE_CHARGE_PREMIUM = 2.00 

    def __init__(self, account_number: int, client_number: int, balance: float, 
                date_created, minimum_balance):
        """Initializes a new instance of the SavingsAccount class.

        Args:
            account_number (int): The account number.
            client_number (int): The client number.
            balance (float): The initial balance of the account.
            date_created (date): The date when the account was created.
            minimum_balance: The minimum balance (validated as a float or 
                default to 50.00).
        
        Raises:
            ValueError: if the account number or client number is not an integer,
                or if the balance is not a number, or if the date is not an 
                instance of the date class.
        """
    
        super().__init__(account_number, client_number, balance, date_created)
    
        try:
            self.__minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.__minimum_balance = 50.00

    @property
    def minimum_balance(self) -> float:
        """Returns the minimum balance.
    
        Returns:
            float: The minimum balance of the savings account.
        """
    
        return self.__minimum_balance

    def __str__(self) -> str:
        """Returns a string representation of the savings account.
    
        Returns:
            str: The string representation of the savings account.
        """
    
        base_str = super().__str__()
    
        return (base_str +
                f"\nMinimum Balance: ${self.__minimum_balance:.2f} " +
                "Account Type: Savings")

    def get_service_charge(self) -> float:
        """Returns the service charge based on balance and minimum balance.
    
        Returns:
            float: The calculated service charge for the account.
        """
    
        if self.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
