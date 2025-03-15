"""Defines the ManagementFeeStrategy class for investment account charges."""

from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """Strategy for applying management fees to long-term investment accounts.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float) -> None:
        """Initializes the ManagementFeeStrategy with account creation date and 
        management fee.

        Args:
            date_created (date): The date the account was created.
            management_fee (float): The fee applied for long-term accounts.
        """
        
        self._date_created = date_created
        self._management_fee = management_fee

    def calculate_service_charges(self, account) -> float:
        """Calculates service charges based on account creation date.

        Args:
            account (BankAccount): The bank account to calculate charges for.

        Returns:
            float: The calculated service charge.
        """
        
        if self._date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE + self._management_fee

        return self.BASE_SERVICE_CHARGE
        
