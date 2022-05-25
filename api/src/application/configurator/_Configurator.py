from application.model import Configurations
from helper import read_json_from_file_as_dictionary


class Configurator(object):
    
    @staticmethod
    def load_configurations(config_path):
        # type: (str) -> Configurations
        
        cfg = read_json_from_file_as_dictionary(config_path)
        
        configs = Configurations()
        configs.flask_port = cfg.get("FlaskPort")
        configs.allowed_urls = cfg.get("AllowedUrls")
        
        configs.time_to_cookies_expire_in_minutes = cfg.get("TimeToCookiesExpireInMinutes", 10)

        return configs
