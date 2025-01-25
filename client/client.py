__author__ = "Nkechi Echeta"
__version__ = "1.0.0"

class Client:
    """Represents a banking client."""

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes a new Client instance.

        Args:
            client_number (int): An integer value representing the client number.
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            email_address (str): The client's email address.
        """
        self.__client_number = client_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
