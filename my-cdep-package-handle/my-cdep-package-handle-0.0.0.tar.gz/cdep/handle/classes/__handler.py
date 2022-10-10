import sys, traceback, socket, json

from logging import Logger
from typing import Union, List
from pathlib import Path

from ..models import HandlerConfig, DeadMansConfig


class Handler:
    def __init__(self,
    config: HandlerConfig | None,
    deadmans_config: DeadMansConfig | None
) -> None:
        pass

    def raise_for_config(self):
        pass

    def raise_for_deadmans_config(self):
        pass

    def set_config(self, config: HandlerConfig):
        pass

    def set_deadmans_config(self, config: DeadMansConfig):
        pass

    def textplain(
        self,
        body: str,
        title: str,
        attachments: Union[List[Path], List[bytes]] = [],
    ):
        pass

    def json_text(
        self,
        subject: str,
        body: str,
        config: HandlerConfig | None,
        attachments: Union[List[Path], List[bytes]] = [],
    ):
        pass

    def deadmans_control_email(
        self,
        body: str,
        subject: str = "Connector Deadman's Control from",
        attachments: Union[List[Path], List[bytes]] = [],
    ):
        pass

    def object(
        self,
        message: str,
        object: dict | list,
        title: str = "Data Object has been raised for reviewing",
        exit_code=None,
    ):
        pass

    def exception(
        self,
        title: str = "An exception has been raised",
        exc_info: tuple = None,
        exit_code: int = None,
    ):
        pass
