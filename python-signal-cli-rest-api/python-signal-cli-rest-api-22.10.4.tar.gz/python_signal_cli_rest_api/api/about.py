"""
about
"""

from dataclasses import dataclass
from typing import List

from sanic import Blueprint
from sanic.response import json
from sanic_ext import openapi

from python_signal_cli_rest_api.lib.jsonrpc import jsonrpc

about_v1 = Blueprint("about_v1", url_prefix="/about")


@dataclass
class AboutGetV1Params:
    """
    AboutGetV1Params
    """

    mode: str
    versions: List[str]
    signal_cli: str


@about_v1.get("/", version=1)
@openapi.tag("General")
@openapi.response(
    200,
    {"application/json": AboutGetV1Params},
    description="OK",
)
@openapi.description("Returns the supported API versions.")
async def about_v1_get(request):  # pylint: disable=unused-argument
    """
    Lists general information about the API.
    """
    signal_cli = jsonrpc({"method": "version"}).get("result").get("version")
    return json(
        {
            "mode": "json-rpc",
            "versions": ["v1", "v2"],
            "signal_cli": signal_cli,
        },
        200,
    )
