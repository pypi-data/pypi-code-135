"""Handlers for logging."""

import logging
import os


def setup_logger(verbose_mode: bool = False) -> logging.Logger:
    """Setup the logger."""

    logger = logging.getLogger('graphintrospect')
    logger.setLevel(logging.DEBUG if os.getenv('DEBUG') or verbose_mode else logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(os.getenv('LOG_FORMAT') or '%(asctime)s %(levelname)s %(name)s - %(message)s'))

    for h in logger.handlers:
        logger.removeHandler(h)

    logger.addHandler(handler)
    logger.propagate = False

    return logger


LOG: logging.Logger = setup_logger()
