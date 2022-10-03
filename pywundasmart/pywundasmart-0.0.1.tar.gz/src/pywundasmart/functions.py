import asyncio
import aiohttp
import xmltodict
import re


async def get_devices(httpsession, wunda_ip, wunda_user, wunda_pass):
    wunda_url = f"http://{wunda_ip}/getdevices.cgi"
    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status

        if status == 200:
            devices = []
            data = await resp.text()
            xml_data = xmltodict.parse(data)
            for device in xml_data["devices"]["dev"]:
                if '@sn' in device:
                    device_type = device["@type"]
                    if re.match(r"BT", device_type):
                        devices.append(
                            {
                                "i"              : device['@id'],
                                "type"           : device_type,
                                "sn"             : device['@sn'],
                                "characteristics": [ "ver", "t", "h", "bat", "sig", "alarm" ]
                            }
                        )
                    elif re.match(r"TH", device_type):
                        devices.append(
                            {
                                "i"              : device['@id'],
                                "type"           : device_type,
                                "sn"             : device['@sn'],
                                "characteristics": [ "ver", "t", "bat", "sig", "alarm" ]
                            }
                        )
                    elif re.match(r"HB", device_type):
                        devices.append(
                            {
                                "i"              : device['@id'],
                                "type"           : device_type,
                                "sn"             : device['@sn'],
                                "characteristics": [ "ver", "bat", "sig", "alarm" ]
                            }
                        )
            return {"state": True, "devices": devices}

        return {"state": False, "code": status}

    except (asyncio.TimeoutError, aiohttp.ClientError):
        return {"state": False, "code": 500}

async def get_rooms(httpsession, wunda_ip, wunda_user, wunda_pass):
    wunda_url = f"http://{wunda_ip}/cmd.cgi"
    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status

        if status == 200:
            rooms = []
            data = await resp.json()
            for room in data["rooms"]:
                rooms.append(
                    {
                        "i"              : room["i"],
                        "n"              : room["n"].replace("%20", " "),
                        "characteristics": ["t", "h", "sp", "tp"]
                    }
                )
            return {"state": True, "rooms": rooms}

        return {"state": False, "code": status}
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return {"state": False, "code": 500}


async def get_room_states(httpsession, wunda_ip, wunda_user, wunda_pass):
    wunda_url = f"http://{wunda_ip}/cmd.cgi"
    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status
        if status == 200:
            room_states = []
            data = await resp.json()
            for room_state in data["rooms"]:
                room_states.append(
                    {
                        "i": room_state["i"],
                        "state": {
                            "t": room_state["t"],
                            "h": room_state["h"],
                            "sp": room_state["sp"],
                            "tp": room_state["tp"],
                        },
                    }
                )
            return room_states
        return []
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return []


async def get_device_states(httpsession, wunda_ip, wunda_user, wunda_pass):
    wunda_url = f"http://{wunda_ip}/getdevices.cgi"

    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status

        if status == 200:
            devices = {}
            data = await resp.text()
            xml_data = xmltodict.parse(data)
            for device in xml_data["devices"]["dev"]:
                if '@sn' in device:
                    devices[str(device['@id'])] = device['@sn']
        else:
            return []
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return []

    wunda_url = f"http://{wunda_ip}/syncvalues.cgi?v=2"
    try:
        resp = await httpsession.get(
            wunda_url, auth=aiohttp.BasicAuth(wunda_user, wunda_pass)
        )
        status = resp.status
        if status == 200:
            device_states = []
            data = await resp.text()
            for device_state in data.splitlines():
                device_state_split = dict(x.split(":") for x in device_state.split(";") if ":" in x)
                if ('s', '1') in device_state_split.items():
                        i = device_state.split(";")[0]
                        if i in devices:
                            device_type = device_state_split["t"]
                            if re.match(r"^BT", device_type):
                                device_states.append (
                                    {
                                        "i"     : device_state.split(";")[0],
                                        "sn"    : devices[i],
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
                                device_states.append (
                                    {
                                        "i"     : device_state.split(";")[0],
                                        "sn"    : devices[i],
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
                                device_states.append (
                                    {
                                        "i"     : device_state.split(";")[0],
                                        "sn"    : devices[i],
                                        "state" : {
                                            "ver": device_state_split["v"],
                                            "bat": device_state_split["bat"],
                                            "sig": device_state_split["sig"],
                                            "alarm": device_state_split["alarm"]
                                        }
                                    }
                                )
            return device_states
        return []
    except (asyncio.TimeoutError, aiohttp.ClientError):
        return []

async def put_room_state(httpsession, wunda_ip, wunda_user, wunda_pass, deviceid, params):
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

