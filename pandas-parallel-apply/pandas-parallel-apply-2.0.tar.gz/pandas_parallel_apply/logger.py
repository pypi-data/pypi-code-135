"""Python logger settings."""

import os
import logging

# define custom logging levels
logging.DEBUG2 = 3
logging.addLevelName(logging.DEBUG2, "DEBUG-VERBOSE")
logging.__all__ += ["DEBUG2"]


class CustomFormatter(logging.Formatter):
    """Custom formatting for logger."""

    yellow = "\x1b[33;20m"
    green = "\x1b[32;20m"
    cyan = "\x1b[36;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    pre = "[%(asctime)s-%(name)s-%(levelname)s]"
    post = "(%(filename)s:%(funcName)s:%(lineno)d)"

    # Example [TIME:LEVEL:NAME] Message [FILE:FUNC:LINE]
    FORMATS = {
        logging.DEBUG: f"{cyan}{pre}{reset} %(message)s {yellow}{post}{reset}",
        logging.DEBUG2: f"{cyan}{pre}{reset} %(message)s {yellow}{post}{reset}",
        logging.INFO: f"{green}{pre}{reset} %(message)s {yellow}{post}{reset}",
        logging.WARNING: f"{yellow}{pre}{reset} %(message)s {yellow}{post}{reset}",
        logging.ERROR: f"{red}{pre}{reset} %(message)s {yellow}{post}{reset}",
        logging.CRITICAL: f"{bold_red}{pre}{reset} %(message)s {yellow}{post}{reset}",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class CustomLogger:
    """
    Custom logger.
    Attributes:
        name (str): Logger's name.
    Usage:
        Set the ``<NAME>_LOGLEVEL`` environment variable to control the logging level for the whole project.
        If not set, the default logging level is ``DEBUG`` (0 = no logging, 1 = info, 2 = debug, 3 = debug verbose).
    """

    log_levels = {0: logging.NOTSET, 1: logging.INFO, 2: logging.DEBUG, 3: logging.DEBUG2}

    def __init__(self, name: str = "PANDAS_PARALLEL_APPLY"):

        # initialize logger and set logging level
        self.logger = logging.getLogger(name)
        env_var = int(os.environ[f"{name}_LOGLEVEL"]) if f"{name}_LOGLEVEL" in os.environ else 2
        self.logger.setLevel(self.log_levels[env_var])
        self.logger.debug2 = lambda msg: self.logger.log(logging.DEBUG2, msg)

        # add custom formatter to logger
        handler = logging.StreamHandler()
        handler.setFormatter(CustomFormatter())
        self.logger.addHandler(handler)

    def get_logger(self):
        """Get logger."""
        return self.logger

    def set_level(self, level: int):
        """
        Change logging level: 0 = no logging, 1 = info, 2 = debug, 3 = debug verbose.
        """
        if 0 <= level <= 3:
            self.logger.setLevel(self.log_levels[level])
        else:
            raise ValueError("Unknown logging level.")


# global project logger
logger = CustomLogger().get_logger()
