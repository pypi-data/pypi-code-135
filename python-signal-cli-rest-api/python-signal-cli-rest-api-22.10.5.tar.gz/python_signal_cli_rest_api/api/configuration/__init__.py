"""
configuration handler
"""

from dataclasses import dataclass, field
from enum import Enum
from traceback import format_exc
from typing import Optional, Union

from sanic import Blueprint
from sanic.exceptions import BadRequest
from sanic.log import logger, logging
from sanic.response import json
from sanic_ext import openapi

from python_signal_cli_rest_api.dataclasses import ResponseBadRequest

configuration_v1 = Blueprint("configuration_v1", url_prefix="/configuration")


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


@dataclass
class LoggingV1ParamsDocs:
    """
    LoggingV1ParamsDocs
    """

    level: Optional[Union[LoggingLevelChoices, str]]


@dataclass
class LoggingV1ParamsValidate(LoggingV1ParamsDocs):
    """
    LoggingV1ParamsValidate
    """

    level: str = ""

    def __post_init__(self):
        self.validate_level()

    def validate_level(self):
        """
        validate level
        """
        if self.level:
            vals = [level.value for level in LoggingLevelChoices]
            if self.level not in vals:
                raise BadRequest(
                    f"level must be one of {','.join(LoggingLevelChoices.__members__.keys())}"
                )


@dataclass
class ConfigurationV1ParamsDocs:
    """
    ConfigurationV1ParamsDocs
    """

    logging: Optional[LoggingV1ParamsDocs] = field(default_factory=dict)


@dataclass
class ConfigurationV1ParamsValidate:
    """
    ConfigurationV1ParamsValidate
    """

    logging: Optional[LoggingV1ParamsValidate] = field(default_factory=dict)


@dataclass
class LoggingV1Response:
    """
    LoggingV1Response
    """

    level: str


@dataclass
class ConfigurationV1Response:
    """
    ConfigurationV1Response
    """

    logging: LoggingV1ParamsDocs


@configuration_v1.post("/", version=1)
@openapi.tag("Configuration")
@openapi.body({"application/json": ConfigurationV1ParamsDocs}, required=True)
@openapi.response(
    200, {"application/json": ConfigurationV1Response}, description="Updated"
)
@openapi.response(
    400, {"application/json": ResponseBadRequest}, description="Bad Request"
)
@openapi.description("Set the REST API configuration.")
async def configuration_v1_post(
    request, body: ConfigurationV1ParamsValidate
):  # pylint: disable=unused-argument
    """
    Set the REST API configuration.
    """
    level = do_configure_logging(body.logging.level)
    return json(
        ConfigurationV1Response(
            logging=LoggingV1Response(level=level).__dict__,
        ).__dict__,
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
