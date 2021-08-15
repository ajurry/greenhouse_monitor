import json
import config_loader.monitor_config as monitor_config

class JsonConfigReader:
    """Used to load and extract the config
    information from monitor_config.json"""
    def __init__(self, file_path):
        self.__loaded_json = r"{}"
        self.__file_path = file_path
        self.config = monitor_config.Config

        self.__load_json()
        self.__extract_config_from_json()
    
    def get_config(self):
        return self.config

    def __load_json(self):
        """Loaded config json from file"""
        with open(self.__file_path) as json_file:
            self.__loaded_json = json.load(json_file)

    # Breaking O\C principle here
    # Probably worth using a build in future
    def __extract_config_from_json(self):
        """Look-up to see if we have key pairs"""
        if "water_control_pump_pin" in self.__loaded_json:
            self.config.water_control_pump_pin =\
                self.__loaded_json["water_control_pump_pin"]
        
