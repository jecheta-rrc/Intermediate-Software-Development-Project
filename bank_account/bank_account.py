"""BankAccount class implementation."""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

from typing import Union

class BankAccount:
    """Represents a bank account with attributes for account number, client
    number, and balance.
    """
 
    def __init__(self, account_number: int, client_number: int, balance: float = 0.0):
        """Initializes a new BankAccount instance.
 
        Args:
            account_number (int): The account number of the bank account.
            client_number (int): The client number associated with the account holder.
            balance (float): The initial balance of the account.
 
        Raises:
            ValueError: If account_number or client_number is not an integer,
            or if balance cannot be converted to a float.
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
 
        try:
            balance = float(balance)
        except ValueError:
            balance = 0.0
 
        self._account_number = account_number
        self._client_number = client_number
        self._balance = balance
 
    @property
    def account_number(self) -> int:
        """Gets the account number."""
        return self._account_number
 
    @property
    def client_number(self) -> int:
        """Gets the client number."""
        return self._client_number
 
    @property
    def balance(self) -> float:
        """Gets the current balance."""
        return self._balance
 
    def update_balance(self, amount: Union[float, str]) -> None:
        """Updates the account balance by adding the given amount.
 
        Args:
            amount (float): The amount to add (or subtract if negative).
       
        Raises:
            ValueError: If amount cannot be converted to a float.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Update amount must be numeric.")
 
        self._balance += amount
 
    def deposit(self, amount: Union[float, str]) -> None:
        """
        Deposits the given amount into the account.
 
        Args:
            amount (float): The amount to deposit.
 
        Raises:
            ValueError: If the amount is not numeric or is less than or equal to zero.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
 
        if amount <= 0:
            formatted_amount = f"${abs(amount):,.2f}"
            raise ValueError(f"Deposit amount: {formatted_amount} must be positive.")
 
        self.update_balance(amount)
 
    def withdraw(self, amount: Union[float, str]) -> None:
        """
        Withdraws the given amount from the account.
 
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
            raise ValueError(f"Withdrawal amount: {formatted_amount} must be positive.")
 
        if amount > self._balance:
            formatted_amount = f"${amount:,.2f}"
            formatted_balance = f"${self._balance:,.2f}"
            raise ValueError(
                f"Withdrawal amount: {formatted_amount} must not exceed the account balance: {formatted_balance}."
            )
 
        self.update_balance(-amount)
 
    def __str__(self) -> str:
        """
        Returns a string representation of the BankAccount instance.
        Returns:
            str: A formatted string showing the account number and balance.
        """
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
 