"""Client class to manage client information for a banking system."""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

from email_validator import validate_email, EmailNotValidError

class Client:
    """Represents a bank client with details like client number, first name, 
    last name, and email address.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, 
    email_address: str):
        """Initializes a new instance of the Client class with validation for 
        attributes.
        
        Args:
            client_number (int): A unique identifier for the client.
            first_name (str): The first name of the client.
            last_name (str): The last name of the client.
            email_address (str): The email address of the client.

        Raises:
            ValueError: If client_number is not an integer, or if first_name, or 
            last_name is blank after stripping whitespace.
        """

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self._client_number = client_number

        stripped_first_name = first_name.strip()
        if not stripped_first_name:
            raise ValueError("First name cannot be blank.")
        self._first_name = stripped_first_name

        stripped_last_name = last_name.strip()
        if not stripped_last_name:
            raise ValueError("Last name cannot be blank.")
        self._last_name = stripped_last_name

        try:
            valid_email = validate_email(email_address)
            self._email_address = valid_email.email
        except EmailNotValidError:
            self._email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """Returns the client number.
        
        Returns:
            int: The client number.
        """

        return self._client_number

    @property
    def first_name(self) -> str:
        """Returns the first name.
        
        Returns:
            str: The first name.
        """

        return self._first_name

    @property
    def last_name(self) -> str:
        """Returns the last name.
        
        Returns:
            str: The last name.
        """

        return self._last_name

    @property
    def email_address(self) -> str:
        """Returns the email address.
        
        Returns:
            str: The email address.
        """

        return self._email_address

    def __str__(self) -> str:
        """Returns a string representation of the Client.
        
        Returns:
            str: A formatted string containing the client's last name, first 
                name, client address, and email address.
        """
        
        return (
            f"{self.last_name}, {self.first_name} "
            f"[{self.client_number}] - {self.email_address}"
        )
   
