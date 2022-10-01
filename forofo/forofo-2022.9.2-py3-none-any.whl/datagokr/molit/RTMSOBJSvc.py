import logging
import os
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional

import pendulum
from pydantic import BaseModel, Field, HttpUrl, SecretStr, ValidationError

from ...utils import get_last_update_datetime
from ..client import DataGoKr
from ..common import KST

# logging
logger = logging.getLogger(__file__)

# debug only
TZINFO = pendulum.timezone("Asia/Seoul")
MOLIT_API_KEY = os.getenv("MOLIT_API_KEY")
DEBUG_LAWD_CD = "11110"
DEBUG_DEAL_YMD = (datetime.now(tz=TZINFO) - timedelta(weeks=8)).strftime("%Y%m")


################################################################################
# [Abstract] Abstract for RTMSOBJSvc
################################################################################
class RTMSOBJSvc(DataGoKr):
    base_url: str = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc"

    async def get_records(self, dt: datetime = None, *, LAWD_CD: str = None, DEAL_YMD: str = None):
        """\
        [NOTE] 매월 15일 업데이트

        LAWD_CD: str
            e.g. "11110"
        DEAL_YMD: str
            e.g. "202209"
        """
        if dt is not None or DEAL_YMD is None:
            if dt is None:
                dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
            DEAL_YMD = dt.strftime("%Y%m")

        return await super().get_records(LAWD_CD=LAWD_CD, DEAL_YMD=DEAL_YMD)


# Some Endpoints are Opened at Port 8081
class RTMSOBJSvc8081(RTMSOBJSvc):
    base_url: str = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc"


################################################################################
# [API] 아파트 매매 실거래자료 (아파트 매매 신고자료)
################################################################################
# Output Model
class RTMSDataSvcAptTradeModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    거래금액: Optional[str]  # 만원
    건축년도: Optional[str]  # 건축년도
    년: Optional[str]  # 계약년도
    법정동: Optional[str]
    아파트: Optional[str]  # 아파트명
    월: Optional[str]  # 계약월
    일: Optional[str]  # 계약일
    전용면적: Optional[str]  # 전용면적, sqm
    지번: Optional[str]  # 지번
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]  # 층
    해제여부: Optional[str]  # 해제여부
    해제사유발생일: Optional[str]  # 해제사유발생일
    거래유형: Optional[str]  # 중개 및 직거래 여부
    중개업소주소: Optional[str]  # 시군구 단위


# API
class RTMSDataSvcAptTrade(RTMSOBJSvc8081):
    Model = RTMSDataSvcAptTradeModel
    prefix = "getRTMSDataSvcAptTrade"
    schedule = "15 0 15 * *"


################################################################################
# [API] 연립/다세대 매매 실거래자료 (연립/다세대 매매 신고자료)
################################################################################
# Output Model
class RTMSDataSvcRHTradeModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    거래금액: Optional[str]  # 만원
    건축년도: Optional[str]  # 건축년도
    년: Optional[str]  # 계약년도
    대지권면적: Optional[str]  # 대지권면적
    법정동: Optional[str]
    연립다세대: Optional[str]  # 연립다세대명
    월: Optional[str]  # 계약월
    일: Optional[str]  # 계약일
    전용면적: Optional[str]  # 전용면적, sqm
    지번: Optional[str]  # 지번
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]  # 층
    해제여부: Optional[str]  # 해제여부
    해제사유발생일: Optional[str]  # 해제사유발생일
    거래유형: Optional[str]  # 중개 및 직거래 여부
    중개업소주소: Optional[str]  # 시군구 단위


# API
class RTMSDataSvcRHTrade(RTMSOBJSvc8081):
    Model = RTMSDataSvcRHTradeModel
    prefix = "getRTMSDataSvcRHTrade"
    schedule = "30 0 15 * *"


################################################################################
# [API] 단독/다가구 매매 실거래자료 (단독/다가구 매매 신고자료)
################################################################################
# Output Model
class RTMSDataSvcSHTradeModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    거래금액: Optional[str]  # 만원
    건축년도: Optional[str]  # 건축년도
    년: Optional[str]  # 계약년도
    대지면적: Optional[str]  # 대지면적
    법정동: Optional[str]
    연면적: Optional[str]  # 연면적
    월: Optional[str]  # 계약월
    일: Optional[str]  # 계약일
    주택유형: Optional[str]  # 주택유형
    지역코드: Optional[str]  # 지역코드
    해제여부: Optional[str]  # 해제여부
    해제사유발생일: Optional[str]  # 해제사유발생일
    거래유형: Optional[str]  # 중개 및 직거래 여부
    중개업소주소: Optional[str]  # 시군구 단위


# API
class RTMSDataSvcSHTrade(RTMSOBJSvc8081):
    Model = RTMSDataSvcSHTradeModel
    prefix: str = "getRTMSDataSvcSHTrade"
    schedule = "45 0 15 * *"


################################################################################
# [API] 아파트 매매 실거래 상세자료
################################################################################
# Output Model
class RTMSDataSvcAptTradeDevModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    거래금액: Optional[str]  # 만원
    건축년도: Optional[str]  # 건축년도
    년: Optional[str]  # 계약년도
    도로명: Optional[str]  # 도로명
    도로명건물본번호코드: Optional[str]  # 도로명건물본번호코드
    도로명건물부번호코드: Optional[str]  # 도로명건물부번호코드
    도로명시군구코드: Optional[str]  # 도로명시군구코드
    도로명일련번호코드: Optional[str]  # 도로명일련번호코드
    도로명지상지하코드: Optional[str]  # 도로명지상지하코드
    도로명코드: Optional[str]  # 도로명코드
    법정동: Optional[str]
    법정동본번코드: Optional[str]
    법정동부번코드: Optional[str]
    법정동시군구코드: Optional[str]
    법정동읍면동코드: Optional[str]
    아파트: Optional[str]  # 아파트명
    월: Optional[str]  # 계약월
    일: Optional[str]  # 계약일
    일련번호: Optional[str]  # 일련번호
    전용면적: Optional[str]  # 전용면적
    지번: Optional[str]  # 지번
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]  # 층
    해제여부: Optional[str]  # 해제여부
    해제사유발생일: Optional[str]  # 해제사유발생일
    거래유형: Optional[str]  # 중개 및 직거래 여부
    중개업소주소: Optional[str]  # 시군구 단위


# API
class RTMSDataSvcAptTradeDev(RTMSOBJSvc):
    Model = RTMSDataSvcAptTradeDevModel
    prefix = "getRTMSDataSvcAptTradeDev"
    schedule = "0 1 15 * *"


################################################################################
# [API] 아파트 분양권 전매 신고 자료
################################################################################
# Output Model
class RTMSDataSvcSilvTradeModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    거래금액: Optional[str]  # 만원
    구분: Optional[str]  # 분양권 및 입주권(입)
    년: Optional[str]  # 계약년도
    단지: Optional[str]  # 단지
    동: Optional[str]  # 법정동
    시군구: Optional[str]  # 시군구
    월: Optional[str]  # 계약월
    일: Optional[str]  # 계약일
    전용면적: Optional[str]  # 전용면적
    지번: Optional[str]  # 지번
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]  # 층
    해제여부: Optional[str]  # 해제여부
    해제사유발생일: Optional[str]  # 해제사유발생일
    거래유형: Optional[str]  # 중개 및 직거래 여부
    중개업소주소: Optional[str]  # 시군구 단위


# API
class RTMSDataSvcSilvTrade(RTMSOBJSvc):
    Model = RTMSDataSvcSilvTradeModel
    prefix = "getRTMSDataSvcSilvTrade"
    schedule = "15 1 15 * *"


################################################################################
# [API] 오피스텔 매매 신고 조회 서비스
################################################################################
# Output Model
class RTMSDataSvcOffiTradeModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    거래금액: Optional[str]  # 만원
    년: Optional[str]  # 계약년도
    단지: Optional[str]  # 단지
    법정동: Optional[str]  # 법정동
    시군구: Optional[str]  # 시군구
    월: Optional[str]  # 계약월
    일: Optional[str]  # 계약일
    전용면적: Optional[str]  # 전용면적
    지번: Optional[str]  # 지번
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]  # 층
    해제여부: Optional[str]  # 해제여부
    해제사유발생일: Optional[str]  # 해제사유발생일
    거래유형: Optional[str]  # 중개 및 직거래 여부
    중개업소주소: Optional[str]  # 시군구 단위


# API
class RTMSDataSvcOffiTrade(RTMSOBJSvc):
    Model = RTMSDataSvcOffiTradeModel
    prefix = "getRTMSDataSvcOffiTrade"
    schedule = "30 1 15 * *"


################################################################################
# [API] 토지 매매 신고 조회 서비스
################################################################################
# Output Model
class RTMSDataSvcLandTradeModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    거래금액: Optional[str]  # 만원
    거래면적: Optional[str]  # 면적, sqm
    지분거래구분: Optional[str]  # 지분/공란
    년: Optional[str]  # 계약년도
    법정동: Optional[str]  # 법정동
    시군구: Optional[str]  # 시군구
    용도지역: Optional[str]  # 용도지역
    월: Optional[str]  # 계약월
    일: Optional[str]  # 계약일
    지목: Optional[str]  # 지목
    지역코드: Optional[str]  # 지역코드
    해제여부: Optional[str]  # 해제여부
    해제사유발생일: Optional[str]  # 해제사유발생일
    거래유형: Optional[str]  # 중개 및 직거래 여부
    중개업소주소: Optional[str]  # 시군구 단위


# API
class RTMSDataSvcLandTrade(RTMSOBJSvc):
    Model = RTMSDataSvcLandTradeModel
    prefix = "getRTMSDataSvcLandTrade"
    schedule = "45 1 15 * *"


################################################################################
# [API] 상업업무용 부동산 매매 신고 조회 서비스
################################################################################
# Output Model
class RTMSDataSvcNrgTradeModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    거래금액: Optional[str]  # 만원
    건물면적: Optional[str]  # 면적, sqm
    건물주용도: Optional[str]  # 건물주용도
    건축년도: Optional[str]  # 건축년도
    지분거래구분: Optional[str]  # 지분/공란
    년: Optional[str]  # 계약년도
    대지면적: Optional[str]  # 대지면적, sqm
    법정동: Optional[str]  # 법정동
    시군구: Optional[str]  # 시군구
    용도지역: Optional[str]  # 용도지역
    월: Optional[str]  # 계약월
    유형: Optional[str]  # 건물유형 (일반/집합)
    일: Optional[str]  # 계약일
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]  # 층
    해제여부: Optional[str]  # 해제여부
    해제사유발생일: Optional[str]  # 해제사유발생일
    거래유형: Optional[str]  # 중개 및 직거래 여부
    중개업소주소: Optional[str]  # 시군구 단위


# API
class RTMSDataSvcNrgTrade(RTMSOBJSvc):
    Model = RTMSDataSvcNrgTradeModel
    prefix = "getRTMSDataSvcNrgTrade"
    schedule = "0 2 15 * *"


################################################################################
# [API] 아파트 전월세 자료
################################################################################
# Output Model
class RTMSDataSvcAptRentModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    건축년도: Optional[str]  # 건축년도
    년: Optional[str]  # 계약년도
    법정동: Optional[str]  # 법정동
    보증금액: Optional[str]
    아파트: Optional[str]
    월: Optional[str]  # 계약월
    월세금액: Optional[str]
    일: Optional[str]  # 계약일
    전용면적: Optional[str]
    지번: Optional[str]
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]  # 층


# API
class RTMSDataSvcAptRent(RTMSOBJSvc8081):
    Model = RTMSDataSvcAptRentModel
    prefix = "getRTMSDataSvcAptRent"
    schedule = "15 2 15 * *"


################################################################################
# [API] 연립/다세대 전월세 자료
################################################################################
# Output Model
class RTMSDataSvcRHRentModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    건축년도: Optional[str]  # 건축년도
    년: Optional[str]  # 계약년도
    법정동: Optional[str]  # 법정동
    보증금액: Optional[str]
    연립다세대: Optional[str]
    월: Optional[str]  # 계약월
    월세금액: Optional[str]
    일: Optional[str]  # 계약일
    전용면적: Optional[str]
    지번: Optional[str]
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]  # 층


# API
class RTMSDataSvcRHRent(RTMSOBJSvc8081):
    Model = RTMSDataSvcRHRentModel
    prefix = "getRTMSDataSvcRHRent"
    schedule = "30 2 15 * *"


################################################################################
# [API] 단독/다가구 전월세 자료
################################################################################
# Output Model
class RTMSDataSvcSHRentModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    계약면적: Optional[str]  # 계약면적
    년: Optional[str]  # 계약년도
    법정동: Optional[str]  # 법정동
    보증금액: Optional[str]
    월: Optional[str]  # 계약월
    월세금액: Optional[str]
    일: Optional[str]  # 계약일
    지역코드: Optional[str]  # 지역코드


# API
class RTMSDataSvcSHRent(RTMSOBJSvc8081):
    Model = RTMSDataSvcSHRentModel
    prefix = "getRTMSDataSvcSHRent"
    schedule = "45 2 15 * *"


################################################################################
# [API] 오피스텔 전월세 자료
################################################################################
# Output Model
class RTMSDataSvcOffiRentModel(BaseModel):
    """
    API 문서에 자료형 정의되어 있지 않아 모두 String 간주 하였음.
    사용자가 Casting 할 것.
    """

    년: Optional[str]  # 계약년도
    단지: Optional[str]
    법정동: Optional[str]  # 법정동
    보증금: Optional[str]
    시군구: Optional[str]
    월: Optional[str]  # 계약월
    월세: Optional[str]
    일: Optional[str]  # 계약일
    전용면적: Optional[str]
    지번: Optional[str]
    지역코드: Optional[str]  # 지역코드
    층: Optional[str]


# API
class RTMSDataSvcOffiRent(RTMSOBJSvc):
    Model = RTMSDataSvcOffiRentModel
    prefix = "getRTMSDataSvcOffiRent"
    schedule = "0 3 15 * *"
