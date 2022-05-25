from typing import Optional, List


class Configurations(object):
    def __init__(self):
        self.time_to_cookies_expire_in_minutes = None  # type: Optional[int]
        self.flask_port = None  # type: Optional[int]
        self.allowed_urls = None  # type: Optional[List[str]]
