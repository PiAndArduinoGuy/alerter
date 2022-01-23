from gpiozero import Buzzer, LED


class AlerterService:
    def __init__(self):
        self.buzzer = Buzzer(15)
        self.alarm_arm_led_indicator = LED(25)

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
        self.alert_for_security_status(security_status)
        security_state = security_config['securityState']
        self.alert_for_security_state(security_state)

    def alert_for_security_status(self, security_status):
        if security_status == 'BREACHED':
            print("Security status is breached. Attempting to alert")
            self._alert()
        elif security_status == 'SAFE':
            print("Security status is safe. Attempting to stop alert.")
            self._stop_alert()
        else:
            print(f"Unrecognized security status {security_status}")

    def alert_for_security_state(self, security_state):
        if security_state == 'ARMED':
            print("Security state is armed. Alarm arm LED indicator will be turned on.")
            self.alarm_arm_led_indicator.on()
        elif security_state == 'DISARMED':
            print("Security state is disarmed. Alarm arm LED indicator will be turned off.")
            self.alarm_arm_led_indicator.off()
        else:
            print(f"Unrecognized security state {security_state}")
