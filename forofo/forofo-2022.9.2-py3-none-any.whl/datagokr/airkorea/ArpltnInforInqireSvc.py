import logging
import os
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, SecretStr, ValidationError, validator

from ...utils import get_last_update_datetime
from ..client import DataGoKr
from ..common import KST

# logging
logger = logging.getLogger(__file__)

# debug only
AIRKOREA_API_KEY = os.getenv("AIRKOREA_API_KEY")


################################################################################
# [Abstract] Abstract for ArpltnInforInqireSvc
################################################################################
class ArpltnInforInqireSvc(DataGoKr):
    dataType = "XML"


################################################################################
# [API] 측정소별 실시간 측정정보 조회
#  - 매시 15분 내외
#
# 버전(ver) 항목설명
# - 버전을 포함하지 않고 호출할 경우 : PM2.5 데이터가 포함되지 않은 원래 오퍼레이션 결과 표출.
# - 버전 1.0을 호출할 경우 : PM2.5 데이터가 포함된 결과 표출.
# - 버전 1.1을 호출할 경우 : PM10, PM2.5 24시간 예측이동 평균데이터가 포함된 결과 표출.
# - 버전 1.2을 호출할 경우 : 측정망 정보 데이터가 포함된 결과 표출.
# - 버전 1.3을 호출할 경우 : PM10, PM2.5 1시간 등급 자료가 포함된 결과 표출
#
# Grade 값의 의미
#   1: 좋음, 2: 보통, 3: 나쁨, 4: 매우나쁨
################################################################################
# Output Model
class MsrstnAcctoRltmMesureDnstyModel(BaseModel):
    dataTime: str
    so2Value: Optional[float]
    coValue: Optional[float]
    o3Value: Optional[float]
    no2Value: Optional[float]
    pm10Value: Optional[int]
    khaiValue: Optional[int]
    khaiGrade: Optional[int]
    so2Grade: Optional[int]
    coGrade: Optional[int]
    o3Grade: Optional[int]
    no2Grade: Optional[int]
    pm10Grade: Optional[int]
    so2Flag: Optional[str]
    coFlag: Optional[str]
    o3Flag: Optional[str]
    no2Flag: Optional[str]
    pm10Flag: Optional[str]

    @validator("*", pre=True)
    def _hyphen_to_none(cls, v):
        """
        (NOTE)
        Airkorea API는 자료이상 시 null이 아닌 string "-"을 반환하여 schema vaidate error 발생.
        pre-validator에서 "-"을 None으로 변환하여 해결.
        """
        if v in ["-"]:
            return None
        return v


# API
class MsrstnAcctoRltmMesureDnsty(ArpltnInforInqireSvc):
    Model: BaseModel = MsrstnAcctoRltmMesureDnstyModel
    prefix: str = "B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"

    async def get_records(self, stationName: str, dataTerm: str = "DAILY", version: str = "1.3"):
        """\
        stationName: str
            e.g. '종로구'
        dataTerm: str
            Default: "DAILY"
        version: str
            Default: "1.3"
        """
        return await super().get_records(stationName=stationName, dataTerm=dataTerm, version=version)


################################################################################
# [API] 통합대기환경지수 나쁨 이상 측정소 목록조회
#  - 매시 15분 내외
################################################################################
# Output Model
class UnityAirEnvrnIdexSnstiveAboveMsrstnListModel(BaseModel):
    stationName: str
    addr: str


# API
class UnityAirEnvrnIdexSnstiveAboveMsrstnList(ArpltnInforInqireSvc):
    prefix: str = "B552584/ArpltnInforInqireSvc/getUnityAirEnvrnIdexSnstiveAboveMsrstnList"
    Model: BaseModel = UnityAirEnvrnIdexSnstiveAboveMsrstnListModel

    async def get_records(self):
        """\
        [NOTE] Query Parameter 없음.
        """
        return await super().get_records()


################################################################################
# [API] 시도별 실시간 측정정보 조회 상세기능명세
#  - 매시 15분 내외
#
# 버전(ver) 항목설명
# - 버전을 포함하지 않고 호출할 경우 : PM2.5 데이터가 포함되지 않은 원래 오퍼레이션 결과 표출.
# - 버전 1.0을 호출할 경우 : PM2.5 데이터가 포함된 결과 표출.
# - 버전 1.1을 호출할 경우 : PM10, PM2.5 24시간 예측이동 평균데이터가 포함된 결과 표출.
# - 버전 1.2을 호출할 경우 : 측정망 정보 데이터가 포함된 결과 표출.
# - 버전 1.3을 호출할 경우 : PM10, PM2.5 1시간 등급 자료가 포함된 결과 표출
#
# Grade 값의 의미
#   1: 좋음, 2: 보통, 3: 나쁨, 4: 매우나쁨
################################################################################
# Output Model
class CtprvnRltmMesureDnstyModel(BaseModel):
    dataTime: Optional[str]
    stationName: str
    mangName: str
    sidoName: str
    so2Value: Optional[float]
    coValue: Optional[float]
    o3Value: Optional[float]
    no2Value: Optional[float]
    pm10Value: Optional[int]
    pm10Value24: Optional[int]
    pm25Value: Optional[int]
    pm25Value24: Optional[int]
    khaiValue: Optional[int]
    khaiGrade: Optional[int]
    so2Grade: Optional[int]
    coGrade: Optional[int]
    o3Grade: Optional[int]
    no2Grade: Optional[int]
    pm10Grade: Optional[int]
    pm25Grade: Optional[int]
    pm10Grade1h: Optional[int]
    pm25Grade1h: Optional[int]
    so2Flag: Optional[str]
    coFlag: Optional[str]
    o3Flag: Optional[str]
    no2Flag: Optional[str]
    pm10Flag: Optional[str]
    pm25Flag: Optional[str]

    @validator("*", pre=True)
    def _hyphen_to_none(cls, v):
        if v in ["-"]:
            return None
        return v


# API
class CtprvnRltmMesureDnsty(ArpltnInforInqireSvc):
    prefix: str = "B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    Model: BaseModel = CtprvnRltmMesureDnstyModel

    async def get_records(self, sidoName: str = "전국", ver: str = "1.3"):
        """\
        sidoName: str
            e.g. '전국' (서울, 부산, 대구, 인천, 광주, ...)
        ver: str
            Default: "1.3"
        """
        return await super().get_records(sidoName=sidoName, ver=ver)


################################################################################
# [API] 대기질 예보통보 조회
#  - 매일 4회 (5, 11, 17, 23시), 각 시별 30분 내외
#
# 미세먼지/오존 예보 관련 안내사항
#   - 미세먼지 예보는 오늘예보 / 내일예보 / 모레예보가 제공되며, 시시각각으로 변하는 대기질 상황을 전달하기 위해 매일 4회(오전5시, 오전 11시, 오후5시(17시), 오후11시(23시))에 19개 권역으로 발표되고 있습니다.
#   - 내일예보의 경우, 지역별 상세예보는 오전5시, 오전 11시에는 발표되지 않습니다.
#   - 모레예보의 경우, 예보개황만 제공하며 예보등급은 제공하지 않습니다.
#   - 모레예보는 예보 정확도가 낮을 수 있으나 정보 제공을 위해 발표됩니다. (시범운영 : ‘15년 수도권,  ’16년 전국)
#   - 오존예보는 매년 4월15일 ~ 10월15일까지 발표됩니다.
#   - [오늘/내일/모레] 예보 데이터 확인방법
#     "대기질 예보통보 조회" 오퍼레이션 호출 시, 응답 메세지 중 <dataTime>이 2015-12-29 05시 발표일 경우
#     § 오늘예보 : <dataTime> 2015-12-29 05시 발표 <informData> 2015-12-29
#     § 내일예보 : <dataTime> 2015-12-29 05시 발표 <informData> 2015-12-30
#     § 모레예보 : <dataTime> 2015-12-29 05시 발표 <informData> 2015-12-31
################################################################################
# Output Model
class MinuDustFrcstDspthModel(BaseModel):
    dataTime: str
    informCode: str
    informOverall: Optional[str]
    informCause: Optional[str]
    informData: Optional[str]
    informGrade: Optional[str]
    actionKnack: Optional[str]
    imageUrl1: Optional[HttpUrl]
    imageUrl2: Optional[HttpUrl]
    imageUrl3: Optional[HttpUrl]
    imageUrl4: Optional[HttpUrl]
    imageUrl5: Optional[HttpUrl]
    imageUrl6: Optional[HttpUrl]
    imageUrl7: Optional[HttpUrl]
    imageUrl8: Optional[HttpUrl]
    imageUrl9: Optional[HttpUrl]


# API
class MinuDustFrcstDspth(ArpltnInforInqireSvc):
    prefix: str = "B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth"
    Model: BaseModel = MinuDustFrcstDspthModel
    schedule = "0 5,11,17,23 * * *"

    async def get_records(self, *, informCode: str = "PM10", searchDate: str = None):
        """\
        searchDate: str
            e.g. "2022-08-17"
        informCode: str
            e.g. "PM10" ("PM10", "PM25", "O3")
        """
        return await super().get_records(searchDate=searchDate, informCode=informCode)
