"""
A comfier logging module.
"""

__all__ = ["init_logger"]

import logging
import sys
from dataclasses import dataclass
from logging import Logger, StreamHandler

from fontawesome import icons as fai

from libx.sty import get_andlog_fmt, get_orlog_fmt


@dataclass
class LogLevel:
    info: str = f"{fai['info-circle']}"
    # should be ban-bug
    debug: str = f"{fai['bug']}"

    warning: str = f"{fai['exclamation-circle']}"
    critical: str = f"{fai['exclamation-triangle']}"

    error: str = f"{fai['bug']}"
    notset: str = f"{fai['xing']}"

    def __post_init__(self):
        """
        Could you please make this nicer?
        """
        l = logging

        l.addLevelName(l.INFO, self.info)
        l.addLevelName(l.DEBUG, self.debug)
        l.addLevelName(l.ERROR, self.error)
        l.addLevelName(l.WARNING, self.warning)
        l.addLevelName(l.CRITICAL, self.critical)
        l.addLevelName(l.NOTSET, self.notset)


# Run loglevel side-effect
LogLevel()


def get_logger(level: int = logging.DEBUG, app: str = "default") -> Logger:
    logr = logging.getLogger(app)
    logr.setLevel(level)
    return logr


def get_handler(level: int = logging.DEBUG) -> StreamHandler:
    handlr = StreamHandler(sys.stdout)
    handlr.setLevel(level)
    return handlr


def init_logger(level: int = logging.DEBUG, app: str = "default") -> Logger:
    log4, handlr = get_logger(level, app), get_handler(level)

    fmt = logging.Formatter(
        get_orlog_fmt()
        | f"%(name)s [%(asctime)s - %(levelname)s]" + get_andlog_fmt()
        | " %(message)s",
        # Imagine if we could render a clock from  3 svgs just in time lol
        "%m-%d %H:%M:%S",
    )

    handlr.setFormatter(fmt)
    log4.addHandler(handlr)
    return log4
