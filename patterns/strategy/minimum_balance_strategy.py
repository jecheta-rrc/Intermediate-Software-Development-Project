"""Defines the MinimumBalanceStrategy class for savings account charges."""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """Strategy for applying extra service charges if balance is too low."""

    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float) -> None:
        """Initializes the MinimumBalanceStrategy with a minimum balance 
        threshold.

        Args:
            minimum_balance (float): The minimum required balance to avoid 
                                     extra service charges.
        """
        
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account) -> float:
        """Calculates service charges based on the account balance.

        Args:
            account (BankAccount): The bank account to calculate charges for.

        Returns:
            float: The calculated service charge.
        """
        
        if account.get_balance() < self._minimum_balance:
            return self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM

        return self.BASE_SERVICE_CHARGE
