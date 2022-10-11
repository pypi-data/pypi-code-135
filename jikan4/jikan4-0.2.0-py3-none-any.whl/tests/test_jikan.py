import pytest
import time

from jikan4.jikan import Jikan


@pytest.fixture
def jikan():
    time.sleep(
        1
    )  # This is needed to prevent 429 Too Many Requests when resetting the rate limit

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


def test_ratelimit(jikan: Jikan):
    start = time.time()
    for _ in range(10):
        jikan.get_anime(1)
    end = time.time()

    max_per_minute = jikan.rate_limiter.calls_limit / jikan.rate_limiter.period

    assert end - start > 10 / (60 / max_per_minute), "Rate limit not working"
