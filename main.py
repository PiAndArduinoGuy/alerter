import sys
from security_config_subscriber import SecurityConfigSubscriber

if __name__ == '__main__':
    rabbitmq_parameters = sys.argv[1:]
    rabbitmq_host = rabbitmq_parameters[0]
    alerter_security_config_queue_name = rabbitmq_parameters[1]
    exchange_name = rabbitmq_parameters[2]
    security_config_subscriber = SecurityConfigSubscriber(rabbitmq_host,
                                                          alerter_security_config_queue_name,
                                                          exchange_name)


