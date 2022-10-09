"""
Update Profile.
"""


from os import remove as os_remove
from traceback import format_exc
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel
from sanic import Blueprint, Sanic
from sanic.exceptions import BadRequest
from sanic.log import logger
from sanic.response import json, text
from sanic_ext import openapi, validate

from python_signal_cli_rest_api.dataclasses import ResponseBadRequest
from python_signal_cli_rest_api.lib.helper import do_decode_attachments
from python_signal_cli_rest_api.lib.jsonrpc import jsonrpc

update_profile_v1 = Blueprint("update_profile_v1", url_prefix="/profiles")


class UpdateProfileV1PutParams(BaseModel):
    """
    UpdateProfileV1PutParams
    """

    name: str
    family_name: Optional[str]
    base64_avatar: Optional[str] = ""
    about: Optional[str] = ""


@update_profile_v1.put("/<number:path>", version=1)
@openapi.tag("Profiles")
@openapi.body({"application/json": UpdateProfileV1PutParams}, required=True)
@openapi.response(204, None, description="Updated")
@openapi.response(
    400, {"application/json": ResponseBadRequest}, description="Bad Request"
)
@openapi.description(("Set your name and optional an avatar."))
@validate(UpdateProfileV1PutParams)
async def update_profile_v1_put(
    request, number, body: UpdateProfileV1PutParams
):  # pylint: disable=unused-argument
    """
    Update Profile.
    """
    profile_avatar = ""
    app = Sanic.get_app()
    try:
        number = number or app.config.ACCOUNT
    except AttributeError as exc:
        raise BadRequest(
            "number missing in request and PYTHON_SIGNAL_CLI_REST_API_ unset"
        ) from exc
    uuid = str(uuid4())
    try:
        profile_avatar = do_decode_attachments([body.base64_avatar], uuid)[0]
    # pylint: disable=broad-except
    except IndexError:
        pass
    try:
        params = {
            "account": number,
            "givenName": body.name,
        }
        if profile_avatar:
            params.update({"avatarUrlPath": profile_avatar})
        if body.family_name:
            params.update({"familyName": body.family_name})
        if body.about:
            params.update({"about": body.about})
        res = jsonrpc({"method": "updateProfile", "params": params}).get("result")
        if res.get("error"):
            return json({"error": res.get("error")}, 400)
    # pylint: disable=broad-except
    except Exception as exc:
        logger.error(format_exc())
        raise BadRequest("An eror occured. Please check gateway logs.") from exc
    finally:
        os_remove(profile_avatar)
    return text("", 204)
