import asyncio
import os
import traceback

import aiohttp
from aiolimiter import AsyncLimiter
from dotenv import load_dotenv

load_dotenv()
RATE_LIMIT_PER_SECOND = int(os.getenv("RATE_LIMIT_PER_SECOND"))
limiter = AsyncLimiter(
    max_rate=float(os.getenv("ASYNC_LIMITER_MAX_RATE")),
    time_period=float(os.getenv("ASYNC_LIMITER_TIME_PERIOD")),
)


async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()


async def fetch_text(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get(urls: list[str], expected_response: str):
    async with aiohttp.ClientSession() as session:
        i = 0
        total_results = []
        while i < len(urls):
            async with limiter:
                coroutines = []

                if i + RATE_LIMIT_PER_SECOND < len(urls):
                    _urls = urls[i : i + RATE_LIMIT_PER_SECOND]  # noqa E203
                else:
                    _urls = urls[i:]

                if expected_response == "csv":
                    func = fetch_text
                else:
                    func = fetch_json

                for url in _urls:
                    coroutines.append(func(session=session, url=url))
                results = await asyncio.gather(*coroutines, return_exceptions=True)
            total_results += results
            i += RATE_LIMIT_PER_SECOND

    err = None
    for result, coro in zip(total_results, coroutines):
        if isinstance(result, Exception):
            err = result
            print(f"{coro.__name__} failed:")
            traceback.print_exception(type(err), err, err.__traceback__)

    if err:
        raise RuntimeError("One or more scripts failed.")

    return total_results
