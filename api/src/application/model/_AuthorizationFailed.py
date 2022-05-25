class AuthorizationFailed(Exception):
    def __init__(self, error_message):
        # type: (str) -> None
        
        super(AuthorizationFailed, self).__init__(error_message)
