from dataclasses import dataclass

@dataclass
class Config:
    """Config data structure for passing settings around"""
    water_control_pump_pin: int