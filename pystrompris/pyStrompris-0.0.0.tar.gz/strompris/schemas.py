from datetime import datetime

class Periode():
    start_tid: datetime
    slutt_tid: datetime
    
    def __init__(self, start: datetime, slutt: datetime) -> None:
        self.start_tid = start
        self.slutt_tid = slutt


class Prising():
    start: datetime
    slutt: datetime
    NOK_kwh: float
    EUR_kwh: float
    kwh: float # Defaults to NOK
    exr: float # Exchange Rate
    
    def __init__(self, periode: Periode, data: dict) -> None:
        self.start = periode.start_tid
        self.slutt = periode.slutt_tid
        self.NOK_kwh = data['NOK_per_kWh']
        self.EUR_kwh = data['EUR_per_kWh']
        self.kwh = round(self.NOK_kwh, 3)
        self.exr = data['EXR']
    


