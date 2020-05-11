from patterns.strategy.strategy import QuackBehavior, FlyBehavior


class SimpleQuackBehavior(QuackBehavior):

    def do(self):
        return 'simple quack!'


class NoQuackBehavior(QuackBehavior):

    def do(self):
        return '-'


class SimpleFlyBehavior(FlyBehavior):

    def do(self):
        return 'flying'


class NoFlyBehavior(FlyBehavior):

    def do(self):
        return 'i can\'t fly!'
