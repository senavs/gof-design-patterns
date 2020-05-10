from factory_method.product import GeometricForm


class Triangle(GeometricForm):

    def __init__(self, *sides: float):
        super().__init__(*sides)

        if len(sides) != 3:
            raise AttributeError('triangle has only 3 sides')

        if not self.is_valid():
            raise AttributeError('wrong values for a triangle')

    def is_valid(self, *sides: float):
        if sides:
            return Triangle(*sides).is_valid()
        return not (self._sides[0] >= sum(self._sides[1:]) or
                    self._sides[1] >= self._sides[0] + self._sides[2] or
                    self._sides[2] >= sum(self._sides[:2]))


class Rectangle(GeometricForm):

    def __init__(self, *sides: float):
        super().__init__(*sides)

        if len(sides) != 4:
            raise AttributeError('rectangle has only 3 sides')


class Square(Rectangle):

    def __init__(self, *sides: float):
        super().__init__(*sides)

        if min(sides) != max(sides):
            raise AttributeError('wrong values for a square')
