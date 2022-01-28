import json
import time

import pika
from pika.exceptions import AMQPConnectionError

from service.alert_delegator_service import AlerterService
import logging


class SecurityConfigSubscriber:
    def __init__(self,
                 rabbitmq_host: str,
                 alerter_security_config_queue_name: str,
                 exchange_name: str,
                 alerter_service: AlerterService):
        self.received_security_config = {}
        self.alerter_service = alerter_service
        self.rabbitmq_host = rabbitmq_host
        self.alerter_security_config_queue_name = alerter_security_config_queue_name
        self.exchange_name = exchange_name
        self.connect(alerter_security_config_queue_name, exchange_name, rabbitmq_host)

    def connect(self, alerter_security_config_queue_name, exchange_name, rabbitmq_host):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbitmq_host)
        )
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=exchange_name,
                                      exchange_type='fanout',
                                      durable=True)
        self.channel.queue_declare(queue=alerter_security_config_queue_name)
        self.channel.queue_bind(exchange=exchange_name,
                                queue=alerter_security_config_queue_name)
        self.channel.basic_consume(queue=alerter_security_config_queue_name,
                                   on_message_callback=self.receive_security_config,
                                   auto_ack=True)

    def listen_for_security_config_messages(self):
        try:
            logging.info("Listening for messages...")
            self.channel.start_consuming()
        except AMQPConnectionError:
            time.sleep(5)
            logging.info("Connection failed, attempting to reconnect.")
            self.connect(self.alerter_security_config_queue_name, self.exchange_name, self.rabbitmq_host)
            self.listen_for_security_config_messages()

    def receive_security_config(self, ch, method, properties, body):
        security_config_string = body.decode()
        security_config = json.loads(security_config_string)
        self.received_security_config = security_config
        logging.info("New security config received: %s", security_config)
        self.alerter_service.delegate(security_config)
