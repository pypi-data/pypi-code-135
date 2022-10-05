from typing import List, Union
from pyrmv.classes.Stop import Stop
from pyrmv.enums.location_type import LocationType
from pyrmv.enums.lang import Language
from pyrmv.enums.selection_mode import SelectionMode
from pyrmv.raw.stop_by_coords import stop_by_coords as raw_stop_by_coords
from pyrmv.utility.find_exception import find_exception

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

def stop_by_coords(
    
        access_id: str,
        coords_lat: Union[str, float],
        coords_lon: Union[str, float],

        lang: Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR] = Language.EN,
        radius: Union[int, float] = 1000,
        max_number: int = 10,
        stop_type: Literal[LocationType.S, LocationType.P, LocationType.SP, LocationType.SE, LocationType.SPE] = LocationType.S,
        selection_mode: Literal[SelectionMode.SLCT_A, SelectionMode.SLCT_N] = None, # type: ignore
    ) -> List[Stop]:
    """Method returns a list of stops around a given center coordinate.
    The returned results are ordered by their distance to the center coordinate.  

    More detailed request is available as `raw.stop_by_coords()`, however returns `dict` instead of `List[Stop]`.

    ### Args:
        * access_id (`str`): Access ID for identifying the requesting client. Get your key on [RMV website](https://opendata.rmv.de/site/start.html).
        * coords_lat (`Union[str, float]`): Latitude of centre coordinate.
        * coords_lon (`Union[str, float]`): Longitude of centre coordinate.
        * lang (`Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR]`, **optional**): The language of response. Defaults to `Language.EN`.
        * radius (`Union[int, float]`, **optional**): Search radius in meter around the given coordinate if any. Defaults to `1000`.
        * max_number (`int`, **optional**): Maximum number of returned stops. Defaults to `10`.
        * stop_type (`Literal[LocationType.S, LocationType.P, LocationType.SP, LocationType.SE, LocationType.SPE]`, **optional**): Type filter for location types. Defaults to `LocationType.S`.
        * selection_mode (`Literal[SelectionMode.SLCT_A, SelectionMode.SLCT_N]`, **optional**): Selection mode for locations. `SelectionMode.SLCT_N`: Not selectable, `SelectionMode.SLCT_A`: Selectable. Defaults to `None`.

    ### Returns:
        * List[Stop]: List of Stop objects. Empty list if none found.
    """    

    if selection_mode == None:
        selection_mode = None
    else:
        selection_mode = selection_mode.code

    stops = []
    stops_raw = raw_stop_by_coords(
        accessId=access_id,
        originCoordLat=coords_lat,
        originCoordLong=coords_lon,
        lang=lang.code,
        radius=radius,
        maxNo=max_number,
        stopType=stop_type.code,
        locationSelectionMode=selection_mode
    )

    find_exception(stops_raw)

    for stop in stops_raw["stopLocationOrCoordLocation"]:
        if "StopLocation" in stop:
            stops.append(Stop(stop["StopLocation"]))
        elif "CoordLocation" in stop:
            stops.append(Stop(stop["CoordLocation"]))

    return stops