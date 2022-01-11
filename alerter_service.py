from gpiozero import LED, Buzzer

from alerter_error import AlerterError
from validation_util import ValidationUtil


class AlerterService:
    def __init__(self):
        zone_one_led = LED(6)
        zone_two_led = LED(13)
        zone_three_led = LED(19)
        zone_four_led = LED(26)
        self.zone_leds = [zone_one_led, zone_two_led, zone_three_led, zone_four_led]
        self.triggered_zone = -1
        self.buzzer = Buzzer(15)

    def alert(self, zone_number):
        try:
            ValidationUtil.validate_zone_number(zone_number)
            self._sound_alarm()
            self._light_up_zone_led(zone_number)
        except AlerterError as alerter_error:
            print(f"AlerterError occurred with message '{alerter_error}'")

    def stop_alert(self):
        if self.triggered_zone != -1:
            self._silence_alarm()
        else:
            print("No zones have been triggered. No sounding alarm to silence")

    def _alerter_not_previously_triggered(self):
        return self.triggered_zone == -1

    def _light_up_zone_led_if_possible(self, zone_number):
        try:
            ValidationUtil.validate_alerter_not_yet_triggered(self.triggered_zone)
            print(f"Zone {zone_number} was triggered, lighting up zone {zone_number} LED now")
            self.zone_leds[zone_number - 1].blink()
            self.triggered_zone = zone_number
        except AlerterError as alerter_error:
            print(f"AlerterError occurred with message '{alerter_error}'")

    def _sound_alarm(self):
        print("Buzzer will be turned on.")
        self.buzzer.on()

    def _silence_alarm(self):
        print("Buzzer will be turned off")
        self.buzzer.off()

    def _light_up_zone_led(self, zone_number):
        self._light_up_zone_led_if_possible(zone_number)
