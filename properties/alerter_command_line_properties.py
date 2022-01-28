import argparse

from properties.alerter_properties import AlerterProperties


class AlerterCommandLineProperties(AlerterProperties):
    def __init__(self):
        super().__init__()
        parser = argparse.ArgumentParser()
        parser.add_argument("--logging_file_location", required=True)
        parser.add_argument("--rabbitmq_host", required=True)
        parser.add_argument("--alerter_security_config_queue_name", required=True)
        parser.add_argument("--exchange_name", required=True)
        self.arguments = vars(parser.parse_args())

    def set_logging_file_location(self):
        self._logging_file_location = self.arguments["logging_file_location"]

    def set_rabbitmq_host(self):
        self._rabbitmq_host = self.arguments["rabbitmq_host"]

    def set_alerter_security_config_queue_name(self):
        self._alerter_security_config_queue_name = self.arguments["alerter_security_config_queue_name"]

    def set_exchange_name(self):
        self._exchange_name = self.arguments["exchange_name"]
