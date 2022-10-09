"""
common dataclasses
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Error:
    """
    SearchV1Error
    """

    error: str


@dataclass
class ResponseBadRequest:
    """
    ResponseBadRequest
    """

    description: str
    status: int
    message: str


@dataclass
class Recipients:
    """
    Recipients
    """

    recipients: List[str]


@dataclass
class ResponseTimestamp:
    """
    ResponseTimestamp
    """

    timestamp: Recipients


@dataclass
class ResponseTimestamps:
    """
    ResponseTimestamps
    """

    timestamps: ResponseTimestamp


@dataclass
class GroupId:
    """
    GroupId
    """

    group_id: str
