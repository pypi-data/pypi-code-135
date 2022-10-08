from datetime import datetime, timedelta
import aiohttp
import json
from typing import Final, List, Optional, final
from strompris.schemas import *
from strompris.common import getNorwayTime

class PriceSource():
    
    _price_today: list[Prising] = []
    _price_tomorrow: list[Prising] = []
    
                
    async def async_fetch_price_data(self, url, timeout: int = 30) -> Optional[List[dict]]:
        """Calls external endopoint by url and deserializes json response 

        Args:
            url (_type_): Web Url
            timeout (int, optional): Timeout in seconds. Defaults to 30.

        Returns:
            Optional[List[dict]]: Deserialized json
        """
        headers = {}
        request_timeout = aiohttp.ClientTimeout(total=timeout)
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
    
    async def async_fetch_for_today(self, zone: int) -> Optional[List[Prising]]:
        return None
    
    async def async_fetch_for_tomorrow(self, zone: int) -> Optional[List[Prising]]:
        return None
        

class Hvakosterstrommen(PriceSource):

    
    
    
    api_url: Final[str] = "https://www.hvakosterstrommen.no/api/v1/prices/"
    
    def __init__(self) -> None:
        pass
    
    
    @final
    def byggApiUrl(self, sone: int, dato: datetime):
        return self.api_url + "{dtp}_NO{soneNr}.json".format(dtp = dato.strftime("%Y/%m-%d"), soneNr=str(sone))
        

        
    async def _map_response(self, respons: List[dict], isToday = True) -> List[Prising]:
        prisPeriode: List[Prising] = []
        for pris in respons:
            indeks = respons.index(pris)
            startTid = getNorwayTime().replace(hour=indeks, minute=0, second=0, microsecond=0)
            if (isToday != True):
                startTid += timedelta(days=1) 
            
            sluttTid = startTid + timedelta(hours=1)
            periode = Periode(start=startTid, slutt=sluttTid)
            prising = Prising(periode=periode, data=pris)
            prisPeriode.append(prising)
        return prisPeriode
       
    async def async_fetch_for_today(self, zone: int) -> list[Prising]:
        url = self.byggApiUrl(sone=zone, dato=getNorwayTime())
        data = await self.async_fetch_price_data(url=url)
        if (data is None):
            return []
        else:
            self._price_today = await self._map_response(data)
            return self._price_today
    
    async def async_fetch_for_tomorrow(self, zone: int) -> list[Prising]:
        if (getNorwayTime().hour < 13):
            raise Exception("Strømpris har ikke blitt satt enda.")
        nyTid = getNorwayTime() + timedelta(days=1)
        
        url = self.byggApiUrl(sone=zone, dato=nyTid)
        data = await self.async_fetch_price_data(url=url)
        if (data is None):
            return []
        else:
            self._price_tomorrow = await self._map_response(data, isToday=False)
            return self._price_tomorrow
       


class PriceNotAvailable(Exception):
    """Error to indicate that price data is not available"""