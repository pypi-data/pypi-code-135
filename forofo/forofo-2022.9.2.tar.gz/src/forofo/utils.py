import json
from datetime import datetime

import pendulum
import xmltodict
from croniter import croniter
from pydantic import BaseModel, HttpUrl

KST = pendulum.timezone("Asia/Seoul")

# RequestInfo Model (Request Info.)
class RequestInfoKeyModel(BaseModel):
    name: str
    headers: dict
    method: str
    scheme: str
    host: str
    path: str
    query: dict


# Response Model (Request Info.)
class ResponseModel(BaseModel):
    request_info: RequestInfoKeyModel
    status: int
    headers: dict
    content_type: str
    content: bytes
    body: dict


# get endpoint
def generate_endpoint(base_url, prefix=None, path=None):
    return "/".join([x.strip("/") for x in [base_url, prefix, path] if x])


# get last update
def get_last_update_datetime(dt, cron_expr: str):
    if not isinstance(dt, datetime):
        dt = datetime.fromisoformat(dt)
    tzinfo = dt.tzinfo
    iter = croniter(cron_expr, dt)
    return datetime.fromtimestamp(iter.get_prev(), tz=tzinfo)


# encrypt
def encrypt(x):
    n = len(x)
    s = n // 4
    return x[:s] + "*" * (n - s)


# genereate response model
async def generate_response_model(response, encrypt_fields=None):
    encrypt_fields = encrypt_fields or []
    query = {k: v if k not in encrypt_fields else encrypt(v) for k, v in response.request_info.url.query.items()}

    # read content
    content = await response.read()

    # parse content
    content_type = response.content_type
    if content_type in ["text/plain", "text/html"]:
        body = content.decode(response.get_encoding())
    elif content_type in ["application/json"]:
        body = json.loads(content)
    elif content_type in ["application/xml", "text/xml"]:
        body = xmltodict.parse(content.decode(response.get_encoding()))
    else:
        raise ReferenceError(content_type)

    return ResponseModel(
        request_info=RequestInfoKeyModel(
            scheme=response.request_info.url.scheme,
            name=response.request_info.url.name,
            headers=response.request_info.headers,
            method=response.request_info.method,
            host=response.request_info.url.host,
            path=response.request_info.url.path,
            query=query,
        ),
        status=response.status,
        headers=response.headers,
        content_type=content_type,
        content=content,
        body=body,
    )
