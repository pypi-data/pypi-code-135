"""
Keystrokes AKA keyboard input
"""
import asyncio
import logging
import sys
from asyncio import AbstractEventLoop, StreamReader
from typing import TextIO


class KeyBoard:
    """
    class for keystrokes AKA keyboard input
    """

    @staticmethod
    async def listen() -> None:
        """
        Keyboard listener
        :return:
        """
        reader: StreamReader = StreamReader()
        pipe: TextIO = sys.stdin
        loop: AbstractEventLoop = asyncio.get_event_loop()
        await loop.connect_read_pipe(
            lambda: asyncio.StreamReaderProtocol(reader), pipe
        )

        async for line in reader:
            decoded: str = line.decode().strip("\n")
            logging.info(decoded)
        await asyncio.sleep(1)

    @classmethod
    async def loop(cls):
        """
        Keyboard loop
        :return:
        """
        await cls.listen()
