import json
import pytest

from jikan4.jikan import Jikan


@pytest.fixture
def jikan():
    return Jikan()


def test_get_anime(jikan: Jikan):
    resp = jikan.get_anime(1)

    assert resp.title == "Cowboy Bebop", "Response does not match expected response"


def test_search_anime(jikan: Jikan):
    resp = jikan.search_anime("tv", "naruto")

    assert {"pagination", "data"}.issubset(
        resp.__dict__
    ), "Response does not match expected response"
    assert len(resp.data) > 0, "Response data is empty"
