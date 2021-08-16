import config_loader.monitor_config as monitor_config

try:
    import RPi.GPIO as GPIO
except: 
    import Mock.GPIO as GPIO

class WaterPump:
    """Allows control of the water pump
    and abstracts Pi related details"""
    __GPIO_pump_pin: int

    def __init__(self, config: monitor_config.Config):
        self.GPIO_pump_pin = config.water_control_pump_pin