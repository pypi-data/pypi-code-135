"""
logging configuration handler
"""

from dataclasses import dataclass
from enum import Enum
from traceback import format_exc

from sanic import Blueprint
from sanic.log import logger, logging
from sanic.response import json, text
from sanic_ext import openapi

from python_signal_cli_rest_api.dataclasses import Error

configuration_logging_v1 = Blueprint(
    "configuration_logging_v1", url_prefix="/configuration/logging"
)


@dataclass
class LoggingLevelChoices(Enum):
    """
    LoggingLevelChoices
    """

    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"


@configuration_logging_v1.post("/level/<level:path>", version=1)
@openapi.tag("Configuration")
@openapi.response(200, LoggingLevelChoices, description="OK")
@openapi.response(400, {"application/json": Error}, description="Bad Request")
@openapi.description(
    "Set the REST API logging level."
    f"`level` must be one of `{','.join(LoggingLevelChoices.__members__.keys())}`"
)
async def configuration_logging_v1_post(
    request, level: str
):  # pylint: disable=unused-argument
    """
    Set the REST API logging level.
    """
    # pylint: disable=no-member
    levels = {
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
    }
    if level not in levels:
        return json(
            {
                "error": f"invalid logging level '{level}', must be one of {levels.keys()}."
            },
            400,
        )
    try:
        logger.info("Setting loglevel: %s", level)
        logger.setLevel(levels.get(level))
    # pylint: disable=broad-except
    except Exception:
        logger.error(format_exc())
        return json({"error": "An eror occured. Please check gateway logs."}, 400)
    return text(
        dict((new_val, new_k) for new_k, new_val in levels.items()).get(
            logger.getEffectiveLevel()
        ),
        200,
    )
