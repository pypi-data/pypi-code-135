import logging
import os
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, validator

from ..client import DataGoKr
from ..common import KST
from ...utils import get_last_update_datetime

# logging
logger = logging.getLogger(__file__)


################################################################################
# [API] 승강기 사고 및 고장 이력 정보
################################################################################
# Output Model
class AcndListModel(BaseModel):
    """원천 데이터의 자료형은 모두 str"""

    elevatorNo: Optional[str]  # 승강기 고유번호
    buldNm: Optional[str]  # 건물명
    address1: Optional[str]  # 건물주소1
    address2: Optional[str]  # 건물주소2
    sido: Optional[str]  # 시도
    sigungu: Optional[str]  # 시군구
    elvtrAsignNo: Optional[str]  # 승강기호기
    elvtrDiv: Optional[str]  # 승강기구분
    elvtrForm: Optional[str]  # 승강기형식
    elvtrDetailForm: Optional[str]  # 승강기세부형식
    elvtrKindNm: Optional[str]  # 승강기종류
    installationPlace: Optional[str]  # 설치장소
    shuttleFloorCnt: Optional[float]  # 운행층수
    ratedSpeed: Optional[float]  # 정격속도(m/s)
    liveLoad: Optional[float]  # 적재하중(kg)
    ratedCap: Optional[float]  # 최대정원(인승)
    companyNm: Optional[str]  # 제조업체
    frstInstallationDe: Optional[str]  # 최초설치일자
    installationDe: Optional[str]  # 설치일자
    occrDt: Optional[str]  # 발생일자
    accContentMeasure: Optional[str]  # 사고내용 및 응급 조치


# API
class AcdnList(DataGoKr):
    base_url = "http://openapi.elevator.go.kr"
    prefix = "/openapi/service/ElevatorAcdnService/getAcdnList"
    Model = AcndListModel
    dataType = "XML"
    schedule = "15 0 1 * *"

    async def get_records(
        self,
        dt: datetime = None,
        *,
        initInspctTime_sdt: str = None,
        initInspctTime_edt: str = None,
        elevator_no: str = None,
    ) -> List[AcndListModel]:
        """
        [NOTE]
        dt 입력한 경우 지난 3개월 간의 데이터 로드.

        Args:
            initInspctTime_sdt (str): e.g. "20220901"
            initInspctTime_edt (str): e.g. "20220930"

        Returns:
            List[AcndListModel]
        """
        if dt is not None or (initInspctTime_sdt is None and initInspctTime_edt is None):
            if dt is None:
                if dt is None:
                    dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
                initInspctTime_sdt = (dt - timedelta(days=61)).strftime("%Y%m%d")
                initInspctTime_edt = (dt - timedelta(days=1)).strftime("%Y%m%d")
        return await super().get_records(
            initInspctTime_sdt=initInspctTime_sdt,
            initInspctTime_edt=initInspctTime_edt,
            elevator_no=elevator_no,
        )


# TRANSLATE
TRANSLATE = {
    "occrDt": "발생일자",
    "accContentMeasure": "사고및조치내용",
    "installationDe": "설치일자",
    "frstInstallationDe": "최초설치일자",
    "sido": "시도",
    "sigungu": "시군구",
    "address1": "건물주소1",
    "address2": "건물주소2",
    "buldNm": "건물명",
    "elvtrDiv": "승강기구분",
    "elvtrForm": "승강기형식",
    "elvtrDetailForm": "승강기세부형식",
    "elvtrKindNm": "승강기종류",
    "elvtrAsignNo": "승강기호기",
    "installationPlace": "설치장소",
    "shuttleFloorCnt": "운행층수",
    "ratedSpeed": "정격속도(m/s)",
    "liveLoad": "적재하중(kg)",
    "ratedCap": "최대정원(인승)",
    "companyNm": "제조업체",
    "elevatorNo": "승강기고유번호",
}

# Data Type 추정 (원자료는 모두 str)
DATA_TYPES = {
    "occrDt": datetime,
    "accContentMeasure": str,
    "installationDe": datetime,
    "frstInstallationDe": datetime,
    "sido": str,
    "sigungu": str,
    "address1": str,
    "address2": str,
    "buldNm": str,
    "elvtrDiv": str,
    "elvtrForm": str,
    "elvtrDetailForm": str,
    "elvtrKindNm": str,
    "elvtrAsignNo": str,
    "installationPlace": str,
    "shuttleFloorCnt": float,
    "ratedSpeed": float,
    "liveLoad": float,
    "ratedCap": float,  # int w/ None
    "companyNm": str,
    "elevatorNo": str,
}
