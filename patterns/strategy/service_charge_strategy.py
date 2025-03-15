"""Defines the abstract ServiceChargeStrategy class for service charge 
calculation.
"""

from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """Abstract base class for service charge calculation strategies."""

    BASE_SERVICE_CHARGE = 0.50 

    @abstractmethod
    def calculate_service_charges(self, account) -> float:
        """Abstract method to calculate service charges.

        Args:
            account (BankAccount): The bank account for which 
            the service charge is calculated.

        Returns:
            float: The calculated service charge amount.
        """
        pass
