import logging
import os
import sys

__all__ = ['set_standard_logging_config']


def suppress_common_packages():
    """Suppress INFO logs from common packages to reduce clutter"""
    # setting warning level to various packages to avoid additional logs
    packages = ('botocore', 'boto3', 'requests', 'urllib3', 'rasterio', 'shapely', 'paramiko')
    for p in packages:
        p_logger = logging.getLogger(p)
        p_logger.setLevel(logging.WARNING)


def get_fmt_string(code: str = None, env: str = None) -> str:
    """Creates common format string for logging

    Args:
        code: an optional flight code to include
        env: an optional environment to include

    Returns:
        a format string
    """
    format_str = '[{asctime}][{name}][{filename}:{lineno}][{funcName}][{levelname}]: {message}'

    if code:
        format_str = "[{}]{}".format(code, format_str)

    if env:
        format_str = "[{}]{}".format(env, format_str)

    return format_str


def set_standard_logging_config(*, level=logging.INFO, stdout: bool = True, stderr: bool = False, logfile: str = None,
                                code: str = None, env: str = None, suppress_packages: bool = True):
    """Sets a standard logging context

    Args:
        level: the logging level of the root logger
        stdout: if true will print logs to stdout
        stderr: if true will print logs to stderr
        logfile: an optional path to write logs to
        code: an optional code to include in the logging output
        env: an optional environment to include in the logging output
        suppress_packages: if true will suppress info messages from common packages
    """

    if env is None and 'IA_ENV' in os.environ:
        env = os.environ['IA_ENV']

    if suppress_packages:
        suppress_common_packages()

    if 'IA_LOGGING_FMT' in os.environ and os.environ['IA_LOGGING_FMT'] != '':
        fmt_string = os.environ['IA_LOGGING_FMT']
    else:
        fmt_string = get_fmt_string(code=code, env=env)

    handlers = list()

    if stdout:
        handlers.append(logging.StreamHandler(sys.stdout))

    if stderr:
        handlers.append(logging.StreamHandler(sys.stderr))

    if logfile:
        handlers.append(logging.FileHandler(logfile))

    if 'IA_LOGFILE' in os.environ and os.environ['IA_LOGFILE'] != '':
        handlers.append(logging.FileHandler(os.environ['IA_LOGFILE']))

    logging.basicConfig(level=level, handlers=handlers, format=fmt_string, style='{', force=True)

