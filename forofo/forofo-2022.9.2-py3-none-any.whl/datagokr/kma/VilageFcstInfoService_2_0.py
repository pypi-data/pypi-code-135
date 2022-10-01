import logging
from datetime import datetime

from pydantic import BaseModel

from ...utils import get_last_update_datetime
from ..client import DataGoKr
from ..common import KST

# logging
logger = logging.getLogger(__file__)


################################################################################
# [API] 초단기 실황  UltraSrtNcst
################################################################################
# Output Model
class UltraSrtNcstRecord(BaseModel):
    baseDate: str
    baseTime: str
    category: str
    obsrValue: str
    nx: int
    ny: int


# API
class UltraSrtNcst(DataGoKr):
    Model: BaseModel = UltraSrtNcstRecord
    prefix: str = "1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
    schedule = "40 * * * *"

    async def get_records(
        self, dt: datetime = None, *, nx: int, ny: int, base_date: str = None, base_time: str = None
    ):
        """\
        nx: int
            e.g. 64
        ny: int
            e.g. 119
        base_date: str
            e.g. '20220817'
        base_time: str
            e.g. '0500'
        """
        if dt is not None or (base_date is None and base_time is None):
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            base_date, base_time = dt.strftime("%Y%m%d,%H00").split(",")

        return await super().get_records(nx=nx, ny=ny, base_date=base_date, base_time=base_time)


################################################################################
# [API] 초단기 예보 UltraSrtFcst
################################################################################
# Output Model
class UltraSrtFcstRecord(BaseModel):
    baseDate: str
    baseTime: str
    fcstDate: str
    fcstTime: str
    category: str
    fcstValue: str
    nx: int
    ny: int


# API
class UltraSrtFcst(DataGoKr):
    Model: BaseModel = UltraSrtFcstRecord
    prefix: str = "1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"
    schedule = "45 * * * *"

    async def get_records(
        self, dt: datetime = None, *, nx: int, ny: int, base_date: str = None, base_time: str = None
    ):
        """\
        nx: int
            e.g. 64
        ny: int
            e.g. 119
        base_date: str
            e.g. '20220817'
        base_time: str
            e.g. '0500'
        """
        if dt is not None or (base_date is None and base_time is None):
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            base_date, base_time = dt.strftime("%Y%m%d,%H30").split(",")

        return await super().get_records(nx=nx, ny=ny, base_date=base_date, base_time=base_time)


################################################################################
# [API] 단기 예보 VilageFcst
################################################################################
# Output Model
class VilageFcstRecord(BaseModel):
    baseDate: str
    baseTime: str
    fcstDate: str
    fcstTime: str
    category: str
    fcstValue: str
    nx: int
    ny: int


# API
class VilageFcst(DataGoKr):
    Model: BaseModel = VilageFcstRecord
    prefix: str = "1360000/VilageFcstInfoService_2.0/getVilageFcst"
    schedule = "10 2,5,8,11,14,17,20,23 * * *"

    async def get_records(
        self, dt: datetime = None, *, nx: int, ny: int, base_date: str = None, base_time: str = None
    ):
        """\
        nx: int
            e.g. 64
        ny: int
            e.g. 119
        base_date: str
            e.g. '20220817'
        base_time: str
            e.g. '0500'
        """
        if dt is not None or (base_date is None and base_time is None):
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            base_date, base_time = dt.strftime("%Y%m%d,%H00").split(",")

        return await super().get_records(nx=nx, ny=ny, base_date=base_date, base_time=base_time)
