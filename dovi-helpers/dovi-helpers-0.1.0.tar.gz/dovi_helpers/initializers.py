import logging
import os
import sys

import structlog
from structlog.processors import CallsiteParameter

__all__ = ("init_system",)

log = structlog.get_logger(__name__)


def init_system() -> None:
    configure_logging()


def configure_logging() -> None:
    logging.basicConfig(
        stream=sys.stdout,
        level=os.getenv("LOG_LEVEL", default=logging.INFO),
    )
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.TimeStamper("ISO"),
            structlog.processors.CallsiteParameterAdder(
                [CallsiteParameter.PROCESS_NAME]
            ),
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
    log.debug("logger.configured")
