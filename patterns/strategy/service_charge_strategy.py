"""This module defines the ServiceChargeStrategy class."""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Avoid circular import issue by using TYPE_CHECKING
if TYPE_CHECKING:
    from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """A base class for implementing different service charge 
    strategies."""
    
    BASE_SERVICE_CHARGE = 0.50  
    
    @abstractmethod
    def calculate_service_charges(self, account: "BankAccount") -> float:
        """Abstract method to calculate service charges for a given 
        account.
        
        Args:
            account (BankAccount): The bank account for which service 
                charges need to be computed.
        
        Returns:
            float: The computed service charge for the given account.
        """
        
        pass
    
