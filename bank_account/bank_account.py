"""BankAccount class implementation."""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from datetime import datetime, date

class BankAccount(ABC):
    """Represents a bank account with attributes for account number, client
    number, and balance.
    """
 
    @abstractmethod
    def __init__(self, account_number: int, client_number: int, 
                 balance: float, 
                 date_created: date) -> None:
        """Initializes a new BankAccount instance.
 
        Args:
            account_number (int): The account number of the bank account.
            client_number (int): The client number associated with the account 
                holder.
            balance (float): The initial balance of the account.
            date_created (str): This represents the date the account was created. 
 
        Raises:
            ValueError: If account_number or client_number is not an integer,
            or if balance cannot be converted to a float.
        """
        if not isinstance(account_number, int):
            raise ValueError("The account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("The client number must be an integer.")
        try:
            balance = float(balance)
        except ValueError:
            raise ValueError ("The balance must be a number")

        if not isinstance(date_created, date):
            date_created = date.today()

        self.BASE_SERVICE_CHARGE = 0.50
 
        self._date_created = date_created
        self._account_number = account_number
        self._client_number = client_number
        self._balance = balance
 
    @property
    def account_number(self) -> int:
        """Gets the account number.
        
        Returns: 
            int: Returns the account number
        """

        return self._account_number
 
    @property
    def client_number(self) -> int:
        """Gets the client number.
        
        Returns: 
            int: the client number
        """
        
        return self._client_number
 
    @property
    def balance(self) -> float:
        """Gets the current balance.
        
        Returns:
            float: The balance of the account. 
        """

        return self._balance
 
    def update_balance(self, amount: float) -> None:
        """Updates the account balance by adding the given amount.
 
        Args:
            amount (float): The amount to add (or subtract if negative.)
       
        Raises:
            ValueError: If amount cannot be converted to a float.
        """
        
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount < 0:
            raise ValueError(f"Deposit amount: ${amount: .2f} must be positive.")

        self._balance += amount
 
    def deposit(self, amount: float) -> None:
        """Deposits the given amount into the account.
 
        Args:
            amount (float): The amount to deposit.
 
        Raises:
            ValueError: If the amount is not numeric or is less than or equal to
            zero.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
 
        if amount <= 0:
            formatted_amount = f"${abs(amount):,.2f}"
            raise ValueError(f"Deposit amount: {formatted_amount} must be positive.")
 
        self.update_balance(amount)
 
    def withdraw(self, amount: float) -> None:
        """Withdraws the given amount from the account.
 
        Args:
            amount (float): The amount to withdraw.
 
        Raises:
            ValueError: If the amount is not numeric, less than or equal to zero,
            or exceeds the current balance.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")
 
        if amount <= 0:
            formatted_amount = f"${abs(amount):,.2f}"
            raise ValueError(f"Withdrawal amount: {formatted_amount} "
                             f"must be positive.")
 
        if amount > self._balance:
            formatted_amount = f"${amount:,.2f}"
            formatted_balance = f"${self._balance:,.2f}"
            raise ValueError(
                f"Withdrawal amount: {formatted_amount}"
                f"must not exceed the account balance: {formatted_balance}."
            )
 
        self.update_balance(-amount)
 
    def __str__(self) -> str:
        """Returns a string representation of the BankAccount instance.
        
        Returns:
            str: A formatted string showing the account number and balance.
        """

        return (f"Account Number: {self._account_number} "
                f"Balance: ${self._balance:,.2f}\n")

    @abstractmethod
    def get_service_charge() -> float:
        """Method that will get the service charge on the bank account
        
        Returns:
            float: The service charge on the account. 
        """

        pass
 