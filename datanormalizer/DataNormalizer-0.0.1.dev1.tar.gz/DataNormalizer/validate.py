# Will ask the Clappform API what keys to expect from the module
# Check the keys against the dataset
# Return if the dataset is fitting or what is wrong and propose help from diagnose.py
from .auth import Auth
from .settings import Settings
import requests

class Validate:
    def __init__(self, app = None):
        self.id = app

    def testAuth():
        if not Auth.tokenValid():
            Auth.refreshToken()