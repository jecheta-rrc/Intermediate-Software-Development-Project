"""This module defines the MinimumBalanceStrategy class."""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """Represents a service charge strategy based on maintaining a minimum 
    balance.
    """
    
    SERVICE_CHARGE_PREMIUM = 2.0
    
    def __init__(self, minimum_balance: float):
        """Initializes a new instance of the MinimumBalanceStrategy class.
        
        Args:
            minimum_balance (float): The minimum balance required to 
            avoid extra service charges.
        """
        
        self.__minimum_balance = minimum_balance
    
    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates service charges based on the account's balance and the 
        minimum balance requirement.
        
        Args:
            account (BankAccount): The bank account for which service 
            charges are calculated.
        
        Returns:
            float: The calculated service charge.
        """
        
        if account.balance >= self.__minimum_balance:
            return super().BASE_SERVICE_CHARGE
        else:
            return super().BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
