from abc import ABC, abstractmethod


class GeometricForm(ABC):
    _sides = []

    @abstractmethod
    def __init__(self, *sides: float):
        if len(sides) < 3:
            raise AttributeError('wrong number of sides for a geometric form')

        self._sides = sides

    def perimeter(self) -> float:
        return sum(self._sides)

    def __repr__(self):
        return f'<{self.__class__.__name__} at {hex(id(self))}>'
