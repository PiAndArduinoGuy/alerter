from gpiozero import Buzzer

from service.alerter import Alerter
import logging

class SecurityStatusAlerterService(Alerter):
    def __init__(self):
        super().__init__()
        self.buzzer = Buzzer(15)

    def alert(self):
        self._sound_alarm()

    def stop_alert(self):
        self._silence_alarm()

    def _sound_alarm(self):
        if not self.buzzer.is_active:
            logging.info("Buzzer will be turned on.")
            self.buzzer.on()
        else:
            logging.info("Buzzer is currently active, will not attempt to turn it on.")

    def _silence_alarm(self):
        if self.buzzer.is_active:
            logging.info("Buzzer will be turned off")
            self.buzzer.off()
        else:
            logging.info("Buzzer is not currently active, will not attempt to turn it off.")
