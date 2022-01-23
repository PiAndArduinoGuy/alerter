from gpiozero import Buzzer

from service.alerter import Alerter


class SecurityStatusAlerterService(Alerter):
    def __init__(self):
        super().__init__()
        self.buzzer = Buzzer(15)

    def alert_given(self, condition):
        if condition == 'BREACHED':
            print("Security status is breached. Attempting to alert")
            self.alert()
        elif condition == 'SAFE':
            print("Security status is safe. Attempting to stop alert.")
            self.stop_alert()
        else:
            print(f"Unrecognized security status {condition}")

    def alert(self):
        self._sound_alarm()

    def stop_alert(self):
        self._silence_alarm()

    def _sound_alarm(self):
        if not self.buzzer.is_active:
            print("Buzzer will be turned on.")
            self.buzzer.on()
        else:
            print("Buzzer is currently active, will not attempt to turn it on.")

    def _silence_alarm(self):
        if self.buzzer.is_active:
            print("Buzzer will be turned off")
            self.buzzer.off()
        else:
            print("Buzzer is not currently active, will not attempt to turn it off.")
