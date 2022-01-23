from gpiozero import LED

from service.security_status_alerter_service import SecurityStatusAlerterService


class AlerterService:
    def __init__(self,
                 security_status_alerter_service: SecurityStatusAlerterService):
        self.alarm_arm_led_indicator = LED(25)
        self.security_status_alerter_service = security_status_alerter_service

    def perform_alerting_given_security_config(self, security_config):
        security_status = security_config['securityStatus']
        self.security_status_alerter_service.alert_given(security_status)
        security_state = security_config['securityState']
        self.alert_for_security_state(security_state)

    def alert_for_security_state(self, security_state):
        if security_state == 'ARMED':
            print("Security state is armed. Alarm arm LED indicator will be turned on.")
            self.alarm_arm_led_indicator.on()
        elif security_state == 'DISARMED':
            print("Security state is disarmed. Alarm arm LED indicator will be turned off.")
            self.alarm_arm_led_indicator.off()
        else:
            print(f"Unrecognized security state {security_state}")
