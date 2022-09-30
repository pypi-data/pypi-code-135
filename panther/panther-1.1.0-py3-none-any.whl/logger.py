import os
import logging
from pydantic import BaseModel
from panther.configs import config
from logging.config import dictConfig


LOGS_DIR = config['base_dir'] / 'logs'
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = 'panther-logger'
    DEFAULT_LOG_FORMAT: str = '%(levelprefix)s | %(asctime)s | %(message)s'
    FILE_LOG_FORMAT: str = '%(asctime)s | %(message)s'
    LOG_LEVEL: str = 'DEBUG'

    version = 1
    disable_existing_loggers = False

    formatters = {
        'default': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': DEFAULT_LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'file_formatter': {
            '()': 'uvicorn.logging.DefaultFormatter',
            'fmt': FILE_LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    }
    handlers = {
        'monitoring_file': {
            'formatter': 'file_formatter',
            'filename': LOGS_DIR / f'monitoring.log',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 100,  # 100 MB,
            'backupCount': 3
        },
        'file': {
            'formatter': 'file_formatter',
            'filename': LOGS_DIR / f'{config["base_dir"].name}.log',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 100,  # 100 MB,
            'backupCount': 3
        },
        'default': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
        },
    }
    loggers = {
        'panther': {
            'handlers': ['default', 'file'],
            'level': LOG_LEVEL,
        },
        'monitoring': {
            'handlers': ['monitoring_file'],
            'level': LOG_LEVEL,
        },
    }


dictConfig(LogConfig().dict())
logger = logging.getLogger('panther')
monitoring = logging.getLogger('monitoring')

"""
[debug, info, warning, error, critical]
"""