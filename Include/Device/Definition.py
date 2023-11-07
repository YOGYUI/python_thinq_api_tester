from enum import IntEnum, unique


@unique
class DeviceType(IntEnum):
    Unknown = 0
    Washer = 201
    Dryer = 202
    Styler = 203
    AirConditioner = 401
    AirPurifier = 402
    Dehumidifier = 403
    RobotCleaner = 501
