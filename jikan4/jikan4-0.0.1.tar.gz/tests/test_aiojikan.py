import json
import pytest

from jikan4.aiojikan import AioJikan


@pytest.fixture
def aiojikan():
    return AioJikan()


@pytest.mark.asyncio
async def test_get_anime(aiojikan: AioJikan):
    resp = await aiojikan.get_anime(1)
    with open('./tests/responses/get_anime(1).json', 'r') as f:
        expected = json.load(f)

    assert resp == expected, 'Response does not match expected response'

    await aiojikan.close()


@pytest.mark.asyncio
async def test_search_anime(aiojikan: AioJikan):
    resp = await aiojikan.search_anime('anime', 'naruto')
    
    assert {'pagination', 'data'}.issubset(resp.keys()), 'Response does not match expected response'

    await aiojikan.close()
