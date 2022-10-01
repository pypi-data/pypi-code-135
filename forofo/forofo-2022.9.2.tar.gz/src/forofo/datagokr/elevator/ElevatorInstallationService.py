import logging
import os
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, validator

from ...utils import get_last_update_datetime
from ..client import DataGoKr
from ..common import KST

# logging
logger = logging.getLogger(__file__)


################################################################################
# [API] 승강기 설치 정보
################################################################################
# Output Model
class InstallationElvtrListModel(BaseModel):
    elevatorNo: Optional[str] # 승강기 고유번호
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
    bdmgtSn: Optional[str]  # 국가건물관리번호


# API
class InstallationElvtrList(DataGoKr):
    base_url = "http://openapi.elevator.go.kr"
    prefix = "openapi/service/ElevatorInstallationService/getInstallationElvtrList"
    Model = InstallationElvtrListModel
    dataType = "XML"
    schedule = "15 0 1 * *"

    async def get_records(
        self, dt: datetime = None, *, Installation_sdt: str = None, Installation_edt: str = None
    ) -> List[InstallationElvtrListModel]:
        """
        Args:
            Installation_sdt (str): e.g. "20220901"
            Installation_edt (str): e.g. "20220930"

        Returns:
            List[InstallationElvtrListModel]
        """
        if dt is not None or (Installation_sdt is None and Installation_edt is None):
            if dt is None:
                if dt is None:
                    dt = get_last_update_datetime(datetime.now(tz=KST), cron_expr=self.schedule)
                Installation_sdt = (dt - timedelta(days=61)).strftime("%Y%m%d")
                Installation_edt = (dt - timedelta(days=1)).strftime("%Y%m%d")
        return await super().get_records(
            Installation_sdt=Installation_sdt,
            Installation_edt=Installation_edt,
        )


# TRANSLATE
TRANSLATE = {
    "installationDe": "설치일자",
    "frstInstallationDe": "최초설치일자",
    "sido": "시도",
    "sigungu": "시군구",
    "address1": "건물주소1",
    "address2": "건물주소2",
    "buldNm": "건물명",
    "bdmgtSn": "국가건물관리번호",
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
    "installationDe": datetime,
    "frstInstallationDe": datetime,
    "sido": str,
    "sigungu": str,
    "address1": str,
    "address2": str,
    "buldNm": str,
    "bdmgtSn": str,
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
