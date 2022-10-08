from datetime import datetime
from typing import final
import pytz

class Common():
    
    def __init__(self) -> None:
        pass
    
    def getNorwayTime(self) -> datetime:
        return datetime.now(pytz.timezone('Europe/Oslo'))