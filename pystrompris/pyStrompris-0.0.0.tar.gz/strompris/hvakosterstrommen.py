from datetime import datetime, timedelta
import json
from typing import Final, List, Optional, final
import pytz
import aiohttp
from strompris.common import Common

from strompris.schemas import *

class Hvakosterstrommen(Common):
    
    
    api_url: Final[str] = "https://www.hvakosterstrommen.no/api/v1/prices/"
    
    def __init__(self) -> None:
        pass
    
    
    @final
    def byggApiUrl(self, sone: int, dato: datetime):
        return self.api_url + "{dtp}_NO{soneNr}.json".format(dtp = dato.strftime("%Y/%m-%d"), soneNr=str(sone))
        
    async def hentPrisData(self, url, timeout_sec: int = 30) -> Optional[List[dict]]:
        """Return WebResponse data from hvakosterstrommen."""

        headers = {}
        request_timeout = aiohttp.ClientTimeout(total=timeout_sec)
        async with aiohttp.ClientSession(
            headers=headers, timeout=request_timeout
        ) as session:
            async with session.get(url) as response:
                if (response.status == 200):
                    payload = await response.read()
                    #json_string = str(payload, "utf-8")
                    return json.loads(payload)
                else:
                    return None
        
    async def behandleRespons(self, respons: List[dict]) -> List[Prising]:
        prisPeriode: List[Prising] = []
        storrelse = len(respons)-1
        for pris in respons:
            indeks = respons.index(pris)
            startTid = self.getNorwayTime().replace(hour=indeks, minute=0, second=0, microsecond=0)
            sluttTid = self.getNorwayTime().replace(hour=0, minute=0, second=0, microsecond=0)
            if indeks != storrelse:
                sluttTid = sluttTid.replace(hour=(indeks + 1)) + timedelta(days = 1)
            periode = Periode(start=startTid, slutt=sluttTid)
            prising = Prising(periode=periode, data=pris)
            prisPeriode.append(prising)
        return prisPeriode
                
    _strompris_i_dag: list[Prising] = []
    async def hentForIDag(self, sone: int) -> Optional[List[Prising]]:
        url = self.byggApiUrl(sone=sone, dato=self.getNorwayTime())
        data = await self.hentPrisData(url=url)
        if (data is None):
            return None
        else:
            self._strompris_i_dag = await self.behandleRespons(data)
            return self._strompris_i_dag
    
    _strompris_i_morgen: list[Prising] = []
    async def hentForIMorgen(self, sone: int) -> Optional[List[Prising]]:
        if (self.getNorwayTime().hour < 13):
            raise Exception("Strømpris har ikke blitt satt enda.")
        nyTid = self.getNorwayTime() + timedelta(days=1)
        
        url = self.byggApiUrl(sone=sone, dato=nyTid)
        data = await self.hentPrisData(url=url)
        if (data is None):
            return None
        else:
            self._strompris_i_morgen = await self.behandleRespons(data)
            return self._strompris_i_morgen
        
    async def hentStromprisNaa(self) -> Optional[Prising]:
        """Henter priser for timen
        
        Hvis strømpriser for i dag ikke er innhentet, vil det hentes inn først
        """
        if (len(self._strompris_i_dag) == 0):
            await self.hentForIDag(1)
        if (len(self._strompris_i_dag) == 0):
            return None
        for pris in self._strompris_i_dag:
            if (pris.start.hour == self.getNorwayTime().hour):
                return pris
        return None
        
    