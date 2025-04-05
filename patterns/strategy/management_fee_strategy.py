"""This module defines the ManagementFeeStrategy class for service charge 
calculation.
"""

__author__ = "Nkecxhi Echeta"
__version__ = "1.1.0"
__credits__ = "Nkechi Echeta"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """A service charge strategy that applies a management fee to accounts."""
    
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)
    
    def __init__(self, date_created: date, management_fee: float):
        """Initializes the ManagementFeeStrategy instance.
        
        Args:
            date_created (date): The date the account was created.
            management_fee (float): The fixed management fee applied 
            to accounts less than 10 years old.
        """
        
        self.__date_created = date_created
        self.__management_fee = management_fee 
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charge for an account based on its age.
        
        Args:
            account (BankAccount): The bank account for which the 
            service charge is calculated.
        
        Returns:
            float: The total calculated service charge.
        """
        
        if self.__date_created <= self.TEN_YEARS_AGO:
            fee = self.BASE_SERVICE_CHARGE
        else:
            fee = self.BASE_SERVICE_CHARGE + self.__management_fee
            
        return fee
