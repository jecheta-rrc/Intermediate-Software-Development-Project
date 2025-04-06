"""This module defines the OverdraftStrategy class for service charge 
calculations.
"""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "Nkechi Echeta"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """A service charge strategy that applies overdraft fees."""
        
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """Initializes the OverdraftStrategy instance.
        
        Args:
            overdraft_limit (float): The maximum amount the balance can 
            be overdrawn.
            overdraft_rate (float): The percentage fee applied when 
            overdraft occurs.
        """
        
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
     
    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates service charges based on overdraft conditions.
        
        Args:
            account (BankAccount): The bank account for which the 
            service charge is calculated.

        Returns:
            float: The total calculated service charge.
        """
        
        if account.balance >= self.__overdraft_limit:
            service_charge = self.BASE_SERVICE_CHARGE 
        else:
            service_charge = self.BASE_SERVICE_CHARGE + (
                (self.__overdraft_limit - account.balance) 
                * self.__overdraft_rate
            )
            
        return service_charge
        
