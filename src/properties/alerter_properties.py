from abc import ABC, abstractmethod

from src.properties.validation.alerter_properties_validator import AlerterPropertiesValidator


class AlerterProperties(ABC):
    def __init__(self):
        self._logging_file_location = None
        self._rabbitmq_host = None
        self._alerter_security_config_queue_name = None
        self._exchange_name = None

    def get_logging_file_location(self):
        AlerterPropertiesValidator.validate_property_non_none(self._logging_file_location)
        return self._logging_file_location

    def get_rabbitmq_host(self):
        AlerterPropertiesValidator.validate_property_non_none(self._rabbitmq_host)
        return self._rabbitmq_host

    def get_alerter_security_config_queue_name(self):
        AlerterPropertiesValidator.validate_property_non_none(self._alerter_security_config_queue_name)
        return self._alerter_security_config_queue_name

    def get_exchange_name(self):
        AlerterPropertiesValidator.validate_property_non_none(self._exchange_name)
        return self._exchange_name

    @abstractmethod
    def set_logging_file_location(self):
        pass

    @abstractmethod
    def set_rabbitmq_host(self):
        pass

    @abstractmethod
    def set_alerter_security_config_queue_name(self):
        pass

    @abstractmethod
    def set_exchange_name(self):
        pass

    def set_alerter_properties(self):
        self.set_logging_file_location()
        self.set_rabbitmq_host()
        self.set_alerter_security_config_queue_name()
        self.set_exchange_name()
