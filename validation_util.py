from alerter_error import AlerterError


class ValidationUtil:
    zone_numbers = [1, 2, 3, 4]

    @staticmethod
    def validate_zone_number(zone_number):
        if zone_number not in ValidationUtil.zone_numbers:
            raise AlerterError(
                f"An unrecognized zone was received -> {zone_number}, valid zones are {ValidationUtil.zone_numbers}")

    @staticmethod
    def validate_alerter_not_yet_triggered(triggered_zone_number):
        if not triggered_zone_number == -1:
            raise AlerterError(f"Zone {triggered_zone_number} has already triggered the alerter.")
