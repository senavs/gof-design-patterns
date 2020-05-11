from abc import ABC, abstractmethod


class Behavior(ABC):
    """Super class for any behavior"""

    @abstractmethod
    def do(self):
        """Abstract method to execute the behavior"""


class QuackBehavior(Behavior, ABC):
    """Base class to quack behavior"""


class FlyBehavior(Behavior, ABC):
    """Base class to fly behavior"""
