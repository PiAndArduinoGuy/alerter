import pika
import json

from alerter_service import AlerterService


class SecurityConfigSubscriber:
    def __init__(self,
                 rabbitmq_host: str,
                 alerter_security_config_queue_name: str,
                 exchange_name: str,
                 alerter_service: AlerterService):
        self.alerter_service = alerter_service
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
        print("Listening for messages...")
        self.channel.start_consuming()

    def receive_security_config(self, ch, method, properties, body):
        securityConfigString = body.decode()
        securityConfig = json.loads(securityConfigString)
        print(f"New security config received: {securityConfig}")
        securityStatus = securityConfig['securityStatus']
        if securityStatus == 'BREACHED':
            print("Security status is breached. Attempting alert")
            zone_number = securityConfig['zoneNumber']
            self.alerter_service.alert(zone_number)
        elif securityStatus == 'SAFE':
            print("Security status is safe. Alert will not be triggered.")
            self.alerter_service.stop_alert()
        else:
            print(f"Unrecognized security status {securityStatus}")
