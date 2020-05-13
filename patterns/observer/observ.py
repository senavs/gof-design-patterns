from abc import ABC, abstractmethod
from typing import Set, Any, MutableSequence, Union


class ABCObservable(ABC):
    _observers: Set['ABCObserver'] = set()

    def add(self, observers: Union['ABCObserver', MutableSequence['ABCObserver']]):
        if isinstance(observers, MutableSequence):
            for observer in observers:
                self.add(observer)
        else:
            self._observers.add(observers)

    def remove(self, observers: Union['ABCObserver', MutableSequence['ABCObserver']]):
        if isinstance(observers, MutableSequence):
            for observer in observers:
                self.remove(observer)
        else:
            self._observers.remove(observers)

    @abstractmethod
    def state(self) -> Any:
        pass

    def notify(self):
        for observer in self._observers:
            observer.update()

    def __repr__(self):
        return f'<{type(self).__qualname__} at {hex(id(self))}>'


class ABCObserver(ABC):
    _observable: 'ABCObservable' = None

    def __init__(self, observable: 'ABCObservable'):
        self._observable = observable

    def update(self):
        if self._observable:
            return self.observable.state()

    @property
    def observable(self) -> 'ABCObservable':
        return self._observable

    def __repr__(self):
        return f'<{type(self).__qualname__} at {hex(id(self))}>'
