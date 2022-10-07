from datetime import datetime, timedelta
from typing import List, OrderedDict, Union
from pyrmv.classes import *
from pyrmv.enums import *
from pyrmv.raw import board_arrival as raw_board_arrival
from pyrmv.raw.board_departure import board_departure as raw_board_departure
from pyrmv.raw.journey_detail import journey_detail as raw_journey_detail
from pyrmv.raw.stop_by_name import stop_by_name as raw_stop_by_name
from pyrmv.raw.stop_by_coords import stop_by_coords as raw_stop_by_coords
from pyrmv.raw.trip_find import trip_find as raw_trip_find
from pyrmv.raw.trip_recon import trip_recon as raw_trip_recon
from pyrmv.raw.him_search import him_search as raw_him_search
from pyrmv.utility.find_exception import find_exception
from pyrmv.errors.not_ready import NotReadyYetError

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

class Client():

    def __init__(self, access_id: str) -> None:
        self.access_id = access_id

    def board_arrival(self,
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
            * BoardArrival: Instance of `BoardArrival` object.
        """

        if (isinstance(direction, Stop) or isinstance(direction, StopTrip)):
            direction = direction.id

        board_raw = raw_board_arrival(
            accessId=self.access_id,
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

        return BoardArrival(board_raw, self)

    def board_departure(self,
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
            board_type: Literal[BoardDepartureType.DEP, BoardDepartureType.DEP_EQUIVS, BoardDepartureType.DEP_MAST, BoardDepartureType.DEP_STATION] = BoardDepartureType.DEP,
        ) -> BoardDeparture:
        """Method returns a board with departing transport. 

        More detailed request is available as `raw.board_departure()`, however returns `dict` instead of `Board`.

        ### Args:
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
            * board_type (`Union[BoardDepartureType.DEP, BoardDepartureType.DEP_EQUIVS, BoardDepartureType.DEP_MAST, BoardDepartureType.DEP_STATION]`, optional): Set the station departure board type to be used. Defaults to `BoardDepartureType.DEP`.

        ### Returns:
            * BoardDeparture: Instance of `BoardDeparture` object.
        """

        if (isinstance(direction, Stop) or isinstance(direction, StopTrip)):
            direction = direction.id

        board_raw = raw_board_departure(
            accessId=self.access_id,
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

        return BoardDeparture(board_raw, self)

    def him_search(self,
            date_begin: Union[str, datetime] = None,
            date_end: Union[str, datetime] = None,
            time_begin: Union[str, datetime] = None,
            time_end: Union[str, datetime] = None,
            weekdays: Union[str, OrderedDict[str, bool]] = None,
            ids: list = None,
            operators: list = None,
            categories: list = None,
            channels: list = None,
            companies: list = None,
            lines: list = None,
            line_ids: list = None,
            stations: Union[list, List[Stop]] = None,
            station_from: Union[str, Stop] = None,
            station_to: Union[str, Stop] = None,
            both_ways: bool = None,
            train_names: list = None,
            search_mode: Literal[SearchMode.MATCH, SearchMode.NOMATCH, SearchMode.TFMATCH] = None,
            affected_journey_mode: Literal[AffectedJourneyMode.ALL, AffectedJourneyMode.OFF] = None,
            affected_journey_stop_mode: Literal[AffectedJourneyStopMode.ALL, AffectedJourneyStopMode.IMP, AffectedJourneyStopMode.OFF] = None,
            priority_min: int = None,
            priority_max: int = None
        ) -> List[Message]:
        """The him_search method will deliver a list of HIM messages if matched by the given criteria as
        well as affected products if any.  

        More detailed request is available as `raw.him_search()`, however returns `dict` instead of `List[Message]`.  

        ### Args:
            * date_begin (`Union[str, datetime]`, optional): Sets the event period start date. Defaults to `None`.
            * date_end (`Union[str, datetime]`, optional): Sets the event period end date. Defaults to `None`.
            * time_begin (`Union[str, datetime]`, optional): Sets the event period start time. Defaults to `None`.
            * time_end (`Union[str, datetime]`, optional): Sets the event period end time. Defaults to `None`.
            * weekdays (`Union[str, OrderedDict[str, bool]]`, optional): Bitmask or an OrderedDict for validity of HIM messages based on weekdays. OrderedDict must be formatted as follows: `OrderedDict(Monday=bool, Tuesday=bool, Wednesday=bool, Thursday=bool, Friday=bool, Saturday=bool, Sunday=bool)`. Each character of a bitmask represents a weekday starting on monday. Example: Only find HIM Messages valid from monday to friday: `1111100`. Defaults to `None`.
            * ids (`list`, optional): List of HIM message IDs as a list or separated by comma. Defaults to `None`.
            * operators (`list`, optional): List of operators as a list or separated by comma. Defaults to `None`.
            * categories (`list`, optional): List of train categories as a list or separated by comma. Defaults to `None`.
            * channels (`list`, optional): List of channels as a list or separated by comma. Defaults to `None`.
            * companies (`list`, optional): List of companies as a list or separated by comma. Defaults to `None`.
            * lines (`list`, optional): Only HIM messages for the given line are part of the result. To filter multiple lines, provide them as a list or separate the codes by comma. Defaults to `None`.
            * line_ids (`list`, optional): Only HIM messages for the given line (identified by its line ID) are part of the result. To filter multiple lines, provide them as a list or separate the line IDs by comma. Defaults to `None`.
            * stations (`Union[list, List[Stop]]`, optional): List of (external) station ids or a list of `Stop` objects to be filtered for as a list or separated by comma. Defaults to `None`.
            * station_from (`Union[str, Stop]`, optional): Filter messages by line segment starting at this station given as (external) station id or as a `Stop` object. Defaults to `None`.
            * station_to (`Union[str, Stop]`, optional): Filter messages by line segment travelling in direction of this station given as (external) station id or as a `Stop` object. Defaults to `None`.
            * both_ways (`bool`, optional): If enabled, messages in both directions - from 'station_from' to 'station_to' as well as from 'station_to' to 'station_from' are returned. Defaults to `None`.
            * train_names (`list`, optional): List of train name to be filtered for seperated by comma. Defaults to `None`.
            * search_mode (`Literal[SearchMode.MATCH, SearchMode.NOMATCH, SearchMode.TFMATCH]`, optional): HIM search mode. `SearchMode.NOMATCH` iterate over all HIM messages available. `SearchMode.MATCH` iterate over all trips to find HIM messages. `SearchMode.TFMATCH` uses filters defined `metas` parameter. Defaults to `None`.
            * affected_journey_mode (`Literal[AffectedJourneyMode.ALL, AffectedJourneyMode.OFF]`, optional): Define how to return affected journeys `AffectedJourneyMode.OFF`: do not return affected journeys. `AffectedJourneyMode.ALL`: return affected journeys. Defaults to `None`.
            * affected_journey_stop_mode (`Literal[AffectedJourneyStopMode.ALL, AffectedJourneyStopMode.IMP, AffectedJourneyStopMode.OFF]`, optional): Define how to return stops of affected journeys. `AffectedJourneyStopMode.IMP`: return important stops of affected journeys. `AffectedJourneyStopMode.OFF`: do not return stops of affected journeys. `AffectedJourneyStopMode.ALL`: return all affected stops of affected journeys. Defaults to `None`.
            * priority_min (`int`, optional): Filter for HIM messages having at least this priority. Defaults to `None`.
            * priority_max (`int`, optional): Filter for HIM messages having this priority as maximum. Defaults to `None`.

        ### Returns:
            * List[Message]: List of `Message` objects. Empty list if none found.
        """        

        if isinstance(station_from, Stop):
            station_from = station_from.ext_id

        if isinstance(station_to, Stop):
            station_to = station_to.ext_id

        if stations != None:
            new_stations = []
            for stop in stations:
                if isinstance(stop, Stop):
                    new_stations.append(stop.ext_id)
                else:
                    new_stations.append(stop)
            stations = new_stations

        if search_mode == None:
            search_mode = None
        else:
            search_mode = search_mode.code

        if affected_journey_mode == None:
            affected_journey_mode = None
        else:
            affected_journey_mode = affected_journey_mode.code

        if affected_journey_stop_mode == None:
            affected_journey_stop_mode = None
        else:
            affected_journey_stop_mode = affected_journey_stop_mode.code

        messages = []
        messages_raw = raw_him_search(
            accessId=self.access_id,
            dateB=date_begin,
            dateE=date_end,
            timeB=time_begin,
            timeE=time_end,
            weekdays=weekdays,
            himIds=ids,
            operators=operators,
            categories=categories,
            channels=channels,
            companies=companies,
            lines=lines,
            lineids=line_ids,
            stations=stations,
            fromstation=station_from,
            tostation=station_to,
            bothways=both_ways,
            trainnames=train_names,
            searchmode=search_mode,
            affectedJourneyMode=affected_journey_mode,
            affectedJourneyStopMode=affected_journey_stop_mode,
            maxprio=priority_max,
            minprio=priority_min
        )

        find_exception(messages_raw)

        for message in messages_raw["Message"]:
            messages.append(Message(message))

        return messages

    def journey_detail(self,
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
            * id (`str`): Specifies the internal journey id of the journey shall be retrieved. Maximum length 512.
            * date (`Union[str, datetime]`, **optional**): Day of operation. Represented in the format `YYYY-MM-DD` or as a datetime object. By default the current server date is used. Defaults to `None`.
            * real_time_mode (`Literal[RealTimeMode.FULL, RealTimeMode.INFOS, RealTimeMode.OFF, RealTimeMode.REALTIME, RealTimeMode.SERVER_DEFAULT]`, **optional**): Set the realtime mode to be used. Read more about this in HAFAS ReST Documentation. Defaults to `None`.
            * from_id (`str`, **optional**): Specifies the station/stop ID the partial itinerary shall start from. Defaults to `None`.
            * from_index (`int`, **optional**): Specifies the station/stop index the partial itinerary shall start from. Defaults to `None`.
            * to_id (`str`, **optional**): Specifies the station/stop ID the partial itinerary shall end at. Defaults to `None`.
            * to_index (`int`, **optional**): Specifies the station/stop index the partial itinerary shall end at. Defaults to `None`.

        ### Returns:
            * Journey: Instance of `Journey` object.
        """    

        if real_time_mode == None:
            real_time_mode = None
        else:
            real_time_mode = real_time_mode.code

        journey_raw = raw_journey_detail(
            accessId=self.access_id,
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

    def stop_by_coords(self,
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
            * coords_lat (`Union[str, float]`): Latitude of centre coordinate.
            * coords_lon (`Union[str, float]`): Longitude of centre coordinate.
            * lang (`Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR]`, **optional**): The language of response. Defaults to `Language.EN`.
            * radius (`Union[int, float]`, **optional**): Search radius in meter around the given coordinate if any. Defaults to `1000`.
            * max_number (`int`, **optional**): Maximum number of returned stops. Defaults to `10`.
            * stop_type (`Literal[LocationType.S, LocationType.P, LocationType.SP, LocationType.SE, LocationType.SPE]`, **optional**): Type filter for location types. Defaults to `LocationType.S`.
            * selection_mode (`Literal[SelectionMode.SLCT_A, SelectionMode.SLCT_N]`, **optional**): Selection mode for locations. `SelectionMode.SLCT_N`: Not selectable, `SelectionMode.SLCT_A`: Selectable. Defaults to `None`.

        ### Returns:
            * List[Stop]: List of `Stop` objects. Empty list if none found.
        """    

        if selection_mode == None:
            selection_mode = None
        else:
            selection_mode = selection_mode.code

        stops = []
        stops_raw = raw_stop_by_coords(
            accessId=self.access_id,
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

    def stop_by_id(self,
            query: str,
            lang: Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR] = Language.EN,
        ) -> Union[Stop, None]:
        """Method can be used to get Stop object whilst only having id available.

        ### Args:
            * query (`str`): Search for that token.
            * lang (`Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR]`, **optional**): The language of response. Defaults to `Language.EN`.
        
        ### Returns:
            * Stop: Instance of `Stop` object or `None` if not found.
        """    

        stops_raw = raw_stop_by_name(
            accessId=self.access_id,
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
            return None

    def stop_by_name(self,
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
            * List[Stop]: List of `Stop` objects. Empty list if none found.
        """    

        if selection_mode == None:
            selection_mode = None
        else:
            selection_mode = selection_mode.code

        stops = []
        stops_raw = raw_stop_by_name(
            accessId=self.access_id,
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

    def trip_find(self,
            lang: Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR] = Language.EN,

            origin_id: str = None, # type: ignore
            origin_id_ext: str = None, # type: ignore
            origin_coord_lat: Union[str, float] = None, # type: ignore
            origin_coord_lon: Union[str, float] = None, # type: ignore
            origin_coord_name: str = None, # type: ignore

            destination_id: str = None, # type: ignore
            destination_id_ext: str = None, # type: ignore
            destination_coord_lat: Union[str, float] = None, # type: ignore
            destination_coord_lon: Union[str, float] = None, # type: ignore
            destination_coord_name: str = None, # type: ignore

            via: str = None, # type: ignore
            via_id: str = None, # type: ignore
            via_gis: str = None, # type: ignore
            via_wait_time: int = 0,

            avoid: str = None, # type: ignore
            avoid_id: str = None, # type: ignore

            change_time_percent: int = 100,
            change_time_min: int = None, # type: ignore
            change_time_max: int = None, # type: ignore
            change_time_add: int = None, # type: ignore
            change_max: int = None, # type: ignore

            date: Union[str, datetime] = None, # type: ignore
            time: Union[str, datetime] = None, # type: ignore
            
            search_arrival: bool = False,

            trips_after_time: int = None, # type: ignore
            trips_before_time: int = None, # type: ignore

            context: str = None, # type: ignore

            passlist: bool = False,
            operators: Union[str, list] = None, # type: ignore
            
            lines: Union[str, list] = None, # type: ignore
            lineids: Union[str, list] = None, # type: ignore

            iv_include: bool = False,
            iv_only: bool = False,
            
            bike_carriage: bool = False,

            passing_points: bool = False,

            real_time_mode: Literal[RealTimeMode.FULL, RealTimeMode.INFOS, RealTimeMode.OFF, RealTimeMode.REALTIME, RealTimeMode.SERVER_DEFAULT] = None, # type: ignore

            include_earlier: bool = False,
            ict_alternatives: bool = False,
            tariff: bool = None, # type: ignore
            messages: bool = False,
            frequency: bool = True
        ) -> List[Trip]:
        """The trip service calculates a trip from a specified origin to a specified destination. These might be
        stop/station IDs or coordinates based on addresses and points of interest validated by the location service or
        coordinates freely defined by the client.

        More detailed request is available as `raw.trip_find()`, however returns `dict` instead of `List[Trip]`.  

        ### Args:
            * lang (`Literal[Language.DE, Language.DA, Language.EN, Language.ES, Language.FR, Language.HU, Language.IT, Language.NL, Language.NO, Language.PL, Language.SV, Language.TR]`, **optional**): The language of response. Defaults to `Language.EN`.
            * origin_id (`str`, **optional**): Specifies the station/stop ID of the origin for the trip. Such ID can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
            * origin_id_ext (`str`, **optional**): Deprecated. Please use originId as it supports external IDs. Specifies the external station/stop ID of the origin for the trip. Such ID can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
            * origin_coord_lat (`Union[str, float]`, **optional**): Latitude of station/stop coordinate of the trip's origin. The coordinate can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
            * origin_coord_lon (`Union[str, float]`, **optional**): Longitude of station/stop coordinate of the trip's origin. The coordinate can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
            * origin_coord_name (`str`, **optional**): Name of the trip's origin if coordinate cannot be resolved to an address or poi. Defaults to `None`.
            * destination_id (`str`, **optional**): Specifies the station/stop ID of the destination for the trip. Such ID can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
            * destination_id_ext (`str`, **optional**): Deprecated. Please use destId as it supports external IDs. Specifies the external station/stop ID of the destination for the trip. Such ID can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
            * destination_coord_lat (`Union[str, float]`, **optional**): Latitude of station/stop coordinate of the trip's destination. The coordinate can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
            * destination_coord_lon (`Union[str, float]`, **optional**): Longitude of station/stop coordinate of the trip's destination. The coordinate can be retrieved from stop_by_name() or stop_by_coords(). Defaults to `None`.
            * destination_coord_name (`str`, **optional**): Name of the trip's destination if coordinate cannot be resolved to an address or poi. Defaults to `None`.
            * via (`str`, **optional**): Complex structure to provide multiple via points separated by semicolon. This structure is build like this: `viaId|waittime|viastatus|products|direct|sleepingCar|couchetteCoach|attributes`. Read more about this in HAFAS ReST Documentation. Defaults to `None`.
            * via_id (`str`, **optional**): ID of a station/stop used as a via for the trip. Specifying a via station forces the trip search to look for trips which must pass through this station. Such ID can be retrieved from stop_by_name() or stop_by_coords(). If `via` is used, `via_id` and `via_wait_time ` are having no effect. Defaults to `None`.
            * via_gis (`str`, **optional**): Complex structure to provide multiple GIS via locations separated by semicolon. This structure is build like this: `locationId|locationMode|transportMode|placeType|usageType|mode|durationOfStay`. Read more about this in HAFAS ReST Documentation. Defaults to `None`.
            * via_wait_time (`int`, **optional**): Defines the waiting time spent at via station in minutes. If `via` is used, `via_id` and `via_wait_time` are having no effect. Defaults to 0.
            * avoid (`str`, **optional**): Complex structure to provide multiple points to be avoided separated by semicolon. This structure is build like this: `avoidId|avoidstatus` avoidId: id, extId or altId of the avoid, mandatory avoidstatus: one of NPAVM (do not run through if this is a meta station), NPAVO (do not run through), NCAVM (do not change if this is a meta station), NCAVO (do not change), optional but defaults to NCAVM Example: Just define three avoids by extId: `avoid="801234;801235;801236"`. Defaults to `None`.
            * avoid_id (`str`, **optional**): ID of a station/stop to be avoided as transfer stop for the trip. Such ID can be retrieved from stop_by_name() or stop_by_coords(). If `avoid` is used, `avoid_id` has no effect. Defaults to `None`.
            * change_time_percent (`int`, **optional**): Configures the walking speed when changing from one leg of the journey to the next one. It extends the time required for changes by a specified percentage. A value of 200 doubles the change time as initially calculated by the system. In the response, change time is presented in full minutes. If the calculation based on changeTime-Percent does not result in a full minute, it is rounded using "round half up" method. Defaults to `100`.
            * change_time_min (`int`, **optional**): Minimum change time at stop in minutes. Defaults to `None`.
            * change_time_max (`int`, **optional**): Maximum change time at stop in minutes. Defaults to `None`.
            * change_time_add (`int`, **optional**): This amount of minutes is added to the change time at each stop. Defaults to `None`.
            * change_max (`int`, **optional**): Maximum number of changes. In range 0-11. Defaults to `None`.
            * date (`Union[str, datetime]`, **optional**): Sets the start date for which the departures shall be retrieved. Represented in the format `YYYY-MM-DD` or as a datetime object. By default the current server date is used. Defaults to `None`.
            * time (`Union[str, datetime]`, **optional**): Sets the start time for which the departures shall be retrieved. Represented in the format `hh:mm[:ss]` in 24h nomenclature or as a datetime object. Seconds will be ignored for requests. By default the current server time is used. Defaults to `None`.
            * search_arrival (`bool`, **optional**): If set, the date and time parameters specify the arrival time for the trip search instead of the departure time. Defaults to `False`.
            * trips_after_time (`int`, **optional**): Minimum number of trips after the search time. Sum of `trips_after_time` and `trips_before_time` has to be less or equal 6. Read more about this in HAFAS ReST Documentation. In range 1-6. Defaults to `None`.
            * trips_before_time (`int`, **optional**): Minimum number of trips before the search time. Sum of `trips_after_time` and `trips_before_time` has to be less or equal 6. Read more about this in HAFAS ReST Documentation. In range 0-6. Defaults to `None`.
            * context (`str`, **optional**): Defines the starting point for the scroll back or forth operation. Use the scrB value from a previous result to scroll backwards in time and use the scrF value to scroll forth. Defaults to `None`.
            * passlist (`bool`, **optional**): Enables/disables the return of the passlist for each leg of the trip. Defaults to `False`.
            * operators (`Union[str, list]`, **optional**): Only trips provided by the given operators are part of the result. If the operator should not be part of the be trip, negate it by putting ! in front of it. Example: Filter for operator A and B: `operators=["A","B"]`. Defaults to `None`.
            * lines (`Union[str, list]`, **optional**): Only journeys running the given line are part of the result. If the line should not be part of the be trip, negate it by putting ! in front of it. Defaults to `None`.
            * lineids (`Union[str, list]`, **optional**): Only journeys running the given line (identified by its line ID) are part of the result. If the line should not be part of the be trip, negate it by putting ! in front of it. Defaults to `None`.
            * iv_include (`bool`, **optional**): Enables/disables search for individual transport routes. Defaults to `False`.
            * iv_only (`bool`, **optional**): Enables/disables search for individual transport routes only. Defaults to `False`.
            * bike_carriage (`bool`, **optional**): Enables/disables search for trips explicit allowing bike carriage. This will only work in combination with `change_max=0` as those trips are always meant to be direct connections. Defaults to `False`.
            * passing_points (`bool`, **optional**): Enables/disables the return of stops having no alighting and boarding in its passlist for each leg of the trip. Needs passlist enabled. Defaults to `False`.
            * real_time_mode (`Literal[RealTimeMode.FULL, RealTimeMode.INFOS, RealTimeMode.OFF, RealTimeMode.REALTIME, RealTimeMode.SERVER_DEFAULT]`, **optional**): Set the realtime mode to be used. Read more about this in HAFAS ReST Documentation. Defaults to `None`.
            * include_earlier (`bool`, **optional**): Disables search optimization in relation of duration. Defaults to `False`.
            * ict_alternatives (`bool`, **optional**): Enables/disables the search for alternatives with individualized change times (ICT). Defaults to `False`.
            * tariff (`bool`, **optional**): Enables/disables the output of tariff data. The default is configurable via provisioning. Defaults to `None`.
            * messages (`bool`, **optional**): Enables/disables the output of traffic messages. The default is configurable via provisioning. Defaults to `False`.
            * frequency (`bool`, **optional**): Enables/disables the calculation of frequency information. Defaults to `True`.

        ### Returns:
            * List[Trip]: List of `Trip` objects. Empty list if none found.
        """    

        if real_time_mode == None:
            real_time_mode = None
        else:
            real_time_mode = real_time_mode.code

        trips = []
        trips_raw = raw_trip_find(

            accessId=self.access_id,
            lang=lang.code,

            originId=origin_id,
            originExtId=origin_id_ext,
            originCoordLat=origin_coord_lat,
            originCoordLong=origin_coord_lon,
            originCoordName=origin_coord_name,

            destId=destination_id,
            destExtId=destination_id_ext,
            destCoordLat=destination_coord_lat,
            destCoordLong=destination_coord_lon,
            destCoordName=destination_coord_name,

            via=via,
            viaId=via_id,
            viaGis=via_gis,
            viaWaitTime=via_wait_time,

            avoid=avoid,
            avoidId=avoid_id,

            changeTimePercent=change_time_percent,
            minChangeTime=change_time_min,
            maxChangeTime=change_time_max,
            addChangeTime=change_time_add,
            maxChange=change_max,

            date=date,
            time=time,
            
            searchForArrival=search_arrival,

            numF=trips_after_time,
            numB=trips_before_time,

            context=context,

            passlist=passlist,
            operators=operators,
            
            lines=lines,
            lineids=lineids,

            includeIv=iv_include,
            ivOnly=iv_only,
            
            bikeCarriage=bike_carriage,

            showPassingPoints=passing_points,

            rtMode=real_time_mode,

            includeEarlier=include_earlier,
            withICTAlternatives=ict_alternatives,
            tariff=tariff,
            trafficMessages=messages,
            withFreq=frequency
        )

        find_exception(trips_raw)

        for trip in trips_raw["Trip"]:
            trips.append(Trip(trip))

        return trips

    def trip_recon(self,
            context: Union[str, Journey],
            date: Union[str, datetime] = None,
            match_real_time: bool = None,
            enable_replacements: bool = None,
            arrival_dev_lower: int = None,
            arrival_dev_upper: int = None,
            departure_dev_lower: int = None,
            departure_dev_upper: int = None,
            passlist: bool = None,
            passing_points: bool = False,
            real_time_mode: Literal[RealTimeMode.FULL, RealTimeMode.INFOS, RealTimeMode.OFF, RealTimeMode.REALTIME, RealTimeMode.SERVER_DEFAULT] = None,
            tariff: bool = None,
            messages: bool = False
        ) -> List[Trip]:
        """Reconstructing a trip can be achieved using the reconstruction context provided by any trip result in the
        `ctx_recon` attribute of `Trip` object. The result will be a true copy of the original trip search result given
        that the underlying data did not change.  

        More detailed request is available as `raw.trip_recon()`, however returns `dict` instead of `List[Trip]`.  

        ### Args:
            * context (`Union[str, Journey]`): Specifies the reconstruction context.
            * date (`Union[str, datetime]`, **optional**): Sets the start date for which the departures shall be retrieved. Represented in the format `YYYY-MM-DD` or as a datetime object. This parameter will force the service to reconstruct the trip on that specific date. If the trip is not available on that date, because it does not operate, exception SvcNoResultError will be raised. Defaults to `None`.
            * match_real_time (`bool`, **optional**): Whether the realtime type that journeys are based on be considered. Defaults to `None`.
            * enable_replacements (`bool`, **optional**): If set to `True` replaces cancelled journeys with their replacement journeys if possible. Defaults to `None`.
            * arrival_dev_lower (`int`, **optional**): Lower deviation in minutes within interval `[0, 720]` indicating "how much earlier than original arrival". Defaults to `None`.
            * arrival_dev_upper (`int`, **optional**): Upper deviation in minutes within interval `[0, 720]` indicating "how much later than original arrival". Defaults to `None`.
            * departure_dev_lower (`int`, **optional**): Lower deviation in minutes within interval `[0, 720]` indicating "how much earlier than original departure". Defaults to `None`.
            * departure_dev_upper (`int`, **optional**): Upper deviation in minutes within interval `[0, 720]` indicating "how much later than original departure". Defaults to `None`.
            * passlist (`bool`, **optional**): Enables/disables the return of the passlist for each leg of the trip. Defaults to `None`.
            * passing_points (`bool`, **optional**): Enables/disables the return of stops having no alighting and boarding in its passlist for each leg of the trip. Needs passlist parameter enabled. Defaults to `False`.
            * real_time_mode (`Literal[RealTimeMode.FULL, RealTimeMode.INFOS, RealTimeMode.OFF, RealTimeMode.REALTIME, RealTimeMode.SERVER_DEFAULT]`, **optional**): Set the realtime mode to be used. Read more about this in HAFAS ReST Documentation. Defaults to `None`.
            * tariff (`bool`, **optional**): Enables/disables the output of tariff data. The default is configurable via provisioning. Defaults to `None`.
            * messages (`bool`, **optional**): Enables/disables the output of traffic messages. The default is configurable via provisioning. Defaults to `False`.

        ### Returns:
            * List[Trip]: List of `Trip` objects. Empty list if none found.
        """    
        
        if real_time_mode == None:
            real_time_mode = None
        else:
            real_time_mode = real_time_mode.code
        
        if isinstance(context, Trip):
            context = context.ctx_recon

        trips = []
        trips_raw = raw_trip_recon(
            accessId=self.access_id,
            ctx=context,
            date=date,
            matchRtType=match_real_time,
            enableReplacements=enable_replacements,
            arrL=arrival_dev_lower,
            arrU=arrival_dev_upper,
            depL=departure_dev_lower,
            depU=departure_dev_upper,
            passlist=passlist,
            showPassingPoints=passing_points,
            rtMode=real_time_mode,
            tariff=tariff,
            trafficMessages=messages,
        )

        find_exception(trips_raw)

        for trip in trips_raw["Trip"]:
            trips.append(Trip(trip))

        return trips