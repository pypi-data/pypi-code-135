from functools import lru_cache

from httpx import AsyncClient, Client

from .blocks import Blocks
from .types import AsyncWebhook, Webhook


@lru_cache(maxsize=10)
def SlackWebhook(url: str) -> Webhook:
    client = Client()

    def webhook(blocks: Blocks) -> None:
        response = client.post(url, json=blocks.dict())
        response.raise_for_status()

    return webhook


@lru_cache(maxsize=10)
def AsyncSlackWebhook(url: str) -> AsyncWebhook:
    client = AsyncClient()

    async def webhook(blocks: Blocks) -> None:
        response = await client.post(url, json=blocks.dict())
        response.raise_for_status()

    return webhook
