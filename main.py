try:
    import RPi.GPIO as GPIO
except: 
    import Mock.GPIO as GPIO

import config_loader.json_config_reader as json_config_reader
import config_loader.monitor_config as monitor_config

def main():
    reader = json_config_reader.JsonConfigReader(r"monitor_config.json")
    config = reader.get_config()
    
    

if __name__=="__main__":
    main()
        