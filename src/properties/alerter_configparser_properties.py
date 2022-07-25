import logging
from configparser import ConfigParser

from src.properties.alerter_properties import AlerterProperties

LOGGER = logging.getLogger(__name__)

class AlerterConfigParserProperties(AlerterProperties):
    
    def __init__(self):
        super().__init__()
        self._config_parser = ConfigParser()
        self._config_parser.read("../alerter_properties.ini")
        LOGGER.info(f"Config parser used for alerter properties, .ini properties file will be used with sections "
                    f"{self._config_parser.sections()}")

    def set_logging_file_location(self):
        self._logging_file_location = self._config_parser['alerter.properties']['logging_file_location']

    def set_rabbitmq_host(self):
        self._rabbitmq_host = self._config_parser['rabbitmq.properties']['host']

    def set_alerter_security_config_queue_name(self):
        self._alerter_security_config_queue_name = self._config_parser['alerter.properties']['alerter_security_config_queue_name']

    def set_exchange_name(self):
        self._exchange_name = self._config_parser['alerter.properties']['exchange_name']