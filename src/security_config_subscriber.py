import json
import logging
import time

import pika
from pika.exceptions import AMQPConnectionError

from properties.alerter_properties import AlerterProperties
from service.alert_delegator_service import AlerterService

LOGGER = logging.getLogger(__name__)


class SecurityConfigSubscriber:

    def __init__(self,
                 alerter_properties: AlerterProperties,
                 alerter_service: AlerterService):
        self.received_security_config = {}
        self.alerter_service = alerter_service
        self.alerter_properties = alerter_properties

    def listen_for_security_config_messages(self):
        while True:
            try:
                rabbitmq_host = self.alerter_properties.get_rabbitmq_host()
                exchange_name = self.alerter_properties.get_exchange_name()
                alerter_security_config_queue_name = self.alerter_properties.get_alerter_security_config_queue_name()

                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host=rabbitmq_host)
                )
                channel = connection.channel()
                channel.exchange_declare(exchange=exchange_name,
                                         exchange_type='fanout',
                                         durable=True)
                channel.queue_declare(queue=alerter_security_config_queue_name)
                channel.queue_bind(exchange=exchange_name,
                                   queue=alerter_security_config_queue_name)
                channel.basic_consume(queue=alerter_security_config_queue_name,
                                      on_message_callback=self.receive_security_config,
                                      auto_ack=True)
                LOGGER.info("Listening for messages...")
                channel.start_consuming()
            except AMQPConnectionError as e:
                LOGGER.error("An AMQPConnectionError has occurred: %r, this exception is eligible for reconnect.", e)
                time.sleep(5)
                logging.info("Attempting to reconnect.")
                continue
            except Exception as e:
                LOGGER.error(
                    "Exception occurred listening to messages: %r, this exception is not eligible for reconnect.", e)
                raise

    def receive_security_config(self, ch, method, properties, body):
        security_config_string = body.decode()
        security_config = json.loads(security_config_string)
        self.received_security_config = security_config
        LOGGER.info("New security config received: %s", security_config)
        self.alerter_service.delegate(security_config)
