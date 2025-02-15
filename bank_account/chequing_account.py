"""TODO"""

from bank_account.bank_account import BankAccount
from datetime import date

class ChequingAccount(BankAccount):
    """TODO"""

    def __init__(self, account_number: int, client_number: int, balance: float, 
                date_created: date, overdraft_limit: float, overdraft_rate: float):
        """TODO"""

        super().__init__(account_number, client_number, balance, date_created)

        BASE_SERVICE_CHARGE = 0.50

        try:
            self.__overdraft_limit = float(overdraft_limit)
        except(ValueError, TypeError):
            self.__overdraft_limit = -100.00

        try:
            self.__overdraft_rate = float(overdraft_rate)
        except(ValueError, TypeError):
            self.__overdraft_rate = 0.05


        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    @property
    def overdraft_limit(self) -> float:
        """TODO"""

        return self.__overdraft_limit

    @property
    def overdraft_rate(self) -> float:
        """TODO"""

        return self.__overdraft_rate

    def __str__(self) -> str:
        """TODO"""

        string_representation = (
            super.__str__ + f"\nOverdraft limit: ${self.__overdraft_limit} "
            f"Overdraft rate: {self.__overdraft_rate * 100:.2f}% "
            f"Account Type: Chequing"
        )

        return string_representation

    def get_service_charge() -> float:
        """TODO"""

        if self.balance >= -self.overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + ((self.__overdraft_limit - self.balance)*
                                                self.__overdraft_rate)