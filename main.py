from logging_setup import LoggingSetup
import argparse
from threading import Thread

from service.alert_delegator_service import AlerterService
from security_config_subscriber import SecurityConfigSubscriber

from service.security_state_alerter_service import SecurityStateAlerterService
from service.security_status_alerter_service import SecurityStatusAlerterService

if __name__ == '__main__':
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--logging_file_location", required=True)
    argparse.add_argument("--rabbitmq_host", required=True)
    argparse.add_argument("--alerter_security_config_queue_name", required=True)
    argparse.add_argument("--exchange_name", required=True)
    arguments = vars(argparse.parse_args())

    logging_file_location = arguments["logging_file_location"]
    rabbitmq_host = arguments["rabbitmq_host"]
    alerter_security_config_queue_name = arguments["alerter_security_config_queue_name"]
    exchange_name = arguments["exchange_name"]

    print(f"Received arguments: \n logging_file_location = {logging_file_location} \n"
          f" rabbitmq_host = {rabbitmq_host} \n"
          f" alerter_security_config_queue_name = {alerter_security_config_queue_name} \n "
          f"exchange_name = {exchange_name}")

    logging_setup = LoggingSetup(logging_file_location)
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
