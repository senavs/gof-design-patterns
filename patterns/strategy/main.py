from patterns.strategy.client import Duck
from patterns.strategy.concrete_strategy import SimpleFlyBehavior, NoFlyBehavior, SimpleQuackBehavior, NoQuackBehavior

if __name__ == '__main__':
    duck1 = Duck(NoQuackBehavior(), SimpleFlyBehavior())
    print(duck1, duck1.quack())
    print(duck1, duck1.fly())

    duck2 = Duck(SimpleQuackBehavior(), NoFlyBehavior())
    print(duck2, duck2.quack())
    print(duck2, duck2.fly())
