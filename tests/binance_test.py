import os

import pytest

from capmonster_python import BinanceTask, CapmonsterClient

API_KEY = os.getenv("API_KEY")
WEBSITE_URL = "https://accounts.binance.com/en/login?loginChannel=&return_to="
WEBSITE_KEY = "login"
VALIDATE_ID = "2b8137c0b9b44189800368819354e114"


def test_to_request():
    task = BinanceTask(
        websiteURL="https://example.com",
        websiteKey="abc123",
        validateId="v4lid4t3"
    )
    result = task.to_request()
    assert result["type"] == "BinanceTask"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "abc123"
    assert result["validateId"] == "v4lid4t3"


@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
async def test_create_task_async():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = client.create_task(
        task=BinanceTask(websiteURL=WEBSITE_URL, websiteKey=WEBSITE_KEY, validateId=VALIDATE_ID))
    assert task_id != 0


@pytest.mark.asyncio
@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
async def test_create_task_async():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = await client.create_task_async(
        task=BinanceTask(websiteURL=WEBSITE_URL, websiteKey=WEBSITE_KEY, validateId=VALIDATE_ID))
    assert task_id != 0
