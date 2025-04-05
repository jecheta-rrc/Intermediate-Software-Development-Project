"""This module defines the Observer class."""

__author__ = "Nkechi Echeta"
__version__ = "1.1.0"
__credits__ = "Nkechi Echeta"

from abc import ABC, abstractmethod

class Observer(ABC):
    """An abstract base class representing an observer in the Observer 
    Pattern.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """Abstract method to handle notifications from the subject.
        
        Args:
            message (str): The notification message received from the 
                subject.
        """
        
        pass
