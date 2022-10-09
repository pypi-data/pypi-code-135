from datetime import datetime, timedelta
import aiohttp
import json
from typing import Final, List, Optional, final
from strompris.schemas import *
from strompris.common import getNorwayTime

class PriceSource():
    
    _price_zone: int
    _price_today: list[Prising] = []
    _price_tomorrow: list[Prising] = []
    
    def __init__(self, price_zone: int) -> None:
        self._price_zone = price_zone
                
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
    
    async def async_fetch_for_today(self) -> Optional[List[Prising]]:
        return None
    
    async def async_fetch_for_tomorrow(self) -> Optional[List[Prising]]:
        return None
        

class Hvakosterstrommen(PriceSource):
    
    api_url: Final[str] = "https://www.hvakosterstrommen.no/api/v1/prices/"
    

    def __init__(self, price_zone: int) -> None:
        super().__init__(price_zone)
    
    
    @final
    def byggApiUrl(self, dato: datetime):
        return self.api_url + "{dtp}_NO{soneNr}.json".format(dtp = dato.strftime("%Y/%m-%d"), soneNr=str(self._price_zone))
        

        
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
       
    async def async_fetch_for_today(self) -> list[Prising]:
        if (not self._price_today and len(self._price_today) != 0 and self._price_today[0].start.day == getNorwayTime().day):
            return self._price_today
        
        url = self.byggApiUrl(dato=getNorwayTime())
        data = await self.async_fetch_price_data(url=url)
        if (data is None):
            return []
        else:
            self._price_today = await self._map_response(data)
            return self._price_today
    
    async def async_fetch_for_tomorrow(self) -> list[Prising]:
        tomorrow = getNorwayTime() + timedelta(days=1)
        
        if (not self._price_tomorrow and len(self._price_tomorrow) != 0 and self._price_tomorrow[0].start.day == tomorrow.day):
            return self._price_tomorrow
        
        if (getNorwayTime().hour < 13):
            raise Exception("Strømpris har ikke blitt satt enda.")
        
        url = self.byggApiUrl(dato=tomorrow)
        data = await self.async_fetch_price_data(url=url)
        if (data is None):
            return []
        else:
            self._price_tomorrow = await self._map_response(data, isToday=False)
            return self._price_tomorrow
       


class PriceNotAvailable(Exception):
    """Error to indicate that price data is not available"""