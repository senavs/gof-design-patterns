from patterns.factory_method.factory import GeometricFactory
from patterns.factory_method.concrete_product import Triangle, Rectangle, Square


class Tangram(GeometricFactory):

    @classmethod
    def create_geometric_form(cls, *sides: float):
        n_sides = len(sides)

        if n_sides < 3:
            raise AttributeError('wrong number of sides for a geometric form')
        elif n_sides == 3:
            return Triangle(*sides)
        elif n_sides == 4:
            if min(sides) == max(sides):
                return Square(*sides)
            else:
                return Rectangle(*sides)
        else:
            raise AttributeError(f'geometric form with {n_sides} number of sides not develop yet.')
