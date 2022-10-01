import logging
from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl, SecretStr, ValidationError, validator

from ...utils import get_last_update_datetime
from ..client import DataGoKr
from ..common import KST

# logging
logger = logging.getLogger(__file__)


################################################################################
# [Abstract] Abstract for kpxSMP
################################################################################
class KpxSMP(DataGoKr):
    base_url = "http://openapi.kpx.or.kr/openapi/smp1hToday"
    dataType = "XML"


################################################################################
# [API] 한국전력거래소_계통한계가격조회
################################################################################
# Output Model
class Smp1hTodayRecord(BaseModel):
    tradeDay: str
    tradeHour: int
    areaCd: int
    smp: float


# API
class Smp1hToday(KpxSMP):
    Model = Smp1hTodayRecord
    prefix = "getSmp1hToday"
    areaCd: int = 1  # 1 : 육지 9 :제주

    async def get_records(self, areaCd: int = 1):
        """\
        areaCd: int
            1: 육지, 9: 제주
        """
        return await super().get_records(areaCd=areaCd)


################################################################################
# [Abstract] Abstract for kpxREC
################################################################################
class KpxREC(DataGoKr):
    base_url = "https://api.odcloud.kr/api"
    dataType = "JSON"


################################################################################
# [API] 한국전력거래소_계통한계가격조회
################################################################################
# Output Model
class TodayRecRecord(BaseModel):
    tradeDay: str
    landRec: float
    landHi: float
    landLo: float
    landAv: float
    jejuRec: float
    jejuHi: float
    jejuLo: float
    jejuAv: float
    lastPrice: float


# API
class RecToday(KpxREC):
    Model = TodayRecRecord
    prefix = "15090556/v1/uddi:3e930f97-a16f-4f43-afbe-9f03ef29e464"

    async def get_records(self, page: int = 1, perPage: int = 1, returnType: str = "JSON"):
        return await super().get_records(page=page, perPage=perPage, returnType=returnType)


################################################################################
# [API] 한국전력거래소_계통한계가격조회
################################################################################
# Output Model
class PowerTradingResultRecord(BaseModel):
    rn: int  # 순번
    fuel: str  # 연료원
    tradeDay: str  # 거래일자(YYYYMMDD)
    time: int  # 시간
    pcap: float  # 설비용량(MW)
    mgo: float  # 전력거래량(MWh)
    rtotal: float  # 전력거래대금


# API
class PowerTradingResultInfo1(DataGoKr):
    __version__ = "1.0"
    Model = PowerTradingResultRecord
    base_url = "http://apis.data.go.kr/B552115/PowerTradingResultInfo1"
    prefix = "getPowerTradingResultInfo1"
    dataType = "XML"

    async def get_records(self, dt: datetime = None, *, tradeDay: str = None):
        """\
        tradeDay: str
            e.g. "20220901"
        """
        if dt is not None or tradeDay is None:
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            tradeDay = dt.strftime("%Y%m%d")

        return await super().get_records(tradeDay=tradeDay)
