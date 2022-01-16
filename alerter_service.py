from gpiozero import Buzzer


class AlerterService:
    def __init__(self):
        self.buzzer = Buzzer(15)

    def _alert(self):
        self._sound_alarm()
        # addition of something to display on LCD screen

    def _stop_alert(self):
        self._silence_alarm()
        # addition of something to display on LCD screen

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

    def perform_alerting_given_security_config(self, security_config):
        security_status = security_config['securityStatus']
        if security_status == 'BREACHED':
            print("Security status is breached. Attempting to alert")
            self._alert()
        elif security_status == 'SAFE':
            print("Security status is safe. Attempting to stop alert.")
            self._stop_alert()
        else:
            print(f"Unrecognized security status {security_status}")
