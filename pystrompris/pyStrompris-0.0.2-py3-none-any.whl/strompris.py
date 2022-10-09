
from datetime import datetime
from typing import Final, List, Optional, final
from .schemas import *
from .common import *
from .PriceSource import *
from .const import *

class Strompris(Common):
    
    priceSource: PriceSource
    
    def __init__(self, source: str, zone: int) -> None:
        if (source is SOURCE_HVAKOSTERSTROMMEN):
            self.priceSource = Hvakosterstrommen(price_zone=zone)
        else:
            raise Exception("Could not find source:",source)
    
    @final
    def showPriceZones(self) -> None:
        print("NO1", "Øst-Norge")
        print("NO2", "Sør-Norge")
        print("NO3", "Midt-Norge")
        print("NO4", "Nord-Norge")
        print("NO5", "Vest-Norge")
        
    async def async_getElPrices(self, withFuture: bool = True) -> list[Prising]:
        prices: list[Prising] = []
                
        _for_today = await self.priceSource.async_fetch_for_today()
        if (_for_today is not None):
            prices.extend(_for_today)
        if (withFuture):
            try:
                _for_tomorrow = await self.priceSource.async_fetch_for_tomorrow()
                if (_for_tomorrow is not None):
                    prices.extend(_for_tomorrow)
            except PriceNotAvailable:
                print("Price data is not available for tomorrow")
                    
        if (self.priceSource._price_zone != 4):
            """Price Zone NO4 is not subjected to Electricity Tax as of now"""
            for price in prices:
                price.tax = self.getTax(price.kwh) 
                price.total = price.kwh + price.tax
        
        return prices
        
    def getElPrices(self, withFuture: bool = True) -> list[Prising]:
        return self.sync(self.async_getElPrices(withFuture=withFuture))
        
    async def async_getElPriceNow(self) -> Optional[Prising]:
        if (not self.priceSource._price_today or len(self.priceSource._price_today) == 0):
            await self.async_getElPrices(withFuture=False)
        return next((x for x in self.priceSource._price_today if x.start.hour == getNorwayTime().hour), [None])
        
    def getElPriceNow(self) -> Optional[Prising]:
        if (not self.priceSource._price_today or len(self.priceSource._price_today) == 0):
            self.sync(self.async_getElPriceNow())
        return self.sync(self.async_getElPriceNow())
        
    def getPriceAttrs(self) -> Optional[PriceAttr]:
        now = self.getElPriceNow()
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
    