from abc import ABC

from patterns.strategy.strategy import Behavior


class Duck(ABC):
    __quack: Behavior = None
    __fly: Behavior = None

    def __init__(self, quack_behavior: Behavior, fly_behavior: Behavior):
        self.__quack = quack_behavior
        self.__fly = fly_behavior

    def quack(self):
        return self.__quack.do()

    def fly(self):
        return self.__fly.do()

    def __str__(self):
        return f'<Duck at {hex(id(self))}>'
