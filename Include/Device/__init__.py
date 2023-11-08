import os
import sys
CURPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([CURPATH])
sys.path = list(set(sys.path))

from Definition import DeviceType
from DeviceCommon import DeviceCommon
from AirConditioner import AirConditioner
from AirPurifier import AirPurifier
from Dehumidifier import Dehumidifier
from Dryer import Dryer
from RobotCleaner import RobotCleaner
from Styler import Styler
from Washer import Washer
