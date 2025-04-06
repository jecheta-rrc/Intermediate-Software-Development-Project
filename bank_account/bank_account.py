"""This module defines the BankAccount class, which extends Subject 
to notify observers of account changes in the Observer Pattern.
"""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "ACE Faculty"

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING
from patterns.observer.subject import Subject

# Avoid circular import issue by using TYPE_CHECKING
if TYPE_CHECKING:
    from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
else:
    from patterns.strategy.service_charge_strategy import ServiceChargeStrategy  

class BankAccount(Subject, ABC):
    """Represents a bank account that supports deposits, withdrawals, 
    service charges, and observer notifications.
    """

    LARGE_TRANSACTION_THRESHOLD: float = 9999.99
    LOW_BALANCE_LEVEL: float = 50.0

    def __init__(self, account_number: int, client_number: int, balance: float, 
                 date_created: date, service_charge_strategy: "ServiceChargeStrategy"):
        """Initializes a bank account instance.

        Args:
            account_number (int): The unique identifier of the bank 
                account.
            client_number (int): The unique identifier of the account 
                holder.
            balance (float): The initial balance of the bank account.
            date_created (date): The date when the bank account was 
                created.
            service_charge_strategy (ServiceChargeStrategy): The 
                strategy used for calculating service charges.

        Raises:
            ValueError: If `account_number` or `client_number` is not 
                an integer.
            ValueError: If `balance` is not numeric.
            ValueError: If `date_created` is not an instance of `date`.
            ValueError: If `service_charge_strategy` is not a valid 
                `ServiceChargeStrategy` instance.
        """
        
        super().__init__()

        if not isinstance(account_number, int):
            raise ValueError("The account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("The client number must be an integer.")
        if not isinstance(balance, (int, float)):
            raise ValueError("The balance must be a numeric value.")
        if not isinstance(date_created, date):
            date_created = date.today()
        if not isinstance(service_charge_strategy, ServiceChargeStrategy):
            raise ValueError("Invalid service charge strategy.")

        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance
        self._date_created = date_created
        self._service_charge_strategy = service_charge_strategy

    @property
    def account_number(self) -> int:
        """Gets the account number.
        
        Returns:
            int: The unique identifier of the bank account.
        """
        
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Gets the client number.
        
        Returns:
            int: The unique identifier of the account holder.
        """
        
        return self.__client_number

    @property
    def balance(self) -> float:
        """Gets the current balance of the bank account.
        
        Returns:
            float: The available balance in the account.
        """
        
        return self.__balance
    
    @property
    def date_created(self) -> date:
        """Gets the date the account was created.

        Returns:
            date: The creation date of the account.
        """
        
        return self._date_created


    def update_balance(self, amount: float) -> None:
        """Updates the account balance by a specified amount.

        Args:
            amount (float): The amount to add (deposit) or subtract 
                (withdraw).

        Raises:
            ValueError: If `amount` is not numeric.
        """
        
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be numeric.")
        
        self.__balance += amount

        # Notify if balance falls below threshold
        if self.__balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.balance:.2f}: on account "
                        f"{self.account_number}.")

        # Notify if a large transaction occurs
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${amount:.2f}: on account {self.account_number}.")

    def deposit(self, amount: float) -> None:
        """Deposits money into the bank account.

        Args:
            amount (float): The amount to be added to the account.

        Raises:
            ValueError: If `amount` is negative or not numeric.
        """
        
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Deposit amount must be a positive numeric value.")
        
        self.update_balance(amount)
        self.notify(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraws money from the bank account.

        Args:
            amount (float): The amount to be withdrawn from the account.

        Raises:
            ValueError: If `amount` is negative or not numeric.
            Warning: If withdrawal is skipped due to insufficient funds.
        """

        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Withdrawal amount must be a positive numeric value.")
        
        # Check if funds are sufficient before attempting withdrawal
        if amount > self.balance:
            print(f"Warning: Insufficient funds. Cannot withdraw "
                  f"${amount:.2f}. Skipping withdrawal.")
            
            return  

        self.update_balance(-amount)
        self.notify(f"Withdrawn ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_service_charge(self) -> float:
        """Calculates and retrieves the service charge for the account.

        Returns:
            float: The computed service charge based on the assigned 
            strategy.
        """
        
        return self._service_charge_strategy.calculate_service_charges(self)

    def __str__(self) -> str:
        """Returns the string representation of the BankAccount object.

        Returns:
            str: A formatted string displaying the account number and 
                current balance.
        """
        
        return (f"Account Number: {self.account_number} "
                f"Balance: ${self.balance:.2f}")