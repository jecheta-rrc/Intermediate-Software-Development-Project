"""Defines the OverdraftStrategy class for overdraft service charge calculations.
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """Strategy for calculating service charges based on overdraft usage."""

    def __init__(self, overdraft_limit: float, overdraft_rate: float) -> None:
        """Initializes the OverdraftStrategy with overdraft limit and rate.

        Args:
            overdraft_limit (float): The maximum overdraft limit.
            overdraft_rate (float): The interest rate applied on overdraft.
        """
        
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account) -> float:
        """Calculates service charges based on the overdraft amount.

        Args:
            account (BankAccount): The bank account to calculate charges for.

        Returns:
            float: The calculated service charge.
        """
        
        balance = account.get_balance()

        if balance < 0:
            overdraft_amount = min(abs(balance), self._overdraft_limit)
            overdraft_fee = overdraft_amount * self._overdraft_rate
            return self.BASE_SERVICE_CHARGE + overdraft_fee

        return self.BASE_SERVICE_CHARGE

