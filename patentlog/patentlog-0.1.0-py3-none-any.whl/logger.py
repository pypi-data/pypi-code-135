"""Provides a logger for console logging."""

from enum import Enum
import datetime
import logging
import sys
import uuid


class Levels(Enum):
    """Logging levels."""

    DEBUG = "-1"
    INFO = "0"
    ERROR = "1"
    CRITICAL = "2"


class Logger:
    def __init__(
        self, log_format: str, job_name: str, env: str, log_level: str = "DEBUG"
    ):
        self._log_format = log_format
        self._job_name = job_name
        self._env = env
        self._log_level = log_level
        self._uuid = uuid.uuid1()
        self._logger = logging.getLogger(self._job_name)
        self._set_minimal_log_level()
        self._chandler = logging.StreamHandler(sys.stdout)
        self._format = logging.Formatter(self._log_format)
        self._chandler.setFormatter(self._format)
        self._logger.addHandler(self._chandler)
        self._extra = {"uuid": self._uuid, "env": self._env}

    def debug(self, msg: str) -> None:
        self._set_level(Levels.DEBUG)
        self._set_time()
        self._logger = logging.LoggerAdapter(self._logger, self._extra)
        self._logger.debug(self._process(msg))

    def info(self, msg: str) -> None:
        self._set_level(Levels.INFO)
        self._set_time()
        self._logger = logging.LoggerAdapter(self._logger, self._extra)
        self._logger.info(self._process(msg))

    def error(self, msg: str) -> None:
        self._set_level(Levels.ERROR)
        self._set_time()
        self._logger = logging.LoggerAdapter(self._logger, self._extra)
        self._logger.error(self._process(msg))

    def critical(self, msg: str) -> None:
        self._set_level(Levels.CRITICAL)
        self._set_time()
        self._logger = logging.LoggerAdapter(self._logger, self._extra)
        self._logger.critical(self._process(msg))

    def _set_level(self, level: Levels) -> None:
        self._extra["level"] = level.value

    def _set_time(self):
        self._extra["time"] = datetime.datetime.now().isoformat()[:-3]

    def _set_minimal_log_level(self) -> None:
        mapper = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }
        self._logger.setLevel(mapper[self._log_level])

    def _process(self, msg: str) -> str:
        return msg.replace("\n", " ").replace("\r", "")