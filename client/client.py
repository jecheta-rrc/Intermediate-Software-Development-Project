"""Defines the Client class for representing a bank client."""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError


class Client:
    """Represents a client with a client number, first name, last name, and 
    email address.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, 
    email_address: str):
        """Initializes a new instance of the Client class.

        Args:
            client_number (int): The client's unique number.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.

        Raises:
            ValueError: If client_number is not an integer, or if first_name or 
            last_name is blank.
            EmailNotValidError: If the email_address is invalid.
        """

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        first_name = first_name.strip()
        if not first_name:
            raise ValueError("First name cannot be blank.")
        self.__first_name = first_name

        last_name = last_name.strip()
        if not last_name:
            raise ValueError("Last name cannot be blank.")
        self.__last_name = last_name

        try:
            email = validate_email(email_address)
            self.__email_address = email.email
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """Gets the client's unique number.
        Returns:
            int: The client's unique number.
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """Gets the client's first name.
        Returns:
            str: The client's first name.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Gets the client's last name.
        Returns:
            str: The client's last name.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """Gets the client's email address.
        Returns:
            str: The client's email address.
        """
        return self.__email_address

    def __str__(self) -> str:
        """Returns a formatted string representation of the Client object.

        Returns:
            str: A string in the format "{last_name}, {first_name} [{client_number}] - {email_address}".
        """
        return f"{self.last_name}, {self.first_name} [{self.client_number}] - {self.email_address}\n"
