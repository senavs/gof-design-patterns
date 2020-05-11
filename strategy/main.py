from strategy.client import Duck
from strategy.concrete_strategy import SimpleFlyBehavior, NoFlyBehavior, SimpleQuackBehavior, NoQuackBehavior

if __name__ == '__main__':
    duck1 = Duck(NoQuackBehavior(), SimpleFlyBehavior())
    print(duck1.quack())
    print(duck1.fly())

    duck2 = Duck(SimpleQuackBehavior(), NoFlyBehavior())
    print(duck2.quack())
    print(duck2.fly())
