import pytest
import time

from jikan4.aiojikan import AioJikan


@pytest.fixture
def aiojikan():
    time.sleep(
        1
    )  # This is needed to prevent 429 Too Many Requests when resetting the rate limit

    return AioJikan()


@pytest.mark.asyncio
async def test_get_anime(aiojikan: AioJikan):
    resp = await aiojikan.get_anime(1)

    assert resp.title == "Cowboy Bebop", "Response does not match expected response"


@pytest.mark.asyncio
async def test_search_anime(aiojikan: AioJikan):
    resp = await aiojikan.search_anime("anime", "naruto")

    assert {"pagination", "data"}.issubset(
        resp.__dict__
    ), "Response does not match expected response"


@pytest.mark.asyncio
async def test_ratelimit(aiojikan: AioJikan):
    start = time.time()
    for _ in range(10):
        await aiojikan.get_anime(1)
    end = time.time()

    max_per_minute = aiojikan.rate_limiter.calls_limit / aiojikan.rate_limiter.period

    assert end - start > 10 / (60 / max_per_minute), "Rate limit not working"
