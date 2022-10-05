from typing import List, Union
from pyrmv.classes.Stop import Stop
from pyrmv.enums.location_type import LocationType
from pyrmv.enums.lang import Language
from pyrmv.enums.selection_mode import SelectionMode
from pyrmv.enums.filter_mode import FilterMode
from pyrmv.raw.stop_by_name import stop_by_name as raw_stop_by_name
from pyrmv.utility.find_exception import find_exception

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

def stop_by_name(
    
        access_id: str,
        query: str,

        lang: Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR] = Language.EN,
        max_number: int = 10,
        stop_type: Literal[LocationType.A, LocationType.ALL, LocationType.AP, LocationType.P, LocationType.S, LocationType.SA, LocationType.SP] = LocationType.ALL,
        selection_mode: Literal[SelectionMode.SLCT_A, SelectionMode.SLCT_N] = None, # type: ignore
        coord_lat: Union[str, float] = None, # type: ignore
        coord_lon: Union[str, float] = None, # type: ignore
        radius: Union[int, float] = 1000,
        refine_id: str = None, # type: ignore
        stations: Union[str, list] = None, # type: ignore
        filter_mode: Literal[FilterMode.DIST_PERI, FilterMode.EXCL_PERI, FilterMode.SLCT_PERI] = FilterMode.DIST_PERI
    ) -> List[Stop]:
    """Method can be used to perform a pattern matching of a user input and to retrieve a list
    of possible matches in the journey planner database. Possible matches might be stops/stations,
    points of interest and addresses.  

    More detailed request is available as `raw.stop_by_name()`, however returns `dict` instead of `List[Stop]`.  

    ### Args:
        * access_id (`str`): Access ID for identifying the requesting client. Get your key on [RMV website](https://opendata.rmv.de/site/start.html).
        * query (`str`): Search for that token.
        * lang (`Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR]`, **optional**): The language of response. Defaults to `Language.EN`.
        * max_number (`int`, **optional**): Maximum number of returned stops. In range 1-1000. Defaults to `10`.
        * stop_type (`Literal[LocationType.A, LocationType.ALL, LocationType.AP, LocationType.P, LocationType.S, LocationType.SA, LocationType.SP]`, **optional**): Type filter for location types. Defaults to `LocationType.ALL`.
        * selection_mode (`Literal[SelectionMode.SLCT_A, SelectionMode.SLCT_N]`, **optional**): Selection mode for locations. `SelectionMode.SLCT_N`: Not selectable, `SelectionMode.SLCT_A`: Selectable. Defaults to `None`.
        * coord_lat (`Union[str, float]`, **optional**): Latitude of centre coordinate. Defaults to `None`.
        * coord_lon (`Union[str, float]`, **optional**): Longitude of centre coordinate. Defaults to `None`.
        * radius (`Union[int, float]`, **optional**): Search radius in meter around the given coordinate if any. Defaults to `1000`.
        * refine_id (`str`, **optional**): In case of an refinable location, this value takes the ID of the refinable one of a previous result. Defaults to `None`.
        * stations (`Union[str, list]`, **optional**): Filter for stations. Matches if the given value is prefix of any station in the itinerary. As a list or as a string separated by comma. Defaults to `None`.
        * filter_mode (`Literal[FilterMode.DIST_PERI, FilterMode.EXCL_PERI, FilterMode.SLCT_PERI]`, **optional**): Filter modes for nearby searches. Defaults to `FilterMode.DIST_PERI`.

    ### Returns:
        * List[Stop]: List of Stop objects. Empty list if none found.
    """    

    if selection_mode == None:
        selection_mode = None
    else:
        selection_mode = selection_mode.code

    stops = []
    stops_raw = raw_stop_by_name(
        accessId=access_id,
        inputString=query,
        lang=lang.code,
        maxNo=max_number,
        stopType=stop_type.code,
        locationSelectionMode=selection_mode,
        coordLat=coord_lat,
        coordLong=coord_lon,
        radius=radius,
        refineId=refine_id,
        stations=stations,
        filterMode=filter_mode.code
    )

    find_exception(stops_raw)

    for stop in stops_raw["stopLocationOrCoordLocation"]:
        if "StopLocation" in stop:
            stops.append(Stop(stop["StopLocation"]))
        elif "CoordLocation" in stop:
            stops.append(Stop(stop["CoordLocation"]))

    return stops