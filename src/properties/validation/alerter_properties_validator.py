from src.properties.validation.alerter_properties_error import AlerterPropertiesError


class AlerterPropertiesValidator:
    @staticmethod
    def validate_property_non_none(alerter_property):
        if alerter_property is None:
            raise AlerterPropertiesError(
                "An alerter property has a none value, the set_alerter_properties method needs to "
                "be called prior to accessing any properties.")
