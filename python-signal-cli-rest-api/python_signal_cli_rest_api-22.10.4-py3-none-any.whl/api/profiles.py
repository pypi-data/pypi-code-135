"""
Update Profile.
"""


from dataclasses import dataclass, field
from os import remove as os_remove
from traceback import format_exc
from typing import Optional
from uuid import uuid4

from sanic import Blueprint, Sanic
from sanic.log import logger
from sanic.response import json, text
from sanic_ext import openapi, validate

from python_signal_cli_rest_api.dataclasses import Error
from python_signal_cli_rest_api.lib.helper import do_decode_attachments
from python_signal_cli_rest_api.lib.jsonrpc import jsonrpc

update_profile_v1 = Blueprint("update_profile_v1", url_prefix="/profiles")


@dataclass
class UpdateProfileV1PutParams:
    """
    UpdateProfileV1PutParams
    """

    name: str
    family_name: Optional[str] = field(default_factory=str)
    base64_avatar: Optional[str] = field(default_factory=str)
    about: Optional[str] = field(default_factory=str)


@update_profile_v1.put("/<number:path>", version=1)
@openapi.tag("Profiles")
@openapi.body({"application/json": UpdateProfileV1PutParams}, required=True)
@openapi.response(204, None, description="Updated")
@openapi.response(400, {"application/json": Error}, description="Bad Request")
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
    except AttributeError:
        return json(
            {
                "error": "number missing in request and PYTHON_SIGNAL_CLI_REST_API_ unset "
            },
            400,
        )
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
    except Exception:
        logger.error(format_exc())
        return json({"error": "An eror occured. Please check gateway logs."}, 400)
    finally:
        os_remove(profile_avatar)
    return text("", 204)
