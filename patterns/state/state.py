from abc import ABC, abstractmethod


class AlertState(ABC):

    @abstractmethod
    def alert(self):
        """abstract method for phone alert"""
