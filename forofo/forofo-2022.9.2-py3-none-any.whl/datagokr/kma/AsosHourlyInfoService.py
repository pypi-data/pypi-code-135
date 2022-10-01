import logging
import os
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional

from pydantic import BaseModel, validator

from ..common import KST
from ...utils import get_last_update_datetime
from ..client import DataGoKr

# logging
logger = logging.getLogger(__file__)


################################################################################
# [API] 지상(종관,ASOS) 시간자료 조회
################################################################################
# Output Model
class WthrDataListRecord(BaseModel):
    tm: str  # 시간
    rnum: int  # 목록순서
    stnId: int  # 지점번호
    stnNm: str  # 지점이름
    ta: Optional[float]  # 기온
    taQcflg: Optional[int]  # 기온품질검사플래그 (null: 정상, 1: 오류, 9: 결측)
    rn: Optional[float]  # 강수량
    rnQcflg: Optional[int]
    ws: Optional[float]  # 풍속
    wsQcflg: Optional[int]
    wd: Optional[str]  # 풍향 (20: 북북동, 40: 북동, ..., 360: 정북, 00: CALM, 99: 변화많음)
    wdQcflg: Optional[int]
    hm: Optional[int]  # 상대습도
    hmQcflg: Optional[int]
    pv: Optional[float]  # 증기압
    td: Optional[float]  # 이슬점온도
    pa: Optional[float]  # 현지기압
    paQcflg: Optional[int]
    ps: Optional[float]  # 해면기압
    psQcflg: Optional[int]
    ss: Optional[float]  # 일조시간
    ssQcflg: Optional[int]
    icsr: Optional[float]  # 일사량
    dsnw: Optional[float]  # 적설량
    hr3Fhsc: Optional[float]  # 3시간신적설
    dc10Tca: Optional[int]  # 전운량
    dc10LmcsCa: Optional[int]  # 중하층운량
    clfmAbbrCd: Optional[str]  # 운형
    lcsCh: Optional[int]  # 최저운고
    vs: Optional[int]  # 시정
    # gndSttCd: Optional[int]   # 2016.7.1 종료
    dmstMtphNo: Optional[str]  # 현상번호
    ts: Optional[float]  # 지면온도
    tsQcflg: Optional[int]
    m005Te: Optional[float]  # 5cm 지중온도
    m01Te: Optional[float]  # 10cm 지중온도
    m02Te: Optional[float]  # 20cm 지중온도
    m03Te: Optional[float]  # 30cm 지중온도

    @validator("*", pre=True)
    def cast(cls, v):
        if v == "":
            return None
        return v


# API
class WthrDataList(DataGoKr):
    Model = WthrDataListRecord
    prefix = "1360000/AsosHourlyInfoService/getWthrDataList"
    schedule = "0 11 * * *"

    async def get_records(
        self,
        dt: datetime = None,
        *,
        stnIds: int,
        startDt: str = None,
        startHh: str = None,
        endDt: str = None,
        endHh: str = None,
        dataCd: str = "ASOS",
        dateCd: str = "HR"
    ):
        """\
        Arguments
        ---------
        stnIds: int
            e.g. 119
        startDt: str
            e.g. '20220817'
        startHh: str
            e.g. '17'
        endDt: str
            e.g. '20220818'
        endHh: str
            e.g. '17'
        dataCd: str
            Default: 'ASOS'
        dateCd: str
            Default: 'HR'
        """
        if dt is not None or all([x is None for x in [startDt, startHh, endDt, endHh]]):
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            startDt = (dt - timedelta(days=1)).strftime("%Y%m%d")
            startHh = "00"
            endDt = (dt - timedelta(days=1)).strftime("%Y%m%d")
            endHh = "23"

        return await super().get_records(
            startDt=startDt,
            startHh=startHh,
            endDt=endDt,
            endHh=endHh,
            stnIds=stnIds,
            dataCd=dataCd,
            dateCd=dateCd,
        )
