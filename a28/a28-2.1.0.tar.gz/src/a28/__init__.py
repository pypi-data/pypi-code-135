"""Build packages to be submitted to Area28."""
import logging

import coloredlogs

from a28.__version__ import __version__  # noqa: F401

# enable logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
coloredlogs.install(level="DEBUG", logger=log)
