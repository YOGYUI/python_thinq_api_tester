import os
import sys
CURPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([CURPATH])
sys.path = list(set(sys.path))

from ThinqAPI import ThinqAPI
from ThinqGUI import ThinqGUI
