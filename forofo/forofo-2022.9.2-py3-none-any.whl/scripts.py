import logging

import click
import uvicorn
from click_loglevel import LogLevel

# from clutter.logging import logger

APP = "forofo.server.main:app"

# this is default (site-packages\uvicorn\main.py)
LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
        },
    },
    "handlers": {
        "default": {"formatter": "default", "class": "logging.StreamHandler", "stream": "ext://sys.stderr"},
        "access": {"formatter": "access", "class": "logging.StreamHandler", "stream": "ext://sys.stdout"},
    },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.error": {"level": "INFO", "handlers": ["default"], "propagate": True},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
    },
}

# add your handler to it (in my case, I'm working with quart, but you can do this with Flask etc. as well, they're all the same)
LOG_CONFIG["loggers"]["quart"] = {"handlers": ["default"], "level": "INFO"}


@click.group()
def forofo():
    pass


@forofo.command()
@click.option("-h", "--host", type=str, default="0.0.0.0")
@click.option("-p", "--port", type=int, default=3000)
@click.option("--debug", is_flag=True)
@click.option("--reload", is_flag=True)
@click.option("--log-level", type=LogLevel(), default=logging.DEBUG)
def run_server(host, port, debug, reload, log_level):
    print("!!!")
    try:
        uvicorn.run(APP, host=host, port=port, debug=debug, reload=reload)  # , log_level=log_level)
    except Exception as ex:
        print(ex)
