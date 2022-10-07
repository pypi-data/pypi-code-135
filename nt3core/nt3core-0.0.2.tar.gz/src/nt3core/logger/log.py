"""Log method to unify log messages """
import traceback
import sys
from enum import Enum
from src.nt3core.logger.log_context import ctx


class LogType(Enum):
    """Log types for Log Messages"""
    DEBUG = 0
    INFO = 1
    CRITICAL = 2
    ERROR = 3
    FATAL = 4
    WARNING = 5


# region Public methods

def log_debug(logger, app: str = "Default", message: str = "", trace_id: bool = False):
    """
    Writes a debug log entry
    :type trace_id: bool
    :param trace_id: Also log a trace id of the current thread
    :type message: str
    :type app: str
    :param logger: Reference to used logger
    :param app: Application writing to log, defaults to "Default"
    :param message: Log message, Defaults to ""
    """
    _log(logger=logger, logtype=LogType.DEBUG, app=app, message=message, stacktrace=False, trace_id=trace_id)


def log_warning(logger, app: str = "Default", message: str = "", trace_id: bool = False):
    """
    Writes a warning log entry
    :type trace_id: bool
    :param trace_id: Also log a trace id of the current thread
    :type message: str
    :type app: str
    :param logger: Reference to used logger
    :param app: Application writing to log, defaults to "Default"
    :param message: Log message, defaults to ""
    """
    _log(logger=logger, logtype=LogType.WARNING, app=app, message=message, stacktrace=False, trace_id=trace_id)


def log_info(logger, app: str = "Default", message: str = "", trace_id: bool = ""):
    """
    Writes an info log entry
    :type trace_id: bool
    :param trace_id: Also log a trace id of the current thread
    :type message: str
    :type app: str
    :param logger: Reference to used logger
    :param app: Application writing to log, defaults to "Default"
    :param message: Log message, defaults to ""
    """
    _log(logger=logger, logtype=LogType.INFO, app=app, message=message, stacktrace=False, trace_id=trace_id)


def log_critical(logger, app: str = "Default", message: str = "", stacktrace: bool = True, trace_id: bool = False):
    """
    Writes a critical log entry
    :type trace_id: bool
    :param trace_id: Also log a trace id of the current thread
    :type stacktrace: bool
    :type message: str
    :type app: str
    :param logger: Reference to used logger
    :param app: Application writing to log, defaults to "Default"
    :param message: Log message, defaults to ""
    :param stacktrace: Also write stack information
    """
    _log(logger=logger, logtype=LogType.CRITICAL, app=app, message=message, stacktrace=stacktrace, trace_id=trace_id)


def log_error(logger, app: str = "Default", message: str = "", stacktrace: bool = True, trace_id: bool = False):
    """
    Writes an error log entry
    :type trace_id: bool
    :param trace_id: Also log a trace id of the current thread
    :type stacktrace: bool
    :type message: str
    :type app: str
    :param logger: Reference to used logger
    :param app: Application writing to log, defaults to "Default"
    :param message: Log message, defaults to ""
    :param stacktrace: Also write stack information
    """
    _log(logger=logger, logtype=LogType.ERROR, app=app, message=message, stacktrace=stacktrace, trace_id=trace_id)


def log_fatal(logger, app: str = "Default", message: str = "", stacktrace: bool = True, trace_id: bool = False):
    """
    Writes a fatal log entry
    :type trace_id: bool
    :param trace_id: Also log a trace id of the current thread
    :type stacktrace: bool
    :type message: str
    :type app: str
    :param logger: Reference to used logger
    :param app: Application writing to log, defaults to "Default"
    :param message: Log message, defaults to ""
    :param stacktrace: Also write stack information
    """
    _log(logger=logger, logtype=LogType.FATAL, app=app, message=message, stacktrace=stacktrace, trace_id=trace_id)


# endregion

# region Private methods

def _log(logger, logtype: LogType = LogType.DEBUG, app: str = "Default", message: str = "", stacktrace: bool = False,
         trace_id: bool = False):
    """
    Logs a message
    :type trace_id: bool
    :param trace_id: Also log a trace id of the current thread
    :type stacktrace: bool
    :type message: str
    :type app: str
    :type logtype: LogType
    :param logger: Reference to used logger
    :param logtype: Type of log message, defaults to DEBUG
    :param app: Application writing to log, defaults to "Default"
    :param message: Log message, defaults to ""
    :param stacktrace: Also write stack information
    """

    if not ctx:
        print("Check ctx is not None")
        ctx.trace_id = ""
    if not hasattr(ctx, "trace_id"):
        ctx.trace_id = ""

        # add trace id to log message
    trace_stack_message = traceback.format_exc()
    _, _, tb = sys.exc_info()
    if trace_id and (ctx.trace_id != ""):
        message = app + "|" + ctx.trace_id + "|" + message
        message_stack = app + "|" + ctx.trace_id + "|" + trace_stack_message
    else:
        message = app + "|" + message
        message_stack = app + "|" + trace_stack_message

    if logtype == LogType.DEBUG:
        logger.debug(message)
        if stacktrace and tb:
            logger.debug(message_stack)
    if logtype == LogType.INFO:
        logger.info(message)
        if stacktrace and tb:
            logger.info(message_stack)
    if logtype == LogType.CRITICAL:
        logger.critical(message)
        if stacktrace and tb:
            logger.critical(message_stack)
    if logtype == LogType.ERROR:
        logger.error(message)
        if stacktrace and tb:
            logger.error(message_stack)
    if logtype == LogType.FATAL:
        logger.fatal(message)
        if stacktrace and tb:
            logger.fatal(message_stack)
    if logtype == LogType.WARNING:
        logger.warning(message)
        if stacktrace and tb:
            logger.fatal(message_stack)

# endregion
