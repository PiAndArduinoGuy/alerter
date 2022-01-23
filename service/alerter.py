from abc import ABC, abstractmethod


class Alerter(ABC):
    def __init__(self):
        self.condition = None

    @abstractmethod
    def alert_given(self, condition):
        pass

    @abstractmethod
    def alert(self):
        pass

    @abstractmethod
    def stop_alert(self):
        pass
