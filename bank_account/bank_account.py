"""BankAccount class implementation."""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"
__credits__ = "ACE Faculty"

from abc import ABC, abstractmethod
from datetime import datetime, date

class BankAccount(ABC):
    """A class to represent a bank account."""

    @abstractmethod
    def __init__(self, account_number: int, client_number: 
                 int, balance: float, date_created: date) -> None:
        """Initializes a new instance of the BankAccount class.
        
        Args:
            account_number (int): an integer value representing the account 
                number.
            client_number (int): an integer value representing the client 
                number.
            balance (float): a float value representing the balance of the 
                account.
            date_created (str): a string value representing the date the 
                account was created.
            
        Raises:
            ValueError: if the account number or client number is 
                not an integer, or if the balance is not a number, or if the 
                date is not an instance of the date class.
        """
        
        self.BASE_SERVICE_CHARGE = 0.50

        if not isinstance(account_number, int):
            raise ValueError("The account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("The client number must be an integer.")
        try:
            balance = float(balance)
        except ValueError as exception:
            raise ValueError("The balance must be a number.") from exception
        if not isinstance(date_created, date):
            date_created = date.today()
        
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance
        self._date_created = date_created

    @property
    def account_number(self) -> int:
        """method to get the account number of the account.
        
        Returns:
            int: the account number of the account.
        """

        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """method to get the client number of the account.
        
        Returns:
            int: the client number of the account.
        """

        return self.__client_number
    
    @property
    def balance(self) -> float:
        """method to get the balance of the account.
        
        Returns:
            float: the balance of the account.      
        """

        return self.__balance
    
    def update_balance(self, amount: float) -> None:
        """method to update the balance of the account.
        
        Args:
            amount (float): the amount to update the balance by
                
        Raises:
            ValueError: if the amount is not numeric or negative.
        """
        
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount < 0:
            raise ValueError(f"Deposit amount: ${amount:.2f} must be positive.")
        
        self.__balance += amount  

    
    def deposit(self, amount: float) -> None:
        """method to deposit money into the account
        
        Args:
            amount (float): the amount to deposit into the account.
            
        Raises:
            ValueError: if the amount is not numeric or negative.
        """
        
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount < 0:
            raise ValueError(f"Deposit amount: ${amount:.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """method to withdraw money from the account.
        
        Args:
            amount (float): the amount to withdraw from the account.
            
            Raises:
                ValueError: if the amount is not numeric, negative, 
                or exceeds the current balance.
        """
        
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")
        
        if amount < 0:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must be positive.")
        
        if amount > self.balance:
            raise ValueError(f"Withdrawal amount: ${amount:.2f} must not exceed" 
            f"the current balance:{self.balance:.2f}.")
        
        self.update_balance(-amount)

    def __str__(self) -> str:
        """"returns a string representation of the BankAccount object.
        
        Returns:
            str: a string representation of the BankAccount object.
        """

        string_representation = (f"Account Number: {self.account_number} "
                                 f"Balance: {self.balance:.2f}")

        return string_representation
    
    @abstractmethod
    def get_service_charge(self) -> float:
        """Method to get the service charge of the account.
        
        Returns:
            float: the service charge of the account.
        """

        pass

 