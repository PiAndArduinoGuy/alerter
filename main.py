import sys
from threading import Thread

from service.alert_delegator_service import AlerterService
from security_config_subscriber import SecurityConfigSubscriber
from service.security_state_alerter_service import SecurityStateAlerterService
from service.security_status_alerter_service import SecurityStatusAlerterService

if __name__ == '__main__':
    rabbitmq_parameters = sys.argv[1:]
    rabbitmq_host = rabbitmq_parameters[0]
    alerter_security_config_queue_name = rabbitmq_parameters[1]
    exchange_name = rabbitmq_parameters[2]
    security_status_alerter_service = SecurityStatusAlerterService()
    security_state_alerter_service = SecurityStateAlerterService()
    alerter_service = AlerterService(security_status_alerter_service,
                                     security_state_alerter_service)
    security_config_subscriber = SecurityConfigSubscriber(rabbitmq_host,
                                                          alerter_security_config_queue_name,
                                                          exchange_name,
                                                          alerter_service)

    security_config_subscriber_thread = Thread(name='security_config_subscriber_thread',
                                               target=security_config_subscriber.listen_for_security_config_messages)

    security_config_subscriber_thread.start()
