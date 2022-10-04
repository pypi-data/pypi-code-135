import asyncio
import aiohttp
import xmltodict
import re


async def get_devices(httpsession, wunda_ip, wunda_user, wunda_pass):
    """ Returns a list of active devices connected to the Wundasmart controller """

    devices = []

    """ Query the getdevices API, which returns a list of all devices connected to the controller. Data is formatted in XML """
    wunda_url = f"http://{wunda_ip}/getdevices.cgi" 
    try: 
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status

        if status == 200:
            device_serials = {}
            data = await resp.text()
            xml_data = xmltodict.parse(data)
            for device in xml_data["devices"]["dev"]:
                if '@sn' in device: # Filter out inactive devices by only returning entries that have a serial number
                    device_type = device["@type"]
                    device_serials[str(device['@id'])] = device['@sn']
                    device_name = device["@type"] + "-" + device["@id"] # Since devices don't have friendly names, generate one automatically
                    if re.match(r"BT", device_type): # Thermostats return temp, humidity, and device status
                        devices.append(
                            {
                                "i"              : device['@id'],
                                "n"              : device_name,
                                "type"           : device_type,
                                "sn"             : device['@sn'],
                                "characteristics": [ "ver", "t", "h", "bat", "sig", "alarm" ]
                            }
                        )
                    elif re.match(r"TH", device_type): # TRVs return temp and device status
                        devices.append(
                            {
                                "i"              : device['@id'],
                                "n"              : device_name,
                                "type"           : device_type,
                                "sn"             : device['@sn'],
                                "characteristics": [ "ver", "t", "bat", "sig", "alarm" ]
                            }
                        )
                    elif re.match(r"HB", device_type): # UFH controllers only return device status  
                        devices.append(
                            {
                                "i"              : device['@id'],
                                "n"              : device_name,
                                "type"           : device_type,
                                "sn"             : device['@sn'],
                                "characteristics": [ "ver", "bat", "sig", "alarm" ]
                            }
                        )
        else:
            return {"state": False, "code": status}
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return {"state": False, "code": 500}

    """ Query the cmd API, which returns a list of rooms configured on the controller. Data is formatted in JSON """
    wunda_url = f"http://{wunda_ip}/cmd.cgi"
    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status

        if status == 200:
            data = await resp.json()
            for room in data["rooms"]:
                devices.append(
                    {
                        "i"              : room["i"],
                        "type"           : "ROOM",
                        "sn"             : room["n"], # since rooms don't have a serial number, we use the room name instead
                        "n"              : room["n"].replace("%20", " "),
                        "characteristics": ["t", "h", "sp", "tp"]
                    }
                )
        else:
            return {"state": False, "code": status}
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return {"state": False, "code": 500}

    return {"state": True, "devices": devices}


async def get_states(httpsession, wunda_ip, wunda_user, wunda_pass):
    """ Returns a full list of metrics from the Wundasmart controller """

    states = []

    """ Since only the getdevices API provides serial numbers, first we need to query that """
    wunda_url = f"http://{wunda_ip}/getdevices.cgi"
    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status

        if status == 200:
            device_serials = {}
            data = await resp.text()
            xml_data = xmltodict.parse(data)
            for device in xml_data["devices"]["dev"]:
                if '@sn' in device:
                    device_serials[str(device['@id'])] = device['@sn']
        else:
            return []
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return []

    """ Query the cmd API to get climate data for each room """
    wunda_url = f"http://{wunda_ip}/cmd.cgi"
    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status
        if status == 200:
            data = await resp.json()
            for room_state in data["rooms"]:
                states.append(
                    {
                        "i": room_state["i"],
                        "sn": room_state["n"], # since rooms don't have a serial number, we use the room name instead
                        "state": {
                            "t": room_state["t"], # temperature
                            "h": room_state["h"], # humidity
                            "sp": room_state["sp"], # set point
                            "tp": room_state["tp"] # temperature mode
                        }
                    }
                )
        else:
            return []
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return []

    """ Query the syncvalues API to get sensor data from each device """
    wunda_url = f"http://{wunda_ip}/syncvalues.cgi?v=2"
    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status
        if status == 200:
            data = await resp.text()
            for device_state in data.splitlines():
                device_state_split = dict(x.split(":") for x in device_state.split(";") if ":" in x)
                if ('s', '1') in device_state_split.items():
                        i = device_state.split(";")[0]
                        if i in device_serials:  # only process devices where we know the serial
                            device_type = device_state_split["t"]
                            if re.match(r"^BT", device_type):
                                states.append (
                                    {
                                        "i"     : device_state.split(";")[0],
                                        "sn"    : device_serials[i],
                                        "state" : {
                                            "ver": device_state_split["v"],
                                            "t": device_state_split["temp"],
                                            "h": device_state_split["rh"],
                                            "bat": device_state_split["bat"],
                                            "sig": device_state_split["sig"],
                                            "alarm": device_state_split["alarm"]
                                        }
                                    }
                                )
                            elif re.match(r"^TH", device_type):
                                states.append (
                                    {
                                        "i"     : device_state.split(";")[0],
                                        "sn"    : device_serials[i],
                                        "state" : {
                                            "ver": device_state_split["v"],
                                            "t": device_state_split["vtemp"],
                                            "bat": device_state_split["bat"],
                                            "sig": device_state_split["sig"],
                                            "alarm": device_state_split["alarm"]
                                        }
                                    }
                                )
                            elif re.match(r"^HB", device_type):
                                states.append (
                                    {
                                        "i"     : device_state.split(";")[0],
                                        "sn"    : device_serials[i],
                                        "state" : {
                                            "ver": device_state_split["v"],
                                            "bat": device_state_split["bat"],
                                            "sig": device_state_split["sig"],
                                            "alarm": device_state_split["alarm"]
                                        }
                                    }
                                )
        else:
            return []
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return []

    return states

async def put_state(httpsession, wunda_ip, wunda_user, wunda_pass, deviceid, params):
    wunda_url = f"http://{wunda_ip}/cmd.cgi"
    try:
        params.append(("i", id))
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass), params=params
        )
        status = resp.status
        if status == 200:
            data = await resp.json()
            for room in data["rooms"]:
                if room["i"] == deviceid:
                    state = {
                        "t": room["t"],
                        "h": room["h"],
                        "sp": room["sp"],
                        "tp": room["tp"],
                    }
                    return state
        return {}
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return {}

