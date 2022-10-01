import asyncio
import logging
import logging.config
import os
from typing import Callable, Union

import aiohttp
import parse
from pydantic import BaseModel, HttpUrl

from ..utils import generate_endpoint
from . import parser
from .common import CyclicApiKey

logger = logging.getLogger(__name__)


class KmaUrlApiException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class _KmaUrlApiClient:
    base_url: HttpUrl = "http://203.247.66.126:8090/url"
    prefix: str = None
    method: str = "GET"
    dataType: str = "JSON"
    Model: BaseModel = None

    def __init__(
        self,
        service_key: Union[str, CyclicApiKey] = CyclicApiKey(),
        default_timeout: float = 10.0,
        default_retries: int = 6,
    ):
        # properties
        self.service_key = service_key
        self.default_timeout = default_timeout
        self.default_retries = default_retries

        # debug
        self._endpoint = None
        self._response = None

    async def get_records(self, **query_params):
        if self.Model:
            records = await self.request(path=None, **query_params)
            return [self.Model(**r) for r in records]
        raise NotImplementedError("Model Not Defined!")

    # request all pages
    async def request(
        self,
        prefix: str = None,
        path: str = None,
        parser: Callable = None,
        timeout: float = None,
        retries: int = None,
        **kwargs,
    ):
        # for debug
        self._endpoint = generate_endpoint(
            base_url=self.base_url,
            prefix=prefix,
            path=path,
        )
        self._params = {
            "authKey": self.service_key() if isinstance(self.service_key, CyclicApiKey) else self.service_key,
            **{k: v for k, v in kwargs.items() if v is not None},
        }
        timeout = timeout or self.default_timeout
        retries = retries or self.default_retries

        async with aiohttp.ClientSession() as session:
            n_try = 0
            while True:
                n_try += 1
                try:
                    self._response = await self._request(
                        method=self.method,
                        url=self._endpoint,
                        params=self._params,
                        session=session,
                        timeout=timeout,
                        parser=parser,
                    )
                    break
                except asyncio.exceptions.TimeoutError as exc:
                    if n_try > retries:
                        raise exc
                    logger.info(f"request timeout. retry {n_try}/{retries})")
                    pass

        return self._response

    # single request
    async def _request(
        self,
        session: aiohttp.ClientSession,
        method: str,
        url: str,
        params: dict = None,
        timeout: float = None,
        parser: Callable = None,
    ):
        async with session.request(method=method, url=url, params=params, timeout=timeout) as response:
            response.raise_for_status()

            # text response - list of files
            if response.content_type in ["text/plain"]:
                body = await response.text()

            # json response
            elif response.content_type in ["application/json"]:
                body = await response.json()

            # file download
            elif response.content_type in ["application/octet-stream", "application/x-zip-compressed"]:
                content_disposition = response.headers["content-disposition"]
                filename = parse.parse('attachment; filename="{filename}";', content_disposition).named["filename"]

                # download
                content = await response.read()
                if len(content) != response.content_length:
                    raise EOFError(f"download incomplete - {len(content)} / {response.content_length}")

                body = {"filename": filename, "content": content}

            # unknown content type
            else:
                raise KmaUrlApiException(message=f"unknown Content-Type {response.content_type}")

            if parser:
                body = parser(body)

            return body

    @staticmethod
    async def _write(filepath: str, content: bytes):
        with open(filepath, "wb") as f:
            f.write(content)


class KmaUrlApiClient(_KmaUrlApiClient):
    ################################################################
    # 수치모델
    ################################################################
    # 수치모델 파일 목록
    async def get_nwp_file_list(
        self,
        tmfc: str,
        nwp: str = "UMKR",
        format: str = "GRIP",
        filter: str = "unis",
        timeout: float = 5.0,
        retries: int = 6,
        parser: Callable = parser.nwp_file_list,
    ):
        return await self.request(
            prefix="nwp_file_list.php",
            tmfc=tmfc,
            nwp=nwp,
            format=format,
            filter=filter,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )

    # 수치모델 파일 다운로드
    async def download_nwp_file(
        self,
        filename: str,
        timeout: float = 30,
        retries: int = 10,
        parser: Callable = parser.download_nwp_file,
    ):
        return await self.request(
            prefix="nwp_file_down.php",
            file=filename,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )

    ################################################################
    # 위성
    ################################################################
    # 천리안 위성
    async def sat_coms_obs_file(
        self,
        tm: str,
        ch: str,
        map: str,
        timeout: float = 10.0,
        retries: int = None,
        parser: Callable = parser.sat,
    ):
        """천리안 위성 기본관측자료.

        Args:
            tm (str): 년월일시분(KST). e.g. "202010101400".
            ch (str): ir1(적외1), ir2(적외2), wv(수증기), swir(단파적외), vis(가시).
            map (str): ea(동아시아), ko(한반도).

        Returns:
            (bin 파일)
        """
        return await self.request(
            prefix="sat_coms_obs_file.php",
            tm=tm,
            ch=ch,
            map=map,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )

    # 천리안 2호 위성
    async def sat_gk2a_obs_file(
        self,
        tm: str,
        ch: str,
        map: str,
        timeout: float = 10.0,
        retries: int = None,
        parser: Callable = parser.sat,
    ):
        """천리안 위성 기본관측자료.

        Args:
            tm (str): 년월일시분(KST). e.g. "202010101400".
            ch (str):
                [적외] ir087(적외 8.7μm), ir096, ir105, ir112, ir123, ir133,
                [근적외] nr013(근적외 1.37μm), nr016,
                [단파적외] sw038(단파적외 3.8μm),
                [가시] vi004(가시 0.47μm), vi005, vi006, vi008,
                [수증기] wv063(수증기 6.3μm), wv069, wv073,
                [주야간합성] rgb-daynight(RGB 주야간 합성),
                [RGB황사] rgb-dust(RGB 황사).
            map (str): ea(동아시아), ko(한반도).

        Returns:
            (NetCDF 파일)
        """
        return await self.request(
            prefix="sat_gk2a_obs_file.php",
            tm=tm,
            ch=ch,
            map=map,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )

    # 위성자료 기본산출물
    async def sat_gk2a_ana_file(
        self,
        tm: str,
        ch: str,
        map: str,
        timeout: float = 10.0,
        retries: int = None,
        parser: Callable = parser.sat,
    ):
        """천리안 위성 기본관측자료.

        Args:
            tm (str): 년월일시분(KST). e.g. "202010101400".
            ch (str):
                aii(대기불안정도), adps(에어로졸 산출물), ci(대류운 탐지), cla(구름분석),
                cld(구름탐지), ctps(운정산출물), dcoew(주간구름 산출물), ff(산불탐지),
                fog(안개), lst(지표면온도), lwrad(장파복사), rr(강우강도), scsi(적설/해빙),
                sst(해수면온도), swrad(단파복사), toz(총오존량), tpw(총가강수량)
            map (str): ea(동아시아), ko(한반도).

        Returns:
            (NetCDF 파일)
        """
        return await self.request(
            prefix="sat_gk2a_ana_file.php",
            tm=tm,
            ch=ch,
            map=map,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )

    # 천리안2A 인공지능 기반 한반도 일사량 자료
    async def sat_ana_txt(
        self,
        tm: str,
        obs: str = "si_ai",
        help: int = 1,
        timeout: float = 10.0,
        retries: int = None,
        parser: Callable = parser.sat_ana_txt,
    ):
        """천리안 위성 기본관측자료.

        Args:
            tm (str): 년월일시분(KST). e.g. "202010101400".
            obs (str): "si_ai" 고정값.
            help (int): 0 도움말 없음, 1 도움말 표출.

        Returns:
            (?)
        """
        return await self.request(
            prefix="cgi-bin/sat/nph-sat_ana_txt",
            tm=tm,
            obs=obs,
            help=help,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )

    # 천리안2A 인공지능 기반 한반도 일사량 자료 파일 다운로드
    async def sat_file_down(
        self,
        tm: str,
        typ: str,
        lvl: str = "l2",
        dat: str = "ai-dsr",
        are: str = "ko",
        timeout: float = 10.0,
        retries: int = None,
        parser: Callable = parser.sat,
    ):
        """천리안2A 인공지능 기반 한반도 일사량 자료 파일 다운로드

        Args:
            tm (str): 기준시각 yyyymmddhhmm (UTC), 1시간 간격. e.g. "202203101000".
            typ (str): "bin" (nc파일), "img" (png이미지).
            lvl (str, optional): "l2" (레벨/고정).
            dat (str, optional): "ai-dsr" (인공지능기반일사자료/고정).
            are (str, optional): "ko" (한반도/고정).

        Returns:
            _type_: _description_
        """
        return await self.request(
            prefix="sat_file_down.php",
            tm=tm,
            typ=typ,
            lvl=lvl,
            dat=dat,
            are=are,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )

    ################################################################
    # 레이더
    ################################################################
    # 사이트
    async def rdr_site_file(
        self,
        tm: str,
        data: str,
        stn: str,
        timeout: float = 10.0,
        retries: int = None,
        parser: Callable = parser.rdr,
    ):
        """사이트

        Args:
            tm (str): 기준시각 yyyymmddhhmm (UTC), 1시간 간격. e.g. "202107151200".
            data (str): "qcd" 레이더, "raw" 원시자료, "img" 이미지.
            stn (str, optional): 레이더지점코드.
                성산 SSP, 구덕산 PSN, 면봉산 MYN, 관악산 KWK, 백령도 BRI, 오성산 KSN,
                진도 JNI, 광덕산 GDK, 강릉 GNG, 고산 GSN.

        Returns:
            _type_: _description_
        """
        return await self.request(
            prefix="rdr_site_file.php",
            tm=tm,
            data=data,
            stn=stn,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )

    # 합성
    async def rdr_cmp_file(
        self,
        tm: str,
        data: str,
        cmp: str,
        timeout: float = 10.0,
        retries: int = None,
        parser: Callable = parser.rdr,
    ):
        """사이트

        Args:
            tm (str): 기준시각 yyyymmddhhmm (UTC), 1시간 간격. e.g. "202107151200".
            data (str): "bin" 이진, "img" 이미지.
            cmp (str, optional):
                이진 - cpp, ppi, cmx, hsr, hsp.
                이미지 - cmb, cmc, cmi.

        Returns:
            _type_: _description_
        """
        return await self.request(
            prefix="rdr_cmp_file.php",
            tm=tm,
            data=data,
            cmp=cmp,
            timeout=timeout,
            retries=retries,
            parser=parser,
        )
