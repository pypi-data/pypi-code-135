# ------------------------------------------------------------------------------
#  es7s [setup/configuration/commons]
#  (c) 2021-2022 A. Shavykin <0.delameter@gmail.com>
# ------------------------------------------------------------------------------
from __future__ import annotations

import logging
import os
import sys
from logging import Logger, StreamHandler, Formatter, DEBUG, WARNING, INFO, ERROR, LogRecord, CRITICAL
from logging.handlers import SysLogHandler
from typing import Literal, cast

from pytermor import Colors, Style, NOOP_STYLE, Styles

from . import APP_NAME, APP_VERSION


class Es7sStderrHandler(StreamHandler):
    def handle(self, record: LogRecord):
        super().handle(record)
        # reset cached exc_text after Es7sStderrFormatter
        # so that syslog won't receive SGRs
        record.exc_text = None


class Es7sSysLogHandler(SysLogHandler):
    def __init__(self, ident: str, **kwargs):
        super().__init__(**kwargs)
        self.ident = f"{APP_NAME}/{ident}[{os.getpid()}]: "


class Es7sStderrFormatter(Formatter):
    STYLE_DEFAULT = NOOP_STYLE
    STYLE_EXCEPTION = Styles.ERROR
    LEVEL_TO_STYLE_MAP = {
        CRITICAL: Styles.CRITICAL,
        ERROR: Styles.ERROR_ACCENT,
        WARNING: Styles.WARNING,
        INFO: Style(fg=Colors.WHITE),
        DEBUG: Style(fg="medium_purple_7"),
    }

    def __init__(self, show_exc_info: bool, **kwargs):
        super().__init__(**kwargs)
        self._show_exc_info = show_exc_info

    def formatMessage(self, record: LogRecord):
        formatted_msg = super().formatMessage(record)
        style = self._resolve_style(record.levelno)
        return style.render(f"[{record.levelname:5.5s}]" + formatted_msg)

    def formatException(self, ei):
        if not self._show_exc_info:
            return None
        formatted = super().formatException(ei)
        result = "\n".join(self.STYLE_EXCEPTION.render(line) for line in formatted.splitlines(keepends=False))
        return result

    def _resolve_style(self, log_level: int | Literal) -> Style:
        return self.LEVEL_TO_STYLE_MAP.get(log_level, self.STYLE_DEFAULT)


class Es7sLogger(Logger):
    QUIET = 100
    VERBOSITY_TO_LOG_LEVEL_MAP = {   #  ARGS    STDERR                           SYSLOG
                                     #  -q      nothing                          <determined by verbosity>
        0: [WARNING, INFO],          #          error (brief), warn              err, warn, info
        1: [INFO,    INFO],          #  -v      error (+traceback), warn, info   err, warn, info
        2: [DEBUG,   DEBUG],         #  -vv     full-debug                       full-debug
    }
    VERBOSITY_MAX_VALUE = 2

    def setup(self, ident: str, subname: str, quiet: bool, verbose: int):
        verbosity_index = min(self.VERBOSITY_MAX_VALUE, verbose)
        stderr_log_level, syslog_log_level = self.VERBOSITY_TO_LOG_LEVEL_MAP[verbosity_index]
        self.setLevel(min(stderr_log_level, syslog_log_level))

        if not quiet:
            stderr_prefix = f'[{subname}]' if verbosity_index > 0 else ''
            stderr_fmt = stderr_prefix + ' %(message)s'
            stderr_show_exc_info = (verbosity_index > 0)

            stderr_formatter = Es7sStderrFormatter(show_exc_info=stderr_show_exc_info, fmt=stderr_fmt)
            stream_handler = Es7sStderrHandler(stream=sys.stderr)
            stream_handler.setLevel(stderr_log_level)
            stream_handler.setFormatter(stderr_formatter)
            self.addHandler(stream_handler)

        syslog_formatter = Formatter(fmt=f'[{subname}] %(message)s [%(filename)s:%(lineno)d]')
        syslog_handler = Es7sSysLogHandler(ident, address='/dev/log', facility=SysLogHandler.LOG_LOCAL7)
        syslog_handler.setFormatter(syslog_formatter)
        self.addHandler(syslog_handler)

    def exception(self, msg: object, **kwargs):
        msg = f'{msg.__class__.__qualname__}: {msg!s}'
        super().exception(msg)

    def print_args(self, var: str) -> str:
        if hasattr(sys, var):
            return str(tuple(getattr(sys, var)))
        return '<N/A>'


def setup(ident: str, subname: str|None, quiet: bool, verbose: int) -> Es7sLogger:
    logging.setLoggerClass(Es7sLogger)
    logger_name = 'es7s' + ('.' + subname if subname else '')
    logger = cast(Es7sLogger, logging.getLogger(logger_name))
    logger.setup(ident, subname, quiet, verbose)

    logger.info(f'Initialized {logger.__class__.__qualname__} with {(ident, subname, quiet, verbose)}')
    logger.info(f'App version: {APP_NAME} v{APP_VERSION}')
    logger.info(f'App original args: {logger.print_args("orig_argv")}')  # since python 3.10
    logger.info(f'App current args: {logger.print_args("argv")}')
    return logger

# resulting syslog output (partial):

    # _TRANSPORT=syslog
    # PRIORITY=7                       # logs filtering:
    # SYSLOG_FACILITY=23               #    "journalctl --facility=local7" (all es7s logs are sent to this facility)
    # _UID=1001                        # or "journalctl --ident=es7s/corectl" (that's "APP_NAME/ident")
    # _GID=1001                        # or "journalctl --grep InstallCommand" ("source", usually command subname) [DEBUG ONLY]
    # _EXE=/usr/bin/python3.10
    # _CMDLINE=/home/a.shavykin/.local/pipx/venvs/es7s/bin/python /home/a.shavykin/.local/bin/es7s corectl install
    # _COMM=es7s
    # SYSLOG_PID=846461
    # SYSLOG_IDENTIFIER=es7s/corectl
    # MESSAGE=[InstallCommand] Initialized with (verbose=0 quiet=False c=False color=None) [log.py:92]
