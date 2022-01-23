from service.security_state_alerter_service import SecurityStateAlerterService
from service.security_status_alerter_service import SecurityStatusAlerterService


class AlerterService:
    def __init__(self,
                 security_status_alerter_service: SecurityStatusAlerterService,
                 security_state_alerter_service: SecurityStateAlerterService):
        self.security_status_alerter_service = security_status_alerter_service
        self.security_state_alerter_service = security_state_alerter_service

    def perform_alerting_given_security_config(self, security_config):
        security_status = security_config['securityStatus']
        self.security_status_alerter_service.alert_given(security_status)
        security_state = security_config['securityState']
        self.security_state_alerter_service.alert_given(security_state)
