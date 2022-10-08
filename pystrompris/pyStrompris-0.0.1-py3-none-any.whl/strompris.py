
from datetime import datetime
from typing import Final, List, Optional, final
from .schemas import *
from .common import *
from .PriceSource import *
from .const import *

class Strompris(Common):
    
    priceSource: PriceSource
    
    def __init__(self, source) -> None:
        if (source is SOURCE_HVAKOSTERSTROMMEN):
            self.priceSource = Hvakosterstrommen()
        else:
            raise Exception("Could not find source:",source)
    
    @final
    def showPriceZones(self) -> None:
        print("NO1", "Øst-Norge")
        print("NO2", "Sør-Norge")
        print("NO3", "Midt-Norge")
        print("NO4", "Nord-Norge")
        print("NO5", "Vest-Norge")
        
    async def async_getElPriceFromSource(self, zone: int, withFuture: bool = True) -> list[Prising]:
        prices: list[Prising] = []
                
        _for_today = await self.priceSource.async_fetch_for_today(zone=zone)
        if (_for_today is not None):
            prices.extend(_for_today)
        if (withFuture):
            try:
                _for_tomorrow = await self.priceSource.async_fetch_for_tomorrow(zone=zone)
                if (_for_tomorrow is not None):
                    prices.extend(_for_tomorrow)
            except PriceNotAvailable:
                print("Price data is not available for tomorrow")    
        if (zone != 4):
            for price in prices:
                price.tax = self.getTax(price.kwh) 
                price.total = price.kwh + price.tax
        
        return prices
        
    def getElPriceFromSource(self, zone: int, withFuture: bool = True) -> list[Prising]:
        return self.sync(self.async_getElPriceFromSource(zone=zone, withFuture=withFuture))
        
    async def async_getElPriceNow(self, zone: int) -> Optional[Prising]:
        if (not self.priceSource._price_today or len(self.priceSource._price_today) == 0):
            await self.async_getElPriceFromSource(zone=zone, withFuture=False)
        return next((x for x in self.priceSource._price_today if x.start.hour == getNorwayTime().hour), [None])
        
    def getElPriceNow(self, zone) -> Optional[Prising]:
        if (not self.priceSource._price_today or len(self.priceSource._price_today) == 0):
            self.sync(self.async_getElPriceNow(zone=zone))
        return self.sync(self.async_getElPriceNow(zone=zone))
        
    def getPriceAttrs(self, zone) -> Optional[PriceAttr]:
        now = self.getElPriceNow(zone=zone)
        common = Common()
        return PriceAttr(
            start=now.start,
            end=now.slutt,
            kwh=now.kwh,
            tax=now.tax,
            total=now.total,
            max=common.getMax(self.priceSource._price_today),
            avg=common.getAverage(self.priceSource._price_today),
            min=common.getMin(self.priceSource._price_today),
            price_level=common.getPriceLevel(now, self.priceSource._price_today)
        )
    