import pika


class SecurityConfigPublisher:
    def __init__(self,
                 rabbitmq_host: str,
                 alerter_security_config_queue_name: str,
                 exchange_name: str
                 ):
        self.exchange_name = exchange_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(rabbitmq_host))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=alerter_security_config_queue_name)

    def send_updated_security_config(self, security_config):
        self.channel.basic_publish(
            exchange=self.exchange_name,
            body=security_config,
            routing_key=''
        )
