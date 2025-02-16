"""This module defines the InvestmentAccount class."""

__author__ = "Nkechi Echeta"
__version__ = "1.1.2025"
__credits__ = "ACE Faculty"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class InvestmentAccount(BankAccount):
    """Represents an investment account, a specialized type of BankAccount."""

    TEN_YEARS_AGO = date.today() - timedelta(days=365.25 * 10)
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float, 
                date_created: date, management_fee):
        """Initializes a new instance of the InvestmentAccount class.

        Args:
        account_number (int): The account number.
        client_number (int): The client number.
        balance (float): The initial balance of the account.
        date_created (date): The date when the account was created.
        management_fee: The management fee (validated as a float or default to 2.55).
        
        Raises:
            ValueError: If the account number or client number is not an integer.
            ValueError: If the balance is not a number.
            ValueError: If the date is not an instance of the date class.
        """
        super().__init__(account_number, client_number, balance, date_created)
    
        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55  # Default value if invalid

    @property
    def management_fee(self) -> float:
        """Return the management fee."""
        return self.__management_fee

    def __str__(self) -> str:
        """Return a string representation of the investment account.
    
        Returns:
            str: A summary of account details including the management fee and account type.
        """
    
        base_str = super().__str__()
    
        if self._date_created > self.TEN_YEARS_AGO:
            return (base_str +
                f"\nManagement Fee: ${self.__management_fee:.2f}" +
                "\nAccount Type: Investment")
        else:
            return base_str + "\nManagement Fee: Waived\nAccount Type: Investment"

    def get_service_charge(self) -> float:
        """Return the service charge based on account age.
      
        Returns:
        float: The calculated service charge.
        """
      
        if self._date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
        
