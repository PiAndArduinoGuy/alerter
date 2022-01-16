import sys
from threading import Thread

from alerter_service import AlerterService
from keypad_alarm_silencer import KeyPadAlarmSilencer
from security_config_subscriber import SecurityConfigSubscriber

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

    keypad_alarm_silencer = KeyPadAlarmSilencer(
        rabbitmq_host,
        alerter_security_config_queue_name,
        exchange_name,
        security_config_subscriber)

    security_config_subscriber_thread = Thread(name='security_config_subscriber_thread',
                                               target=security_config_subscriber.listen_for_security_config_messages)
    keypad_thread = Thread(name='keypad_thread',
                           target=keypad_alarm_silencer.get_entered_password)
    security_config_subscriber_thread.start()
    keypad_thread.start()
