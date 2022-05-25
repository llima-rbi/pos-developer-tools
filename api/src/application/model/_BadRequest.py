class BadRequest(object):
    def __init__(self, invalid_property_name, reason, localized_error_message):
        # type: (str, str, str) -> None
        
        self.invalid_property_name = invalid_property_name
        self.reason = reason
        self.localized_error_message = localized_error_message
