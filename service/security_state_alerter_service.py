from service.alerter import Alerter
from gpiozero import LED


class SecurityStateAlerterService(Alerter):
    def __init__(self):
        super().__init__()
        self.alarm_arm_led_indicator = LED(25)

    def alert_given(self, condition):
        if condition == 'ARMED':
            print("Security state is armed.")
            self.alert()
        elif condition == 'DISARMED':
            print("Security state is disarmed. Alarm arm LED indicator will be turned off.")
            self.stop_alert()
        else:
            print(f"Unrecognized security state {condition}")

    def alert(self):
        if not self.alarm_arm_led_indicator.is_active:
            print("Alarm arm LED indicator will be turned on.")
            self.alarm_arm_led_indicator.on()
        else:
            print("Alarm arm LED indicator is currently active, will not attempt turn it on.")

    def stop_alert(self):
        if self.alarm_arm_led_indicator.is_active:
            print("Alarm arm LED indicator will be turned off")
            self.alarm_arm_led_indicator.off()
        else:
            print("Alarm arm LED indicator is not currently active, will not attempt to turn it off.")