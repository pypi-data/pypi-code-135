"""
The REST api for the worker image
"""

import typing
import logging

import fastapi

LOG = logging.getLogger("worker")
from typing import TypedDict, Optional

# Add any important metrics here to have them statically checked
InfoLog = TypedDict("InfoLog", {"active_renders": int})


# API definitions
api = fastapi.FastAPI()


@api.get("/")
async def info_response() -> InfoLog:
    """
    Endpoint for retrieving metadata from this instance

    :return: full any relevant info points for this instance
    """
    return InfoLog(active_renders=0)


@api.get("/health-check")
async def health_check() -> dict[str, str]:
    """
    Health check endpoint for the status of the API

    :return: A health message
    """
    return {"message": "Healthy!"}

