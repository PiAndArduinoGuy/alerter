from abc import ABC, abstractmethod


class Alerter(ABC):
    def __init__(self):
        self.condition = None

    def alert_given(self, alert_condition, stop_alert_condition):
        if alert_condition:
            print(f"Alert condition met, alert method called.")
            self.alert()
        elif stop_alert_condition:
            print(f"Stop alert condition met, stop alert method called.")
            self.stop_alert()
        else:
            print(f"Neither alert condition nor stop alert condition was met.")

    @abstractmethod
    def alert(self):
        pass

    @abstractmethod
    def stop_alert(self):
        pass
