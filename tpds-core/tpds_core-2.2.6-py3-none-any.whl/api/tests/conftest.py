import pytest
from typing import Generator
from fastapi.testclient import TestClient
from ..core import api_inst


@pytest.fixture
def client() -> Generator:
    with TestClient(api_inst) as c:
        yield c


