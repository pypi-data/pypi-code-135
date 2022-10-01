import logging
from typing import Callable, Union

import aiohttp
import fastnumbers
from pydantic import BaseModel, HttpUrl

from ..utils import ResponseModel, generate_endpoint, generate_response_model
from .common import SERVICE_KEY
from .exceptions import DataGoKrException, DataGoKrResponseException, DataGoKrUnknownException, OpenApiServiceException

logger = logging.getLogger(__name__)

################################################################
# Helper
################################################################
# default parser
def parser(response: ResponseModel, Model: BaseModel = None):
    if "OpenAPI_ServiceResponse" in response.body:
        raise OpenApiServiceException(**response.body["OpenAPI_ServiceResponse"]["cmmMsgHeader"])
    if "response" not in response.body:
        raise DataGoKrUnknownException(response)
    if response.body["response"]["header"]["resultCode"] != "00":
        raise DataGoKrResponseException(**response.body["response"]["header"])
    if "body" not in response.body["response"]:
        return []
    body = response.body["response"]["body"]

    # empty records
    if body["items"] is None:
        if fastnumbers.int(body["totalCount"]) != 0:
            raise DataGoKrUnknownException(response)
        return []

    # records
    records = []
    items = body["items"]["item"]  # item에 1개 record만 담겨있는 경우 있음 (molit, RTMSDataSvcRHTrade)
    items = items if isinstance(items, list) else [items]
    for record in items:
        if Model:
            record = Model(**record)
        records += [{"key": response.request_info, "value": record}]

    return records


# update page no.
def update_pageNo(response: ResponseModel):
    try:
        body = response.body["response"]["body"]
        if fastnumbers.int(body["pageNo"]) * fastnumbers.int(body["numOfRows"]) < fastnumbers.int(body["totalCount"]):
            return fastnumbers.int(body["pageNo"]) + 1
    except KeyError as exc:
        pass
    return None


################################################################
# Abstract Client for DataGoKr
################################################################
# class DataGoKR
class DataGoKr:
    # override required
    prefix: str = None
    Model: BaseModel = None

    # fixed
    base_url: HttpUrl = "http://apis.data.go.kr"
    method: str = "GET"
    dataType: str = "JSON"
    numOfRows: int = 999
    parser: Callable = parser
    encrypt_fields: list = ["serviceKey"]

    def __init__(self, service_key: str = SERVICE_KEY, retries: int = 5):
        # properties
        self.service_key = service_key
        self.retries = retries

        # debug
        self._url = None
        self._params = None
        self._response = None

    async def get_records(self, path: str = None, **query_params):
        if self.Model:
            return await self.request(path=path, **query_params)
        raise NotImplementedError("Model Not Defined!")

    # request all pages
    async def request(self, path: Union[str, list] = None, **query):
        self._url = generate_endpoint(base_url=self.base_url, prefix=self.prefix, path=path)
        self._params = {
            "dataType": self.dataType,
            "numOfRows": self.numOfRows,
            "serviceKey": self.service_key,
            **{k: v for k, v in query.items() if v is not None},
        }
        logger.debug(f"request: {self.method} {self._url} {self._params}")

        # get records
        pageNo, records = 1, []
        async with aiohttp.ClientSession() as session:
            while True:
                self._params.update({"pageNo": pageNo})
                response = self._response = await self._request(
                    method=self.method,
                    url=self._url,
                    params=self._params,
                    session=session,
                )
                pageNo = update_pageNo(response=response)
                if parser:
                    Model = self.Model if self.Model else None
                    response = parser(response=response, Model=Model)
                records += response
                if pageNo is None:
                    break

        return records

    # single request
    async def _request(self, method: str, url: str, params: dict, session):
        for i in range(self.retries):
            try:
                async with session.request(method=method, url=url, params=params) as response:
                    response.raise_for_status()
                    return await generate_response_model(response, encrypt_fields=self.encrypt_fields)
            except OpenApiServiceException as exc:
                pass
