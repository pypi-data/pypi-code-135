from typing import AsyncGenerator

import httpx
import pytest

from fief_cloud.cloud import app
from tests.types import TestClientGeneratorType


@pytest.fixture
@pytest.mark.asyncio
async def test_client(
    test_client_admin_generator: TestClientGeneratorType,
) -> AsyncGenerator[httpx.AsyncClient, None]:
    async with test_client_admin_generator(app) as test_client:
        yield test_client
