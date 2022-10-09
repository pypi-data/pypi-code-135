"""
configuration handler
"""

from enum import Enum
from traceback import format_exc
from typing import Optional

from pydantic import BaseModel
from sanic import Blueprint
from sanic.exceptions import BadRequest
from sanic.log import logger, logging
from sanic.response import json
from sanic_ext import openapi, validate

from python_signal_cli_rest_api.dataclasses import ResponseBadRequest

configuration_v1 = Blueprint("configuration_v1", url_prefix="/configuration")


class LoggingLevelChoices(str, Enum):
    """
    LoggingLevelChoices
    """

    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"


class LoggingV1Params(BaseModel):
    """
    LoggingV1Params
    """

    level: Optional[LoggingLevelChoices]


# pylint: disable=too-few-public-methods
class ConfigurationV1Params(BaseModel):
    """
    ConfigurationV1Params
    """

    logging: Optional[LoggingV1Params]


@configuration_v1.post("/", version=1)
@openapi.tag("Configuration")
@openapi.body({"application/json": ConfigurationV1Params}, required=True)
@openapi.response(
    200, {"application/json": ConfigurationV1Params}, description="Updated"
)
@openapi.response(
    400, {"application/json": ResponseBadRequest}, description="Bad Request"
)
@openapi.description("Set the REST API configuration.")
@validate(ConfigurationV1Params)
async def configuration_v1_post(
    request, body: ConfigurationV1Params
):  # pylint: disable=unused-argument
    """
    Set the REST API configuration.
    """
    level = do_configure_logging(body.logging.level.value)
    return json(
        ConfigurationV1Params(
            logging=LoggingV1Params(level=level).dict(),
        ).dict(),
        200,
    )


def do_configure_logging(level: str):
    """
    configure loglevel
    return current loglevel after configuration
    """
    if level:
        try:
            logger.info("Setting loglevel: %s", level)
            logger.setLevel(logging.getLevelName(level))
        # pylint: disable=broad-except
        except Exception as exc:
            logger.error(format_exc())
            raise BadRequest(
                "Unable to set loglevel, please check gateway logs."
            ) from exc
    return logging.getLevelName(logger.getEffectiveLevel())
