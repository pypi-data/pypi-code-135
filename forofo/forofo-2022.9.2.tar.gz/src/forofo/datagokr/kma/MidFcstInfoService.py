import logging
import os
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, SecretStr, ValidationError

from ...utils import get_last_update_datetime
from ..client import DataGoKr
from ..common import KST

# logging
logger = logging.getLogger(__file__)


################################################################################
# [Abstract] Abstract for MidFcstInfoService
################################################################################
class MidFcstInfo(DataGoKr):
    schedule = "0 6,18 * * *"


################################################################################
# [API] 중기전망조회  MidFcst
################################################################################
# Output Model
class MidFcstModel(BaseModel):
    wfSv: Optional[str]  # 기상전망


# API
class MidFcst(MidFcstInfo):
    Model = MidFcstModel
    prefix = "1360000/MidFcstInfoService/getMidFcst"

    async def get_records(self, dt: datetime = None, *, stnId: str, tmFc: str = None):
        """\
        stnId: int
            e.g. 108
        tmFc: str
            e.g. '202208110600'
        """
        if dt is not None or tmFc is None:
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            tmFc = dt.strftime("%Y%m%d%H00")
        return await super().get_records(tmFc=tmFc, stnId=stnId)


################################################################################
# [API] 중기육상예보조회  MidLandFcst
################################################################################
# Output Model
class MidLandFcstRecord(BaseModel):
    regId: str
    rnSt3Am: Optional[int]  # 3일 후 오전 강수 확률
    rnSt3Pm: Optional[int]  # 3일 후 오후 강수 확률
    rnSt4Am: Optional[int]  # 4일 후 오전 강수 확률
    rnSt4Pm: Optional[int]  # 4일 후 오후 강수 확률
    rnSt5Am: Optional[int]  # 5일 후 오전 강수 확률
    rnSt5Pm: Optional[int]  # 5일 후 오후 강수 확률
    rnSt6Am: Optional[int]  # 6일 후 오전 강수 확률
    rnSt6Pm: Optional[int]  # 6일 후 오후 강수 확률
    rnSt7Am: Optional[int]  # 7일 후 오전 강수 확률
    rnSt7Pm: Optional[int]  # 7일 후 오후 강수 확률
    rnSt8: Optional[int]  # 8일 후 강수 확률
    rnSt9: Optional[int]  # 9일 후 강수 확률
    rnSt10: Optional[int]  # 10일 후 강수 확률
    wf3Am: Optional[str]  # 3일 후 오전 날씨예보
    wf3Pm: Optional[str]  # 3일 후 오후 날씨예보
    wf4Am: Optional[str]  # 4일 후 오전 날씨예보
    wf4Pm: Optional[str]  # 4일 후 오후 날씨예보
    wf5Am: Optional[str]  # 5일 후 오전 날씨예보
    wf5Pm: Optional[str]  # 5일 후 오후 날씨예보
    wf6Am: Optional[str]  # 6일 후 오전 날씨예보
    wf6Pm: Optional[str]  # 6일 후 오후 날씨예보
    wf7Am: Optional[str]  # 7일 후 오전 날씨예보
    wf7Pm: Optional[str]  # 7일 후 오후 날씨예보
    wf8: Optional[str]  # 8일 후 날씨예보
    wf9: Optional[str]  # 9일 후 날씨예보
    wf10: Optional[str]  # 10일 후 날씨예보


# API
class MidLandFcst(MidFcstInfo):
    prefix = "1360000/MidFcstInfoService/getMidLandFcst"
    Model = MidLandFcstRecord

    async def get_records(self, dt: datetime = None, *, regId: str, tmFc: str = None):
        """\
        stnId: int
            e.g. "11B00000"
        tmFc: str
            e.g. '202208110600'
        """
        if dt is not None or tmFc is None:
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            tmFc = dt.strftime("%Y%m%d%H00")

        return await super().get_records(tmFc=tmFc, regId=regId)


################################################################################
# [API] 중기기온조회  MidTa
################################################################################
# Output Model
class MidTaRecord(BaseModel):
    regId: str
    taMin3: Optional[int]  # 3일 후 예상최저기온(℃)
    taMin3Low: Optional[int]  # 3일 후 예상최저기온 하한 범위
    taMin3High: Optional[int]  # 3일 후 예상최저기온 상한 범위
    taMax3: Optional[int]  # 3일 후 예상최고기온(℃)
    taMax3Low: Optional[int]  # 3일 후 예상최고기온 하한 범위
    taMax3High: Optional[int]  # 3일 후 예상최고기온 상한 범위
    taMin4: Optional[int]  # 4일 후 예상최저기온(℃)
    taMin4Low: Optional[int]  # 4일 후 예상최저기온 하한 범위
    taMin4High: Optional[int]  # 4일 후 예상최저기온 상한 범위
    taMax4: Optional[int]  # 4일 후 예상최고기온(℃)
    taMax4Low: Optional[int]  # 4일 후 예상최고기온 하한 범위
    taMax4High: Optional[int]  # 4일 후 예상최고기온 상한 범위
    taMin5: Optional[int]  # 5일 후 예상최저기온(℃)
    taMin5Low: Optional[int]  # 5일 후 예상최저기온 하한 범위
    taMin5High: Optional[int]  # 5일 후 예상최저기온 상한 범위
    taMax5: Optional[int]  # 5일 후 예상최고기온(℃)
    taMax5Low: Optional[int]  # 5일 후 예상최고기온 하한 범위
    taMax5High: Optional[int]  # 5일 후 예상최고기온 상한 범위
    taMin6: Optional[int]  # 6일 후 예상최저기온(℃)
    taMin6Low: Optional[int]  # 6일 후 예상최저기온 하한 범위
    taMin6High: Optional[int]  # 6일 후 예상최저기온 상한 범위
    taMax6: Optional[int]  # 6일 후 예상최고기온(℃)
    taMax6Low: Optional[int]  # 6일 후 예상최고기온 하한범위
    taMax6High: Optional[int]  # 6일 후 예상최고기온 상한범위
    taMin7: Optional[int]  # 7일 후 예상최저기온(℃)
    taMin7Low: Optional[int]  # 7일 후 예상최저기온 하한범위
    taMin7High: Optional[int]  # 7일 후 예상최저기온 상한범위
    taMax7: Optional[int]  # 7일 후 예상최고기온(℃)
    taMax7Low: Optional[int]  # 7일 후 예상최고기온 하한범위
    taMax7High: Optional[int]  # 7일 후 예상최고기온 상한범위
    taMin8: Optional[int]  # 8일 후 예상최저기온(℃)
    taMin8Low: Optional[int]  # 8일 후 예상최저기온 하한범위
    taMin8High: Optional[int]  # 8일 후 예상최저기온 상한범위
    taMax8: Optional[int]  # 8일 후 예상최고기온(℃)
    taMax8Low: Optional[int]  # 8일 후 예상최고기온 하한범위
    taMax8High: Optional[int]  # 8일 후 예상최고기온 상한범위
    taMin9: Optional[int]  # 9일 후 예상최저기온(℃)
    taMin9Low: Optional[int]  # 9일 후 예상최저기온 하한범위
    taMin9High: Optional[int]  # 9일 후 예상최저기온 상한범위
    taMax9: Optional[int]  # 9일 후 예상최고기온(℃)
    taMax9Low: Optional[int]  # 9일 후 예상최고기온 하한범위
    taMax9High: Optional[int]  # 9일 후 예상최고기온 상한범위
    taMin10: Optional[int]  # 10일 후 예상최저기온(℃)
    taMin10Low: Optional[int]  # 10일 후 예상최저기온 하한범위
    taMin10High: Optional[int]  # 10일 후 예상최저기온 상한범위
    taMax10: Optional[int]  # 10일 후 예상최고기온(℃)
    taMax10Low: Optional[int]  # 10일 후 예상최고기온 하한범위
    taMax10High: Optional[int]  # 10일 후 예상최고기온 상한범위


# API
class MidTa(MidFcstInfo):
    prefix = "1360000/MidFcstInfoService/getMidTa"
    Model = MidTaRecord

    async def get_records(self, dt: datetime = None, *, regId: str, tmFc: str = None):
        """\
        stnId: int
            e.g. "11B00000"
        tmFc: str
            e.g. '202208110600'
        """
        if dt is not None or tmFc is None:
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            tmFc = dt.strftime("%Y%m%d%H00")
        return await super().get_records(tmFc=tmFc, regId=regId)


################################################################################
# [API] 중기해상예보조회  MidSeaFcst
################################################################################
# Output Model
class MidSeaFcstRecord(BaseModel):
    regId: str
    wf3Am: Optional[str]  # 3일후 오전날씨예보
    wf3Pm: Optional[str]  # 3일후 오후날씨예보
    wf4Am: Optional[str]  # 4일후 오전날씨예보
    wf4Pm: Optional[str]  # 4일후 오후날씨예보
    wf5Am: Optional[str]  # 5일후 오전날씨예보
    wf5Pm: Optional[str]  # 5일후 오후날씨예보
    wf6Am: Optional[str]  # 6일후 오전날씨예보
    wf6Pm: Optional[str]  # 6일후 오후날씨예보
    wf7Am: Optional[str]  # 7일후 오전날씨예보
    wf7Pm: Optional[str]  # 7일후 오후날씨예보
    wf8: Optional[str]  # 8일후 날씨예보
    wf9: Optional[str]  # 9일후 날씨예보
    wf10: Optional[str]  # 10일후 날씨예보
    wh3AAm: Optional[int]  # 3일후 오전 최저  예상파고(m)
    wh3APm: Optional[int]  # 3일후 오후 최저 예상파고(m)
    wh3BAm: Optional[int]  # 3일후 오전 최고 예상파고(m)
    wh3BPm: Optional[int]  # 3일후 오후 최고 예상파고(m)
    wh4AAm: Optional[int]  # 4일후 오전 최저  예상파고(m)
    wh4APm: Optional[int]  # 4일후 오후 최저 예상파고(m)
    wh4BAm: Optional[int]  # 4일후 오전 최고 예상파고(m)
    wh4BPm: Optional[int]  # 4일후 오후 최고 예상파고(m)
    wh5AAm: Optional[int]  # 5일후 오전 최저  예상파고(m)
    wh5APm: Optional[int]  # 5일후 오후 최저 예상파고(m)
    wh5BAm: Optional[int]  # 5일후 오전 최고 예상파고(m)
    wh5BPm: Optional[int]  # 5일후 오후 최고 예상파고(m)
    wh6AAm: Optional[int]  # 6일후 오전 최저  예상파고(m)
    wh6APm: Optional[int]  # 6일후 오후 최저 예상파고(m)
    wh6BAm: Optional[int]  # 6일후 오전 최고 예상파고(m)
    wh6BPm: Optional[int]  # 6일후 오후 최고 예상파고(m)
    wh7AAm: Optional[int]  # 7일후 오전 최저  예상파고(m)
    wh7APm: Optional[int]  # 7일후 오후 최저 예상파고(m)
    wh7BAm: Optional[int]  # 7일후 오전 최고 예상파고(m)
    wh7BPm: Optional[int]  # 7일후 오후 최고 예상파고(m)
    wh8A: Optional[int]  # 8일후 최저예상파고(m)
    wh8B: Optional[int]  # 8일후 최고 예상파고(m)
    wh9A: Optional[int]  # 9일후 최저예상파고(m)
    wh9B: Optional[int]  # 9일후 최고 예상파고(m)
    wh10A: Optional[int]  # 10일후 최저예상파고(m)
    wh10B: Optional[int]  # 10일후 최고 예상파고(m)


# API
class MidSeaFcst(MidFcstInfo):
    prefix = "1360000/MidFcstInfoService/getMidSeaFcst"
    Model = MidSeaFcstRecord

    async def get_records(self, dt: datetime = None, *, regId: str, tmFc: str = None):
        """\
        tmFc: str
            e.g. '202208110600'
        stnId: int
            e.g. '12A20000'
        """
        if dt is not None or tmFc is None:
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            tmFc = dt.strftime("%Y%m%d%H00")
        return await super().get_records(tmFc=tmFc, regId=regId)
