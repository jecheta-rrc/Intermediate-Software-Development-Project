"""This module defines the Subject class for managing observers in the 
Observer Pattern.
"""

__author__ = "Nkechi Echeta"
__version__ = "1.0.0"
__credits__ = "Nkechi Echeta"

from patterns.observer.observer import Observer
from typing import List

class Subject:
    """A base class for subjects that maintain a list of observers 
    and notify them of state changes."""

    def __init__(self) -> None:
        """Initializes the subject with an empty list of observers."""
        
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Adds an observer to the notification list.
        
        Args:
            observer (Observer): The observer to be added.
        """
        
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Removes an observer from the notification list.
        
        Args:
            observer (Observer): The observer to be removed.
        """
        
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """Notifies all attached observers of an event.
        
        Args:
            message (str): The message to be sent to all observers.
        """
        
        for observer in self._observers:
            observer.update(message)