import logging
import os
from time import sleep

from application.configurator import Configurator
from application.server import FlaskServer, set_allowed_urls
from application.service import LoginService, StoresService
from helper import config_logger


def main():
    service_name = "PosDeveloperTools"
    
    config_logger(_get_log_path(), service_name)
    logger = logging.getLogger(service_name)
    
    configs = Configurator.load_configurations(_get_config_path())

    set_allowed_urls(configs.allowed_urls)

    flask_server = FlaskServer(logger,
                               configs.flask_port,
                               LoginService(logger, configs),
                               StoresService(logger, configs))
    
    flask_server.configure_globals()
    flask_server.start()
    
    while True:
        sleep(100)


def _get_config_path():
    current_file_path = os.path.abspath(os.getcwd())
    return os.path.join(current_file_path, "../../configs.json")


def _get_log_path():
    current_file_path = os.path.abspath(os.getcwd())
    return os.path.join(current_file_path, "../logs")


if __name__ == "__main__":
    main()
