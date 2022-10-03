import os
import base64
import logging

from dotenv import dotenv_values

logging.basicConfig(
    level=os.getenv("LQS_LOG_LEVEL") or logging.INFO,
    format="%(asctime)s  (%(levelname)s - %(name)s): %(message)s",
)
logger = logging.getLogger(__name__)

from .interface import Lister, Getter, Creator, Deleter, Updater
from .bridge import Bridge


class LogQS:
    def __init__(self, **kwargs):
        self._config = {**dotenv_values(".env"), **os.environ, **kwargs}

        logger.debug("config: %s", self._config)

        self._api_url = self._config.get("LQS_API_URL")
        self._api_key_id = self._config.get("LQS_API_KEY_ID")
        self._api_key_secret = self._config.get("LQS_API_KEY_SECRET")

        auth_header_value = "Bearer " + base64.b64encode(
            bytes(f"{self._api_key_id}:{self._api_key_secret}", "utf-8")
        ).decode("utf-8")

        self._headers = {
            "Authorization": auth_header_value,
            "Content-Type": "application/json",
        }

        self.list = Lister(api_url=self._api_url, headers=self._headers)
        self.get = Getter(api_url=self._api_url, headers=self._headers)
        self.create = Creator(api_url=self._api_url, headers=self._headers)
        self.update = Updater(api_url=self._api_url, headers=self._headers)
        self.delete = Deleter(api_url=self._api_url, headers=self._headers)

        self.bridge = Bridge(lister=self.list, getter=self.get)
