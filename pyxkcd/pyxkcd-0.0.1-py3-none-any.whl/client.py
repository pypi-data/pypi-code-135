from .response import Response

import asyncio
import weakref
import random
import httpx

class Client:
    def __init__(self):
        self.session = httpx.Client()
        self.current = self.latest().num

        weakref.finalize(self, self.session.close)

    def get(self, comic: int):
        raw_data = self.session.get(f"https://xkcd.com/{comic}/info.0.json")
        return Response(raw_data.json())

    def latest(self):
        raw_data = self.session.get("https://xkcd.com/info.0.json")
        return Response(raw_data.json())

    def random(self):
        return self.get(random.randint(1, self.current))


class AsyncClient:
    def __init__(self):
        self.session = httpx.AsyncClient()
        self.current = asyncio.run(self.latest()).num

        weakref.finalize(self, self.close)

    async def get(self, comic: int):
        raw_data = await self.session.get(f"https://xkcd.com/{comic}/info.0.json")
        return Response(raw_data.json())

    async def latest(self):
        raw_data = await self.session.get("https://xkcd.com/info.0.json")
        return Response(raw_data.json())

    async def random(self):
        return await self.get(random.randint(1, self.current))

    def close(self):
        asyncio.run(self.session.aclose())
