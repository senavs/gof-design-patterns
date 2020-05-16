from patterns.state.concrete_sate import RingAlertState, VibrateAlertState, SilentAlertState
from patterns.state.context import Phone

if __name__ == '__main__':
    phone1 = Phone('(61) 9 9999-9999')
    phone2 = Phone('(61) 9 8888-8888')

    print('\n--> RingAlertState (default)')
    phone1.call(phone2)

    print('\n--> VibrateAlertState')
    phone2.change_state(VibrateAlertState())
    phone1.call(phone2)

    print('\n--> SilentAlertState')
    phone2.change_state(SilentAlertState())
    phone1.call(phone2)
