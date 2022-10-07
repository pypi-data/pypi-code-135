import json
import pytest

from jikan4.aiojikan import AioJikan


@pytest.fixture
def aiojikan():
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
