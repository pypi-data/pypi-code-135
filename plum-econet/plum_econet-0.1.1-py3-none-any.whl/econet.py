import aiohttp
from .params import Params
from .exceptions import EconetHTTPException, EconetUnauthorized


class Param(object):
    def __init__(self, pid, data, enums):
        self.desc = data.get("name", "")
        self.special = data.get("special", None)
        self.edit = data.get("edit", False)
        self.id = pid
        self.unit = data["unit"]
        self._value = data.get("value", None)
        self.minv = data.get("minv", None)
        self.maxv = data.get("maxv", None)
        self.offset = data.get("offset", None)
        self.mult = data.get("mult", None)
        self.enums = enums

    @property
    def value(self):
        if self.special is not None and self.special != 0 and self._value is not None:
            if len(self.enums[self.special]["values"]) > self._value:
                return self.enums[self.special]["values"][self._value]
        return self._value

    @value.setter
    def value(self, new):
        self._value = new

    def __str__(self):
        return f"{self.value}{self.unit if self.unit is not None else ''}"

    def __repr__(self):
        return f"{self.__class__.__name__}(pid={repr(self.id)})"


class Econet(object):
    def __init__(self, host, login, password):
        self.login = login
        self.password = password
        self.host = host
        self.params = dict()
        self.units = dict()
        self.enums = dict()

    def __repr__(self):
        return f"{self.__class__.__name__}(host={repr(self.host)}, login={repr(self.login)})"

    async def setup(self):
        await self.fetch_units()
        await self.fetch_enums()
        await self.fetch_current_data_params()
        await self.fetch_rm_params()

    async def _call_api(self, cmd):
        async with aiohttp.ClientSession() as session:
            auth = aiohttp.BasicAuth(self.login, self.password)
            async with session.get(f"{self.host}/econet/{cmd}", auth=auth) as resp:
                if resp.status == 401:
                    raise EconetUnauthorized()
                if resp.status != 200:
                    raise EconetHTTPException(
                        f"Got {resp.status} {resp.reason} when calling "
                        f"{self.host}/econet/{cmd}"
                    )
                j = await resp.json()
                return j

    async def fetch_units(self):
        resp = await self._call_api("rmParamsUnitsNames")
        self.units = resp["data"]

    async def fetch_enums(self):
        resp = await self._call_api("rmParamsEnums")
        self.enums = resp["data"]

    async def fetch_current_data_params(self):
        resp = await self._call_api("rmCurrentDataParams")
        for pid, data in resp["data"].items():
            data["unit"] = (
                self.units[int(data["unit"])]
                if int(data["unit"]) < len(self.units)
                else ""
            )
            if pid == "123":
                pid = "110"
            pid = Params.get_by_id(pid)
            self.params[pid] = Param(pid, data, self.enums)

    async def fetch_rm_params(self):
        resp = await self._call_api("rmParamsData")
        for pid, data in enumerate(resp["data"]):
            data["unit"] = (
                self.units[int(data["unit"])]
                if int(data["unit"]) < len(self.units)
                else ""
            )
            pid = Params.get_by_id(pid)
            self.params[pid] = Param(pid, data, self.enums)

    async def fetch_sys_params(self):
        return await self._call_api("sysParams")

    async def fetch_reg_params_data(self):
        resp = await self._call_api("regParamsData")
        for pid, data in resp["data"].items():
            PID = Params.get_by_id(pid)
            if PID is not None:
                self.params[PID].value = data

    async def fetch_rm_params_data(self):
        resp = await self._call_api("rmParamsData")
        for pid, data in enumerate(resp["data"]):
            PID = Params.get_by_id(pid)
            if PID is not None:
                self.params[PID].value = data["value"]

    async def update(self):
        await self.fetch_reg_params_data()
        await self.fetch_rm_params_data()

    def get_param(self, param):
        return self.params[param]

    async def set_param(self, param_id, value):
        if type(param_id) == int:
            endpoint = f"rmNewParam?newParamIndex={param_id}&newParamValue={value}"
        else:
            endpoint = f"rmCurrNewParam?newParamKey={param_id}&newParamValue={value}"
        resp = await self._call_api(endpoint)
        if resp["result"] != "OK":
            raise Exception(f"Something went wrong: {resp}")
