import asyncio
import json
import logging
from typing import Callable, Union

import aiohttp
import fastnumbers
import xmltodict
from pydantic import BaseModel, HttpUrl

from ..utils import generate_endpoint, generate_response_model, ResponseModel

from .common import SERVICE_KEYS
from .exceptions import (
    LocalDataException,
    LocalDataResponseException,
    LocalDataUnknownException,
    OpenApiServiceException,
)

logger = logging.getLogger(__name__)

################################################################
# Helper
################################################################
# update page no.
def update_pageIndex(response: ResponseModel):
    try:
        paging = response.body["result"]["header"]["paging"]
        if fastnumbers.int(paging["pageIndex"]) * fastnumbers.int(paging["pageSize"]) < fastnumbers.int(
            paging["totalCount"]
        ):
            return fastnumbers.int(paging["pageIndex"]) + 1
    except KeyError as exc:
        pass
    return None


# default parser
def parser(response: ResponseModel, Model: BaseModel = None):
    if "OpenAPI_ServiceResponse" in response.body:
        raise OpenApiServiceException(**response.body["OpenAPI_ServiceResponse"]["cmmMsgHeader"])
    if "result" not in response.body:
        raise LocalDataUnknownException(response)
    if response.body["result"]["header"]["process"]["code"] != "00":
        raise LocalDataResponseException(**response.body["result"]["header"])
    if "body" not in response.body["result"]:
        return []
    body = response.body["result"]["body"]

    # empty records
    if body["rows"] is None:
        if fastnumbers.int(response.body["result"]["header"]["paging"]["totalCount"]) != 0:
            raise LocalDataUnknownException(response)
        return []

    # records
    records = []
    for rows in body["rows"]:
        for record in rows["row"]:
            if Model:
                record = Model(**record)
            records += [{"key": response.request_info, "value": record}]
    return records


################################################################
# Client for LocalData
################################################################
# class LocalData
class LocalData:
    # override required
    prefix: str = None
    Model: BaseModel = None

    # fixed
    base_url: HttpUrl = "http://www.localdata.go.kr/platform/rest/GR0"
    prefix: str = "openDataApi"
    method: str = "GET"
    resultType: str = "JSON"
    pageSize: int = 999
    parser: Callable = parser
    encrypt_fields: list = ["authKey"]

    def __init__(self, service_keys: str = SERVICE_KEYS):
        # properties
        self.service_keys = service_keys

        # debug
        self._url = None
        self._params = None
        self._response = None

    async def get_records(self, group_name: str, **query_params):
        authKey = self.service_keys[group_name]
        return await self.request(Model=self.Model, path=None, authKey=authKey, **query_params)

    # request all pages
    async def request(self, Model: BaseModel = None, path: Union[str, list] = None, **query):
        self._url = generate_endpoint(base_url=self.base_url, prefix=self.prefix, path=path)
        self._params = {
            "resultType": self.resultType,
            "pageSize": self.pageSize,
            **{k: v for k, v in query.items() if v is not None},
        }
        logger.debug(f"request: {self.method} {self._url} {self._params}")

        # get records
        pageIndex, records = 1, []
        async with aiohttp.ClientSession() as session:
            while True:
                self._params.update({"pageIndex": pageIndex})
                response = self._response = await self._request(
                    method=self.method,
                    url=self._url,
                    params=self._params,
                    session=session,
                )
                pageIndex = update_pageIndex(response=response)
                if parser:
                    response = parser(response=response, Model=Model)
                records += response
                if pageIndex is None:
                    break

        return records

    # single request
    async def _request(self, method: str, url: str, params: dict, session):
        async with session.request(method=method, url=url, params=params) as response:
            response.raise_for_status()
            return await generate_response_model(response, encrypt_fields=self.encrypt_fields)
