try:
    import RPi.GPIO as GPIO
except: 
    import Mock.GPIO as GPIO

from config_loader.json_reader import JsonReader
from config_loader.monitor_config import Config

def main():
    reader = JsonReader(r"monitor_config.json")
    json = reader.get_json()
    
    config = Config.from_json(json)
    print(config)
    print(config.water_control_pump_pin)

    json_str = config.to_json()
    print(json_str)

if __name__=="__main__":
    main()
        