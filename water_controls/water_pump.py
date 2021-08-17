import config_loader.monitor_config as monitor_config
from configparser import ConfigParser

try:
    import RPi.GPIO as GPIO
except: 
    import Mock.GPIO as GPIO

config_item = 'water_pump'

class WaterPump:
    """Allows control of the water pump
    and abstracts Pi related details"""
    __GPIO_pump_pin: int

    def __init__(self, config_parser: ConfigParser):
        specified_config_item = config_parser.items(config_item)
        self.__dict__.update(specified_config_item)
        