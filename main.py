from properties.alerter_command_line_properties import AlerterCommandLineProperties
from properties.alerter_properties import AlerterProperties
from logging_setup import LoggingSetup
from threading import Thread

from service.alert_delegator_service import AlerterService
from security_config_subscriber import SecurityConfigSubscriber

from service.security_state_alerter_service import SecurityStateAlerterService
from service.security_status_alerter_service import SecurityStatusAlerterService

if __name__ == '__main__':
    alerter_properties: AlerterProperties = AlerterCommandLineProperties()
    alerter_properties.set_alerter_properties()

    logging_setup = LoggingSetup(alerter_properties.get_logging_file_location())
    security_status_alerter_service = SecurityStatusAlerterService()
    security_state_alerter_service = SecurityStateAlerterService()
    alerter_service = AlerterService(security_status_alerter_service,
                                     security_state_alerter_service)
    security_config_subscriber = SecurityConfigSubscriber(alerter_properties.get_rabbitmq_host(),
                                                          alerter_properties.get_alerter_security_config_queue_name(),
                                                          alerter_properties.get_exchange_name(),
                                                          alerter_service)

    security_config_subscriber.listen_for_security_config_messages()
