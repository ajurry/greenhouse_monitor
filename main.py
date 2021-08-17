try:
    import RPi.GPIO as GPIO
except: 
    import Mock.GPIO as GPIO

from config_loader.monitor_config import MonitorConfig
from configparser import ConfigParser
from water_controls.water_pump import WaterPump

def main():
    
    config_parser = ConfigParser()
    config_parser.read('monitor_config.ini')

    water_pump = WaterPump(config_parser)
    print(water_pump.water_control_pump_pin)
    print(water_pump)

if __name__=="__main__":
    main()
        