import json
import logging
import time

import pika
from pika.exceptions import AMQPConnectionError

from service.alert_delegator_service import AlerterService


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

    def listen_for_security_config_messages(self):
        while True:
            try:
                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=self.rabbitmq_host)
                )
                channel = connection.channel()
                channel.exchange_declare(exchange=self.exchange_name,
                                         exchange_type='fanout',
                                         durable=True)
                channel.queue_declare(queue=self.alerter_security_config_queue_name)
                channel.queue_bind(exchange=self.exchange_name,
                                   queue=self.alerter_security_config_queue_name)
                channel.basic_consume(queue=self.alerter_security_config_queue_name,
                                      on_message_callback=self.receive_security_config,
                                      auto_ack=True)
                logging.info("Listening for messages...")
                channel.start_consuming()
            except AMQPConnectionError as e:
                logging.error("An AMQPConnectionError has occurred: %r, this exception is eligible for reconnect.", e)
                time.sleep(5)
                logging.info("Attempting to reconnect.")
                continue
            except Exception as e:
                logging.error(
                    "Exception occurred listening to messages: %r, this exception is not eligible for reconnect.", e)
                raise

    def receive_security_config(self, ch, method, properties, body):
        security_config_string = body.decode()
        security_config = json.loads(security_config_string)
        self.received_security_config = security_config
        logging.info("New security config received: %s", security_config)
        self.alerter_service.delegate(security_config)
