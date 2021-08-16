import json
from config_loader.monitor_config import Config

class JsonReader:
    """Used to load and extract the config
    information from monitor_config.json"""
    def __init__(self, file_path):
        self.__loaded_json = r"{}"
        self.__file_path = file_path
        self.__load_json()
    
    def get_json(self):
        return self.__loaded_json

    def __load_json(self):
        """Loaded config json from file"""
        with open(self.__file_path) as json_file:
            self.__loaded_json = json.load(json_file)