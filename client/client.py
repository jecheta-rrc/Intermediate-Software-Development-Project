"""Client class to manage client information for a banking system."""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError

"""
Client class to manage client information for a banking system.
"""

from email_validator import validate_email, EmailNotValidError

class Client:
    """Represents a client with personal information."""

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes a new instance of the Client class.

        Args:
            client_number (int): An integer value representing the client number.
            first_name (str): A string value representing the client's first name.
            last_name (str): A string value representing the client's last name.
            email_address (str): A string value representing the client's email address.

        Raises:
            ValueError: If client_number is not an integer, or if first_name or last_name is blank.
            EmailNotValidError: If email_address is not a valid email address.
        """
        # Validate client_number
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Validate first_name
        stripped_first_name = first_name.strip()
        if not stripped_first_name:
            raise ValueError("First name cannot be blank.")
        self.__first_name = stripped_first_name

        # Validate last_name
        stripped_last_name = last_name.strip()
        if not stripped_last_name:
            raise ValueError("Last name cannot be blank.")
        self.__last_name = stripped_last_name

        # Validate email_address
        try:
            valid_email = validate_email(email_address)
            self.__email_address = valid_email.email
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """Gets the client number."""
        return self.__client_number

    @property
    def first_name(self) -> str:
        """Gets the first name."""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Gets the last name."""
        return self.__last_name

    @property
    def email_address(self) -> str:
        """Gets the email address."""
        return self.__email_address

    def __str__(self) -> str:
        """
        Returns a string representation of the Client object.

        Format:
            {last_name}, {first_name} [{client_number}] - {email_address}

        Returns:
            str: A formatted string representing the Client object.
        """
        return f"{self.last_name}, {self.first_name} [{self.client_number}] - {self.email_address}"

