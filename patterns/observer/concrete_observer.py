from patterns.observer.observ import ABCObserver, ABCObservable
from patterns.observer.concrete_observable import YouTubeChanel


class YouTubeSubscriber(ABCObserver):

    def __init__(self, name, observable: 'ABCObservable'):
        self.name = name
        super().__init__(observable)

    def update(self):
        observable_state = super().update()
        if observable_state:
            print(f'Hey {self.name}, the {self.observable.name} just posted a new video!')
        else:
            print(f'Sorry, {self.name}. The {self.observable.name} not post a new video yet.')
