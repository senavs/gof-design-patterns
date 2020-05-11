from abc import ABC, abstractmethod


class GeometricFactory(ABC):

    @classmethod
    @abstractmethod
    def create_geometric_form(cls, *sides: float): ...
