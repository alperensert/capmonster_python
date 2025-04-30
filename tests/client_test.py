import os

import pytest

from capmonster_python import CapmonsterClient

API_KEY = os.getenv("API_KEY")


@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
def test_get_balance_success():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    balance = client.get_balance()
    assert balance > 0.1


@pytest.mark.asyncio
@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
async def test_get_balance_success_async():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    balance = await client.get_balance_async()
    assert balance > 0.1
