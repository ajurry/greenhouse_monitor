from dataclasses import dataclass
from configparser import ConfigParser

config_item = 'monitor'

@dataclass
class MonitorConfig:
    """Config data structure for passing settings around"""

    def __init__(self, config_parser: ConfigParser):
        specified_config_item = config_parser.items(config_item)
        self.__dict__.update(specified_config_item)
