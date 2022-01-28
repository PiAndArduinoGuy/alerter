from abc import ABC, abstractmethod
import logging

LOGGER = logging.getLogger(__name__)

class Alerter(ABC):
    def __init__(self):
        self.condition = None

    def alert_given(self, alert_condition, stop_alert_condition):
        if alert_condition:
            LOGGER.info("Alert condition met, alert method called.")
            self.alert()
        elif stop_alert_condition:
            LOGGER.info("Stop alert condition met, stop alert method called.")
            self.stop_alert()
        else:
            LOGGER.info("Neither alert condition nor stop alert condition was met.")

    @abstractmethod
    def alert(self):
        pass

    @abstractmethod
    def stop_alert(self):
        pass
