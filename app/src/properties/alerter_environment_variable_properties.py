import logging

from properties.alerter_properties import AlerterProperties
from os import environ

LOGGER = logging.getLogger(__name__)


class AlerterEnvironmentVariableProperties(AlerterProperties):
    def __init__(self):
        super().__init__()
        LOGGER.info("Environment variable alerter properties used.")
        self.set_alerter_properties()

    def set_logging_file_directory(self):
        self._logging_file_directory = environ['ALERTER_LOGGING_FILE_DIRECTORY']

    def set_rabbitmq_host(self):
        self._rabbitmq_host = environ['ALERTER_RABBITMQ_HOST']

    def set_alerter_security_config_queue_name(self):
        self._security_config_queue_name = environ['ALERTER_SECURITY_CONFIG_QUEUE_NAME']

    def set_exchange_name(self):
        self._exchange_name = environ['ALERTER_EXCHANGE_NAME']
