import aioredis


class TIWebServer:
    def __init__(
        self,
        redis_url: str = "redis://localhost",
    ) -> None:
        self.redis = aioredis.from_url(
            redis_url, encoding="utf-8", decode_responses=True
        )
        self.psub = self.redis.pubsub()
        self.psub.subscribe()

    async def update_table():
        pass
