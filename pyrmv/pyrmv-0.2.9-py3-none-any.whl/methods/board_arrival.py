from datetime import datetime, timedelta
from typing import Union
from pyrmv.classes.Board import BoardArrival
from pyrmv.classes.Stop import Stop, StopTrip
from pyrmv.enums.board_type import BoardArrivalType
from pyrmv.raw import board_arrival as raw_board_arrival
from pyrmv.utility.find_exception import find_exception

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

def board_arrival(
    
        access_id: str,
        id: str = None, # type: ignore
        id_ext: str = None, # type: ignore
        direction: Union[str, Stop, StopTrip] = None, # type: ignore
        date: Union[str, datetime] = None, # type: ignore
        time: Union[str, datetime] = None, # type: ignore
        duration: Union[int, timedelta] = 60,
        journeys_max: int = -1,
        operators: Union[str, list] = None, # type: ignore
        lines: Union[str, list] = None, # type: ignore
        passlist: bool = False,
        board_type: Literal[BoardArrivalType.ARR, BoardArrivalType.ARR_EQUIVS, BoardArrivalType.ARR_MAST, BoardArrivalType.ARR_STATION] = BoardArrivalType.ARR,
    ) -> BoardArrival:
    """Method returns a board with arriving transport. 

    More detailed request is available as `raw.board_arrival()`, however returns `dict` instead of `Board`.

    ### Args:
        * access_id (`str`): Access ID for identifying the requesting client. Get your key on [RMV website](https://opendata.rmv.de/site/start.html).
        * id (`str`, **optional**): Specifies the station/stop ID. Such ID can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
        * id_ext (`str`, **optional**): Deprecated. Please use `id` as it supports external IDs. Specifies the external station/stop ID. Such ID can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
        * direction (`Union[str, Stop, StopTrip]`, **optional**): If only vehicles departing or arriving from a certain direction shall be returned, specify the direction by giving the station/stop ID of the last stop on the journey or the Stop object itself. Defaults to `None`.
        * date (`Union[str, datetime]`, **optional**): Sets the start date for which the departures shall be retrieved. Represented in the format YYYY-MM-DD or as a datetime object. By default the current server date is used. Defaults to `None`.
        * time (`Union[str, datetime]`, **optional**): Sets the start time for which the departures shall be retrieved. Represented in the format hh:mm[:ss] in 24h nomenclature or as a datetime object. Seconds will be ignored for requests. By default the current server time is used. Defaults to `None`.
        * duration (`Union[int, timedelta]`, **optional**): Set the interval size in minutes. Can also be provided as a timedelta. Defaults to `60`.
        * journeys_max (`int`, **optional**): Maximum number of journeys to be returned. If no value is defined or -1, all departing/arriving services within the duration sized period are returned. Defaults to `-1`.
        * operators (`Union[str, list]`, **optional**): Only journeys provided by the given operators are part of the result. To filter multiple operators, separate the codes by comma or provide a list. If the operator should not be part of the be trip, negate it by putting ! in front of it. Example: Filter for operator A and B: `operators=[A,B]`. Defaults to `None`.
        * lines (`Union[str, list]`, **optional**): Only journeys running the given line are part of the result. To filter multiple lines, provide a list or separate the codes by comma or provide a list. If the line should not be part of the be trip, negate it by putting ! in front of it. Defaults to `None`.
        * passlist (`bool`, **optional**): Include a list of all passed waystops. Defaults to `False`.
        * board_type (`Union[BoardArrivalType.ARR, BoardArrivalType.ARR_EQUIVS, BoardArrivalType.ARR_MAST, BoardArrivalType.ARR_STATION]`, optional): Set the station arrival board type to be used. Defaults to `BoardArrivalType.ARR`.

    ### Returns:
        * BoardArrival: Instance of BoardArrival object.
    """

    if (isinstance(direction, Stop) or isinstance(direction, StopTrip)):
        direction = direction.id

    board_raw = raw_board_arrival(
        accessId=access_id,
        id=id,
        extId=id_ext,
        direction=direction,
        date=date,
        time=time,
        duration=duration,
        maxJourneys=journeys_max,
        operators=operators,
        lines=lines,
        passlist=passlist,
        boardType=board_type.code
    )

    find_exception(board_raw)

    return BoardArrival(board_raw, access_id)