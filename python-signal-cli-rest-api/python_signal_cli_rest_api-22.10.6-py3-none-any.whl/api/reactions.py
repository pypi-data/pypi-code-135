"""
send message reactions to single contact
"""


from traceback import format_exc
from typing import Optional

from pydantic import BaseModel
from sanic import Blueprint
from sanic.exceptions import BadRequest
from sanic.log import logger
from sanic.response import json
from sanic_ext import openapi, validate

from python_signal_cli_rest_api.dataclasses import (
    ResponseBadRequest,
    ResponseTimestamps,
)
from python_signal_cli_rest_api.lib.jsonrpc import jsonrpc

reactions_v1 = Blueprint("reactions_v1", url_prefix="/reactions")


def send_reaction(
    number: str,
    reaction: str,
    remove: bool,
    recipient: str,
    target_author: str,
    timestamp: int,
    groupid: str = "",
):  # pylint: disable=too-many-arguments
    """
    send reaction
    """
    try:
        params = {
            "account": number,
            "emoji": reaction,
            "remove": remove,
            "targetAuthor": target_author,
            "targetTimestamp": timestamp,
            "recipient": recipient,
        }
        if groupid:
            params.update({"groupId": groupid})
        logger.info(params)
        result = jsonrpc({"method": "sendReaction", "params": params}).get("result", {})
        timestamp = result.get("timestamp")
        return {"timestamp": timestamp}, 200
    # pylint: disable=broad-except
    except Exception as exc:
        logger.error(format_exc())
        raise BadRequest("An eror occured. Please check gateway logs.") from exc


class ReactionsV1PostParams(BaseModel):
    """
    ReactionsV1PostParams
    """

    reaction: str
    target_author: str
    timestamp: int
    recipient: str
    groupid: Optional[str] = ""
    remove: Optional[bool] = False


@reactions_v1.post("/<number:path>", version=1)
@openapi.tag("Reactions")
@openapi.parameter("number", str, required=True, location="path")
@openapi.body({"application/json": ReactionsV1PostParams}, required=True)
@openapi.response(201, {"application/json": ResponseTimestamps}, description="Created")
@openapi.response(
    400, {"application/json": ResponseBadRequest}, description="Bad Request"
)
@openapi.description("Send a reaction.")
@validate(json=ReactionsV1PostParams)
async def reactions_v1_post(
    request, number, body: ReactionsV1PostParams
):  # pylint: disable=unused-argument
    """
    Send a reaction.
    """
    try:
        return_message, return_code = send_reaction(
            number=number,
            reaction=body.reaction,
            remove=body.remove,
            target_author=body.target_author,
            timestamp=body.timestamp,
            recipient=body.recipient,
            groupid=body.groupid,
        )
        return json(return_message, return_code)
    # pylint: disable=broad-except
    except Exception as exc:
        logger.error(format_exc())
        raise BadRequest("An eror occured. Please check gateway logs.") from exc


class ReactionsV1DeleteParams(BaseModel):
    """
    ReactionsV1DeleteParams
    """

    recipient: str
    target_author: str
    timestamp: int


@reactions_v1.delete("/<number:path>", ignore_body=False, version=1)
@openapi.tag("Reactions")
@openapi.parameter("number", str, required=True, location="path")
@openapi.body({"application/json": ReactionsV1DeleteParams}, required=True)
@openapi.response(200, {"application/json": ResponseTimestamps}, description="Deleted")
@openapi.response(
    400, {"application/json": ResponseBadRequest}, description="Bad Request"
)
@openapi.description("Delete a reaction.")
@validate(ReactionsV1DeleteParams)
async def reactions_v1_delete(
    request, number, body: ReactionsV1DeleteParams
):  # pylint: disable=unused-argument
    """
    Delete a reaction.
    """
    try:
        return_message, return_code = send_reaction(
            number=number,
            reaction="👍",
            remove=True,
            target_author=body.target_author,
            timestamp=body.timestamp,
            recipient=body.recipient,
        )
        return json(return_message, return_code)
    # pylint: disable=broad-except
    except Exception as exc:
        logger.error(format_exc())
        raise BadRequest("An eror occured. Please check gateway logs.") from exc
