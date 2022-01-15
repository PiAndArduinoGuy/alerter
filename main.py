import sys

from alerter_service import AlerterService
from keypad import KeyPad
from security_config_subscriber import SecurityConfigSubscriber
from threading import Thread

if __name__ == '__main__':
    rabbitmq_parameters = sys.argv[1:]
    rabbitmq_host = rabbitmq_parameters[0]
    alerter_security_config_queue_name = rabbitmq_parameters[1]
    exchange_name = rabbitmq_parameters[2]
    alerter_service = AlerterService()
    security_config_subscriber = SecurityConfigSubscriber(rabbitmq_host,
                                                          alerter_security_config_queue_name,
                                                          exchange_name,
                                                          alerter_service)

    keypad = KeyPad(alerter_service)

    security_config_subscriber_thread = Thread(name='security_config_subscriber_thread',
                                               target=security_config_subscriber.listen_for_security_config_messages)
    keypad_thread = Thread(name='keypad_thread',
                           target=keypad.get_entered_password)
    security_config_subscriber_thread.start()
    keypad_thread.start()

