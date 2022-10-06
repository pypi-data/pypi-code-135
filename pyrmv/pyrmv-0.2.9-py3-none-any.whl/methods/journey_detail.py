from datetime import datetime
from typing import Union
from pyrmv.classes.Journey import Journey
from pyrmv.enums.rt_mode import RealTimeMode
from pyrmv.raw.journey_detail import journey_detail as raw_journey_detail
from pyrmv.utility.find_exception import find_exception

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

def journey_detail(

        access_id: str,
        id: str,
        date: Union[str, datetime] = None, # type: ignore
        real_time_mode: Literal[RealTimeMode.FULL, RealTimeMode.INFOS, RealTimeMode.OFF, RealTimeMode.REALTIME, RealTimeMode.SERVER_DEFAULT] = None, # type: ignore
        from_id: str = None, # type: ignore
        from_index: int = None, # type: ignore
        to_id: str = None, # type: ignore
        to_index: int = None # type: ignore
    ) -> Journey:
    """The journey_detail method will deliver information about the complete route of a vehicle. The journey
    identifier is part of a trip or `board_departure()` response. It contains a list of all stops/stations of this journey
    including all departure and arrival times (with real-time data if available) and additional information like
    specific attributes about facilities and other texts.  

    More detailed request is available as `raw.journey_detail()`, however returns `dict` instead of `Journey`.

    ### Args:
        * access_id (`str`): Access ID for identifying the requesting client. Get your key on [RMV website](https://opendata.rmv.de/site/start.html).
        * id (`str`): Specifies the internal journey id of the journey shall be retrieved. Maximum length 512.
        * date (`Union[str, datetime]`, **optional**): Day of operation. Represented in the format `YYYY-MM-DD` or as a datetime object. By default the current server date is used. Defaults to `None`.
        * real_time_mode (`Literal[RealTimeMode.FULL, RealTimeMode.INFOS, RealTimeMode.OFF, RealTimeMode.REALTIME, RealTimeMode.SERVER_DEFAULT]`, **optional**): Set the realtime mode to be used. Read more about this in HAFAS ReST Documentation. Defaults to `None`.
        * from_id (`str`, **optional**): Specifies the station/stop ID the partial itinerary shall start from. Defaults to `None`.
        * from_index (`int`, **optional**): Specifies the station/stop index the partial itinerary shall start from. Defaults to `None`.
        * to_id (`str`, **optional**): Specifies the station/stop ID the partial itinerary shall end at. Defaults to `None`.
        * to_index (`int`, **optional**): Specifies the station/stop index the partial itinerary shall end at. Defaults to `None`.

    ### Returns:
        * Journey: Instance of Journey object.
    """    

    if real_time_mode == None:
        real_time_mode = None
    else:
        real_time_mode = real_time_mode.code

    journey_raw = raw_journey_detail(
        accessId=access_id,
        id=id,
        date=date,
        rtMode=real_time_mode,
        fromId=from_id,
        fromIdx=from_index,
        toId=to_id,
        toIdx=to_index
    )

    find_exception(journey_raw)

    return Journey(journey_raw)