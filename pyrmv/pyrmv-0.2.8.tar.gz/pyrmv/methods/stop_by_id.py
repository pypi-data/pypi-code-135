from typing import List, Union
from pyrmv.classes.Stop import Stop
from pyrmv.enums.lang import Language
from pyrmv.raw.stop_by_name import stop_by_name as raw_stop_by_name
from pyrmv.utility.find_exception import find_exception

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

def stop_by_id(
    
        access_id: str,
        query: str,
        lang: Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR] = Language.EN,
    ) -> Union[Stop, None]:
    """Method can be used to get Stop object whilst only having id available.

    ### Args:
        * access_id (`str`): Access ID for identifying the requesting client. Get your key on [RMV website](https://opendata.rmv.de/site/start.html).
        * query (`str`): Search for that token.
        * lang (`Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR]`, **optional**): The language of response. Defaults to `Language.EN`.
    
    ### Returns:
        * Stop: Instance of Stop object or None if not found.
    """    

    stops_raw = raw_stop_by_name(
        accessId=access_id,
        inputString=query,
        lang=lang.code,
        maxNo=1
    )

    find_exception(stops_raw)

    if len(stops_raw["stopLocationOrCoordLocation"]) > 0:
        stop = stops_raw["stopLocationOrCoordLocation"][0]

        if "StopLocation" in stop:
            return Stop(stop["StopLocation"])
        elif "CoordLocation" in stop:
            return Stop(stop["CoordLocation"])
        else:
            return None
    else:
        return 0