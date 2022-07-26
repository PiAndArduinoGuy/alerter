from logging_setup import LoggingSetup
from properties.alerter_configparser_properties import AlerterConfigParserProperties
from properties.alerter_properties import AlerterProperties
from security_config_subscriber import SecurityConfigSubscriber
from service.alert_delegator_service import AlerterService
from service.security_state_alerter_service import SecurityStateAlerterService
from service.security_status_alerter_service import SecurityStatusAlerterService

if __name__ == '__main__':
    alerter_properties: AlerterProperties = AlerterConfigParserProperties()

    logging_setup = LoggingSetup(alerter_properties.get_logging_file_directory())
    security_status_alerter_service = SecurityStatusAlerterService()
    security_state_alerter_service = SecurityStateAlerterService()
    alerter_service = AlerterService(security_status_alerter_service,
                                     security_state_alerter_service)
    security_config_subscriber = SecurityConfigSubscriber(
        alerter_properties,
        alerter_service)

    security_config_subscriber.listen_for_security_config_messages()
