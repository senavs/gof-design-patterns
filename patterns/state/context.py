from patterns.state.state import AlertState
from patterns.state.concrete_sate import RingAlertState


class Phone:
    _state = RingAlertState()

    def __init__(self, number: str):
        self.number = str(number)

    def call(self, other: 'Phone'):
        print(f'receiving call from {other.number}')
        other.alert()

    def alert(self):
        self._state.alert()

    def change_state(self, state: 'AlertState'):
        self._state = state
