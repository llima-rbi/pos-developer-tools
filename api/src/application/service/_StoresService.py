from logging import Logger

from application.model import Configurations
from helper import json_serialize


class StoresService(object):
    
    def __init__(self, logger, configurations):
        # type: (Logger, Configurations) -> None
        
        self.logger = logger
        self.configs = configurations

    @staticmethod
    def get_all_stores():
        all_stores_json = \
            {
                    99999: "10.200.22.1",
                    17764: "10.89.59.1"
            }
        
        return json_serialize(all_stores_json)
