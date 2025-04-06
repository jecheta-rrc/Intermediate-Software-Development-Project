"""This module defines the Client class, which acts as an observer 
for bank account notifications in the Observer Pattern.
"""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"

from patterns.observer.observer import Observer
from datetime import datetime
from utility.file_utils import simulate_send_email

class Client(Observer):
    """Represents a bank client who receives notifications about 
    transactions on their bank account.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, 
    email_address: str):
        """Initializes a client instance.
        
        Args:
            client_number (int): The unique identifier of the client.
            first_name (str): The first name of the client.
            last_name (str): The last name of the client.
            email_address (str): The email address of the client.
        """
        
        self._client_number = client_number
        self._first_name = first_name
        self._last_name = last_name
        self._email_address = email_address

    @property
    def client_number(self) -> int:
        """Gets the client's unique identifier.
        
        Returns:
            int: The unique client number.
        """
        
        return self._client_number

    @property
    def first_name(self) -> str:
        """Gets the client's first name.
        
        Returns:
            str: The client's first name.
        """
        
        return self._first_name

    @property
    def last_name(self) -> str:
        """Gets the client's last name.
        
        Returns:
            str: The client's last name.
        """
        
        return self._last_name

    @property
    def email_address(self) -> str:
        """Gets the client's email address.
        
        Returns:
            str: The client's email address.
        """
        
        return self._email_address

    def update(self, message: str) -> None:
        """Receives notifications from the bank account and simulates 
        sending an email.
        
        Args:
            message (str): The notification message received from the 
                bank account.
        """
        
        subject = f"ALERT: Unusual Activity: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        email_message = (f"Notification for {self.client_number}: {self.first_name} " 
                         f"{self.last_name}: {message}")
        
        # Simulate sending an email
        simulate_send_email(self.email_address, subject, email_message)

    def __str__(self) -> str:
        """Returns a string representation of the client.
        
        Returns:
            str: The string representation of the client.
        """
        
        return f"Client({self.first_name} {self.last_name}, Email: {self.email_address})"
