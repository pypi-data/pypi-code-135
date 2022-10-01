import logging
import os
from . import setup
from . import messenger


def config():
    return setup.start()


def start():
    return messenger.start()
