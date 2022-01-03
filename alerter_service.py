from gpiozero import LED


class AlerterService:
    def __init__(self):
        zone_one_led = LED(6)
        zone_two_led = LED(13)
        zone_three_led = LED(19)
        zone_four_led = LED(26)
        self.zone_leds = [zone_one_led, zone_two_led, zone_three_led, zone_four_led]
        self.zone_numbers = [1, 2, 3, 4]
        self.triggered_zone = -1

    def _sound_alarm(self):
        print("Use you imagination and hear the alarm going off")

    def _light_up_zone_led(self, zone_number):
        if zone_number in self.zone_numbers:
            self._light_up_zone_led_if_possible(zone_number)
        else:
            print(f"An unrecognized zone was received -> {zone_number}, valid zones are 1,2,3 and 4")

    def alert(self, zone_number):
        self._sound_alarm()
        self._light_up_zone_led(zone_number)

    def _alerter_not_previously_triggered(self):
        return self.triggered_zone == -1

    def _light_up_zone_led_if_possible(self, zone_number):
        if self._alerter_not_previously_triggered():
            print(f"Zone {zone_number} was triggered, lighting up zone {zone_number} LED now")
            self.zone_leds[zone_number - 1].blink()
            self.triggered_zone = zone_number
        else:
            print(f"Zone {self.triggered_zone} has already triggered the alerter.")
