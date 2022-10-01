import time
import requests
from netatmoapi.client import Client


class URL:
    TOKEN = "https://api.netatmo.com/oauth2/token"
    AUTHORIZE = "https://api.netatmo.com/oauth2/authorize"
    HOMESDATA = "https://api.netatmo.com/api/homesdata"
    HOMESTATUS = "https://api.netatmo.com/api/homestatus"
    SETSTATE = "https://api.netatmo.com/api/setstate"
    GETSCENARIOS = "https://api.netatmo.com/api/getscenarios"
    GETROOMMEASURE = "https://api.netatmo.com/api/getroommeasure"
    SETTHERMMODE = "https://api.netatmo.com/api/setthermmode"
    GETMEASURE = "https://api.netatmo.com/api/getmeasure"
    GETEVENTS = "https://api.netatmo.com/api/getevents"
    SETPERSONSAWAY = "https://api.netatmo.com/api/setpersonsaway"
    SETPERSONSHOME = "https://api.netatmo.com/api/setpersonshome"
    ADDWEBHOOK = "https://api.netatmo.com/api/addwebhook"
    DROPWEBHOOK = "https://api.netatmo.com/api/dropwebhook"
    SETROOMTHERMPOINT = "https://api.netatmo.com/api/setroomthermpoint"
    SYNCHOMESCHEDULE = "https://api.netatmo.com/api/synchomeschedule"
    SWITCHHOMESCHEDULE = "https://api.netatmo.com/api/switchhomeschedule"
    GETPUBLICDATA = "https://api.netatmo.com/api/getpublicdata"
    GETSTATIONSDATA = "https://api.netatmo.com/api/getstationsdata"
    GETHOMECOACHSDATA = "https://api.netatmo.com/api/gethomecoachsdata"


class Station:

    """_summary_

    Returns:
        _type_: _description_
    """

    class Aircare:

        """_summary_"""

        def __init__(self, client: Client) -> None:
            self.client = client

        def gethomecoachsdata(self, device_id: str) -> requests.Response:

            """_summary_

            Args:
                device_id (str): _description_

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.GETHOMECOACHSDATA,
                params={
                    "access_token": self.client.access_token,
                    "device_id": device_id,
                },
            )

    class Control:

        """_summary_"""

        def __init__(self, client: Client) -> None:
            self.client = client

        def homesdata(
            self, home_id: str = None, gateway_types: list[str] = None
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str, optional): _description_. Defaults to None.
                gateway_types (list[str], optional): _description_. Defaults to None.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.HOMESDATA,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "gateway_types": gateway_types,
                },
            )

        def homestatus(
            self, home_id: str, device_types: list[str] = None
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str): _description_
                device_types (list[str], optional): _description_. Defaults to None.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.HOMESTATUS,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "device_types": device_types,
                },
            )

        def setstate(self, json: dict) -> requests.Response:

            """_summary_

            Args:
                json (dict): _description_

            Returns:
                requests.Response: _description_
            """

            return requests.post(
                URL.SETSTATE,
                params={"access_token": self.client.access_token},
                json=json,
            )

        def getscenarios(self, home_id: str) -> dict:
            return requests.get(
                URL.GETSCENARIOS,
                params={"access_token": self.client.access_token, "home_id": home_id},
            )

        def getroommeasure(
            self,
            home_id: str,
            room_id: str,
            scale: str,
            type: str,
            date_begin: int = 0,
            date_end: int = time.time(),
            limit: int = 1024,
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str): _description_
                room_id (str): _description_
                scale (str): _description_
                type (str): _description_
                date_begin (int, optional): _description_. Defaults to 0.
                date_end (int, optional): _description_. Defaults to time.time().
                limit (int, optional): _description_. Defaults to 1024.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.GETROOMMEASURE,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "room_id": room_id,
                    "scale": scale,
                    "type": type,
                    "date_begin": date_begin,
                    "date_end": date_end,
                    "limit": limit,
                },
            )

        def setthermmode(
            self, home_id: str, mode: str, endtime: int = None
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str): _description_
                mode (str): _description_
                endtime (int, optional): _description_. Defaults to None.

            Returns:
                requests.Response: _description_
            """

            return requests.post(
                URL.SETTHERMMODE,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "mode": mode,
                    "endtime": endtime,
                },
            )

        def getmeasure(
            self,
            device_id: str,
            module_id: str,
            scale: str,
            type: list[str],
            date_begin: int = 0,
            date_end: int = time.time(),
        ) -> requests.Response:

            """_summary_

            Args:
                device_id (str): _description_
                module_id (str): _description_
                scale (str): _description_
                type (list[str]): _description_
                date_begin (int, optional): _description_. Defaults to 0.
                date_end (int, optional): _description_. Defaults to time.time().

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.GETMEASURE,
                params={
                    "access_token": self.client.access_token,
                    "device_id": device_id,
                    "module_id": module_id,
                    "scale": scale,
                    "type": type,
                    "date_begin": date_begin,
                    "date_end": date_end,
                },
            )

    class Energy:

        """_summary_"""

        def __init__(self, client: Client) -> None:
            self.client = client

        def homesdata(
            self, home_id: str = None, gateway_types: list[str] = None
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str, optional): _description_. Defaults to None.
                gateway_types (list[str], optional): _description_. Defaults to None.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.HOMESDATA,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "gateway_types": gateway_types,
                },
            )

        def homestatus(
            self, home_id: str, device_types: list[str] = None
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str): _description_
                device_types (list[str], optional): _description_. Defaults to None.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.HOMESTATUS,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "device_types": device_types,
                },
            )

        def getroommeasure(
            self,
            home_id: str,
            room_id: str,
            scale: str,
            type: str,
            date_begin: int = 0,
            date_end: int = time.time(),
            limit: int = 1024,
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str): _description_
                room_id (str): _description_
                scale (str): _description_
                type (str): _description_
                date_begin (int, optional): _description_. Defaults to 0.
                date_end (int, optional): _description_. Defaults to time.time().
                limit (int, optional): _description_. Defaults to 1024.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.GETROOMMEASURE,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "room_id": room_id,
                    "scale": scale,
                    "type": type,
                    "date_begin": date_begin,
                    "date_end": date_end,
                    "limit": limit,
                },
            )

        def setroomthermpoint(
            self,
            home_id: str,
            room_id: str,
            mode: str,
            temp: int = None,
            endtime: int = None,
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str): _description_
                room_id (str): _description_
                mode (str): _description_
                temp (int, optional): _description_. Defaults to None.
                endtime (int, optional): _description_. Defaults to None.

            Returns:
                requests.Response: _description_
            """

            return requests.post(
                URL.SETROOMTHERMPOINT,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "room_id": room_id,
                    "mode": mode,
                    "temp": temp,
                    "endtime": endtime,
                },
            )

        def setthermmode(
            self, home_id: str, mode: str, endtime: int = None
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str): _description_
                mode (str): _description_
                endtime (int, optional): _description_. Defaults to None.

            Returns:
                requests.Response: _description_
            """

            return requests.post(
                URL.SETTHERMMODE,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "mode": mode,
                    "endtime": endtime,
                },
            )

        def getmeasure(
            self,
            device_id: str,
            module_id: str,
            scale: str,
            type: list[str],
            date_begin: int = 0,
            date_end: int = time.time(),
            limit: int = 1024,
            optimize: bool = True,
            real_time: bool = False,
        ) -> requests.Response:

            """_summary_

            Args:
                device_id (str): _description_
                module_id (str): _description_
                scale (str): _description_
                type (list[str]): _description_
                date_begin (int, optional): _description_. Defaults to 0.
                date_end (int, optional): _description_. Defaults to time.time().
                limit (int, optional): _description_. Defaults to 1024.
                optimize (bool, optional): _description_. Defaults to True.
                real_time (bool, optional): _description_. Defaults to False.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.GETMEASURE,
                params={
                    "access_token": self.client.access_token,
                    "device_id": device_id,
                    "module_id": module_id,
                    "scale": scale,
                    "type": type,
                    "date_begin": date_begin,
                    "date_end": date_end,
                    "limit": limit,
                    "optimize": optimize,
                    "real_time": real_time,
                },
            )

        def synchomeschedule(
            self,
            home_id: str,
            zones: dict,
            timetable: dict,
            hg_temp: int,
            away_temp: int,
            schedule_id: str = None,
            name: str = None,
        ) -> requests.Response:

            """_summary_

            Args:
                home_id (str): _description_
                zones (dict): _description_
                timetable (dict): _description_
                hg_temp (int): _description_
                away_temp (int): _description_
                schedule_id (str, optional): _description_. Defaults to None.
                name (str, optional): _description_. Defaults to None.

            Returns:
                requests.Response: _description_
            """

            return requests.post(
                URL.SYNCHOMESCHEDULE,
                params={
                    "access_token": self.client.access_token,
                    "home_id": home_id,
                    "zones": zones,
                    "timetable": timetable,
                    "hg_temp": hg_temp,
                    "away_temp": away_temp,
                    "schedule_id": schedule_id,
                    "name": name,
                },
            )

        def switchhomeschedule(
            self, schedule_id: str, home_id: str
        ) -> requests.Response:

            """_summary_

            Args:
                schedule_id (str): _description_
                home_id (str): _description_

            Returns:
                requests.Response: _description_
            """

            return requests.post(
                URL.SWITCHHOMESCHEDULE,
                params={
                    "access_token": self.client.access_token,
                    "schedule_id": schedule_id,
                    "home_id": home_id,
                },
            )

    class Weather:

        """_summary_"""

        def __init__(self, client: Client) -> None:
            self.client = client

        def getpublicdata(
            self,
            lat_ne: int,
            lon_ne: int,
            lat_sw: int,
            lon_sw: int,
            required_data: list[str] = None,
            filter: bool = False,
        ) -> requests.Response:

            """_summary_

            Args:
                lat_ne (int): _description_
                lon_ne (int): _description_
                lat_sw (int): _description_
                lon_sw (int): _description_
                required_data (list[str], optional): _description_. Defaults to None.
                filter (bool, optional): _description_. Defaults to False.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.GETPUBLICDATA,
                params={
                    "access_token": self.client.access_token,
                    "lat_ne": lat_ne,
                    "lon_ne": lon_ne,
                    "lat_sw": lat_sw,
                    "lon_sw": lon_sw,
                    "required_data": required_data,
                    "filter": filter,
                },
            )

        def getstationsdata(self, device_id: str) -> requests.Response:

            """_summary_

            Args:
                device_id (str): _description_

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.GETSTATIONSDATA,
                params={
                    "access_token": self.client.access_token,
                    "device_id": device_id,
                },
            )

        def getmeasure(
            self,
            device_id: str,
            scale: str,
            type: list[str],
            module_id: str = None,
            date_begin: int = 0,
            date_end: int = time.time(),
            limit: int = 1024,
            optimize: bool = True,
            real_time: bool = False,
        ) -> requests.Response:

            """_summary_

            Args:
                device_id (str): _description_
                scale (str): _description_
                type (list[str]): _description_
                module_id (str, optional): _description_. Defaults to None.
                date_begin (int, optional): _description_. Defaults to 0.
                date_end (int, optional): _description_. Defaults to time.time().
                limit (int, optional): _description_. Defaults to 1024.
                optimize (bool, optional): _description_. Defaults to True.
                real_time (bool, optional): _description_. Defaults to False.

            Returns:
                requests.Response: _description_
            """

            return requests.get(
                URL.GETMEASURE,
                params={
                    "access_token": self.client.access_token,
                    "device_id": device_id,
                    "module_id": module_id,
                    "scale": scale,
                    "type": type,
                    "date_begin": date_begin,
                    "date_end": date_end,
                    "limit": limit,
                    "optimize": optimize,
                    "real_time": real_time,
                },
            )
