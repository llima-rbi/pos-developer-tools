from datetime import datetime


class TokenUser(object):
    def __init__(self, user, expire_datetime):
        # type: (str, datetime) -> None
        
        self.user = user
        self.expire_datetime = expire_datetime
