"""
Conscious module to handle processing and abstract thought
"""
import asyncio
import logging


class Conscious:
    """
    Conscious class to handle processing and abstract thought
    """

    @classmethod
    async def loop(cls) -> None:
        """
        Conscious loop
        :return:
        """
        logging.info("I'm conscious")
        while True:
            await cls.process_input()

    @classmethod
    async def process_input(cls) -> None:
        """
        Handle the input
        :return:
        """
        await asyncio.sleep(1)
