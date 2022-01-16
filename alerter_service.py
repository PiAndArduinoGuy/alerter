from gpiozero import Buzzer

from alerter_error import AlerterError
from validation_util import ValidationUtil


class AlerterService:
    def __init__(self):
        self.triggered_zone = -1
        self.buzzer = Buzzer(15)

    def _alert(self, zone_number):
        try:
            ValidationUtil.validate_zone_number(zone_number)
            ValidationUtil.validate_alerter_not_yet_triggered(self.triggered_zone)
            self._sound_alarm()
        except AlerterError as alerter_error:
            print(f"AlerterError occurred with message '{alerter_error}'")

    def stop_alert(self):
        try:
            self._silence_alarm()
        except AlerterError as alerter_error:
            print(f"AlerterError occurred with message '{alerter_error}'")

    def _sound_alarm(self):
        print("Buzzer will be turned on.")
        self.buzzer.on()

    def _silence_alarm(self):
        print("Buzzer will be turned off")
        self.buzzer.off()

    def perform_alerting_given_security_config(self, security_config):
        security_status = security_config['securityStatus']
        if security_status == 'BREACHED':
            print("Security status is breached. Attempting alert")
            zone_number = security_config['zoneNumber']
            self._alert(zone_number)
        elif security_status == 'SAFE':
            print("Security status is safe. Alert will not be triggered.")
            self.stop_alert()
        else:
            print(f"Unrecognized security status {security_status}")
