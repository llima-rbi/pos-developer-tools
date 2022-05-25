from datetime import timedelta, datetime
from logging import Logger
from uuid import uuid4

from application.model import Configurations, TokenUser, AuthorizationFailed
from application.thread import CleanTokenThread
from typing import Dict


class LoginService(object):
    def __init__(self, logger, configurations):
        # type: (Logger, Configurations) -> None

        self.logger = logger
        self.configs = configurations
        
        self.tokens = {}  # type: Dict[unicode, TokenUser]
        self.time_to_cookies_expire_in_minutes = self.configs.time_to_cookies_expire_in_minutes
        self.clean_token_thread = CleanTokenThread(self.time_to_cookies_expire_in_minutes, self)
        self.clean_token_thread.start()
    
    def login(self, user_name, password):
        # type: (str, str) -> bool
        
        self._authenticate_user(user_name.encode("utf-8"), password.encode("utf-8"))
        
        new_token = str(uuid4())
        self.tokens[new_token] = TokenUser(user_name, self._get_new_expire_time())
        
        return new_token

    def logout(self, token):
        # type: (str) -> None
        
        if token in self.tokens:
            del self.tokens[token]
        
    def is_valid_token(self, token):
        # type: (str) -> bool
        
        if not token:
            return False

        if token in self.tokens:
            if self.tokens[token].expire_datetime >= datetime.now():
                self.tokens[token].expire_datetime = self._get_new_expire_time()
                return True
            else:
                del self.tokens[token]

        return False

    def clean_expired_tokens(self):
        # type: () -> None
        for token in self.tokens:
            if self.tokens[token].expire_datetime < datetime.now():
                del self.tokens[token]

    def _get_new_expire_time(self):
        return datetime.now() + timedelta(minutes=float(self.time_to_cookies_expire_in_minutes) * 60)
    
    @staticmethod
    def _authenticate_user(user_name, password):
        # type: (str, str) -> None
        
        if user_name == "admin" and password == "admin":
            # TODO: Implement authentication method
            return
        
        raise AuthorizationFailed("Invalid user of password")
