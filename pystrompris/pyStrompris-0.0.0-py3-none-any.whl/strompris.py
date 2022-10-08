
from datetime import datetime
from typing import final
import pytz

from strompris.common import Common

class Strompris(Common):
    
    def __init__(self) -> None:
        pass
    
    @final
    def showPriceZones(self) -> None:
        print("NO1", "Øst-Norge")
        print("NO2", "Sør-Norge")
        print("NO3", "Midt-Norge")
        print("NO4", "Nord-Norge")
        print("NO5", "Vest-Norge")
        
        