import json
from dataclasses import dataclass

@dataclass
class Config:
    """Config data structure for passing settings around"""
    water_control_pump_pin: int

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json):
        return cls(**json)