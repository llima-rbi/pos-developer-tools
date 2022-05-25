from threading import Thread, Condition


class CleanTokenThread(Thread):
    def __init__(self, time_to_cookies_expire_in_minutes, login_service):
        # type: (int, LoginService) -> None
        
        super(CleanTokenThread, self).__init__()
        
        self.time_to_cookies_expire_in_minutes = time_to_cookies_expire_in_minutes
        self.thread_condition = Condition()
        self.running = True
        self.daemon = True
        self.login_service = login_service

    def run(self):
        # type: () -> None
        while self.running:
            self.login_service.clean_expired_tokens()

            with self.thread_condition:
                self.thread_condition.wait(self.time_to_cookies_expire_in_minutes * 60)

    def stop(self):
        if self.running:
            with self.thread_condition:
                self.running = False
                self.thread_condition.notifyAll()
