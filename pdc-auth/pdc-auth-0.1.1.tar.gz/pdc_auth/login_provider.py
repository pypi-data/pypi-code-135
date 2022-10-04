import json
import os
from uuid import getnode as get_mac

import requests

from .endpoint import EndpointConfig
from .exceptions.login_provider_exc import LoginProviderFailedException

DEFAULT_BOT_ID = 1
DEFAULT_BOT_VERSION = 'unofficial'

class Bot:
    bot_id: int
    latest_version: str
    version: str

    def __init__(self, bot_id=DEFAULT_BOT_ID, version=DEFAULT_BOT_VERSION):
        self.bot_id = bot_id
        self.version = version

class LoginProvider:
    bot = Bot(DEFAULT_BOT_ID)
    endpoint = EndpointConfig()
    headers = {
        'Content-Type': 'aplication/json',
        'Accept': 'aplication/json',
    }

    session = requests.Session()

    def __init__(self, bot_id=DEFAULT_BOT_ID, version=DEFAULT_BOT_VERSION):
        self.update_bot(bot_id=bot_id, version=version)

    def update_bot(self, bot_id=DEFAULT_BOT_ID, version=DEFAULT_BOT_VERSION, latest_version=None):
        self.bot.bot_id = bot_id
        self.bot.version = version
        self.bot.latest_version = latest_version
    
    def update_headers(self, headers: dict):
        self.headers.update(headers)

    def login(self, email: str, password: str) -> bool:
        host = self.endpoint.get_host()
        payload = json.dumps({
            'email': email,
            'password': password,
            'name': os.environ['COMPUTERNAME'],
            'mac': str(get_mac()),
            'bot_id': self.bot.bot_id,
            'version': self.bot.version,
        })

        req = self.session.post(host, headers=self.headers, data=payload)

        if req.status_code != 200:
            raise LoginProviderFailedException(email)

        return True