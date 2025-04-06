"""This module defines the InvestmentAccount class."""

__author__ = "Nkechi Echeta"
__version__ = "1.1.2025"
__credits__ = "ACE Faculty"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """Represents an investment account with management fees."""

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date,
                 management_fee: float) -> None:
        """Initializes a new instance of the InvestmentAccount class.

        Args:
            account_number (int): The unique identifier for the account.
            client_number (int): The unique identifier for the client.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            management_fee (float): The fee charged for account 
                management.
        """
        
        service_charge_strategy = ManagementFeeStrategy(date_created, management_fee)

        super().__init__(account_number, client_number, balance, date_created, 
                         service_charge_strategy)

        self.__management_fee = management_fee

    def get_service_charges(self) -> float:
        """Calculates the service charge based on management fee 
        strategy.

        Returns:
            float: The calculated service charge.
        """
        
        return self._service_charge_strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Returns a string representation of the InvestmentAccount 
        object.

        Returns:
            str: A formatted string containing account details.
        """
        
        return (f"Account Number: {self.account_number} "
                f"Balance: ${self.balance:.2f}\n"
                f"Management Fee: ${self.__management_fee:.2f}\n"
                f"Account Type: Investment")
                