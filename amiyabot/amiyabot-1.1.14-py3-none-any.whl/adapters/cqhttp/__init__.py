import json
import asyncio
import websockets

from typing import Callable
from amiyabot.adapters import BotAdapterProtocol
from amiyabot.builtin.message import Message
from amiyabot.builtin.messageChain import Chain


def mirai_api_http(host: str, ws_port: int, http_port: int):
    def adapter(appid: str, token: str):
        return CQHttpBotInstance(appid, token, host, ws_port, http_port)

    return adapter


class CQHttpBotInstance(BotAdapterProtocol):
    def __init__(self, appid: str, token: str, host: str, ws_port: int, http_port: int):
        super().__init__(appid, token)

        self.host = host
        self.ws_port = ws_port
        self.http_port = http_port

    def close(self):
        pass

    async def connect(self, private: bool, handler: Callable):
        pass

    async def send_chain_message(self, chain: Chain):
        pass

    async def send_message(self,
                           chain: Chain,
                           user_id: str = '',
                           channel_id: str = '',
                           direct_src_guild_id: str = ''):
        pass

    async def package_message(self, event: str, message: dict):
        pass
