import config_loader.json_config_reader as json_config_reader
import config_loader.monitor_config as monitor_config


def main():
    reader = json_config_reader.JsonConfigReader(r"monitor_config.json")
    config = reader.get_config()
    print(config.water_control_pump_pin)

if __name__=="__main__":
    main()
        