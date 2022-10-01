import logging
from venv import create
from archetypewsgi.api_resources.error import APIRequestError
from archetypewsgi.enums import Method
from archetypewsgi import prod_api_base
import aiohttp
import asyncio
from archetypewsgi.api_request_thread import requests_loop

async def create_session():
    return aiohttp.ClientSession()

class APIRequestor:
    def __init__(self):
        from archetypewsgi import secret_key

        self.secret_key = secret_key
        self.http_session = asyncio.run_coroutine_threadsafe(create_session(), requests_loop).result()

    async def create_request(
        self,
        request_method: Method,
        path: str,
        headers: dict = {},
        data: dict = {},
        object: str = None,
        intent: str = None,
    ):
        headers["Authorization"] = f"Bearer {self.secret_key}"
        url = f"{prod_api_base}{path}"
        
        logging.debug(f"Archetype req: {request_method} {url}")

        if request_method == Method.GET:
            response = await self.http_session.get(url=url, headers=headers)
        elif request_method == Method.POST:
            response = await self.http_session.post(url=url, headers=headers, json=data)
        elif request_method == Method.PUT:
            response = await self.http_session.put(url=url, headers=headers, json=data)
        elif request_method == Method.DELETE:
            response = await self.http_session.delete(url=url, headers=headers, json=data)

        if response.status < 400:
            return await response.json()
        else:
            raise APIRequestError(
                request_method, response.status, await response.json(), intent=intent
            )
