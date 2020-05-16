from patterns.state.state import AlertState


class RingAlertState(AlertState):

    def alert(self):
        print('triiiiiinn... triiiiiin')


class VibrateAlertState(AlertState):

    def alert(self):
        print('zuuu... zuuu')


class SilentAlertState(AlertState):

    def alert(self):
        print('...')
