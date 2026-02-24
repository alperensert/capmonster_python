import os

import pytest

from capmonster_python import CapmonsterClient, BasiliskTask

API_KEY = os.getenv("API_KEY")
WEBSITE_URL = "https://faucetpay.io/account/register"
WEBSITE_KEY = "a3760bfe5cf4254b2759c19fb2601667"


def test_to_request():
    task = BasiliskTask(
        websiteURL="https://example.com",
        websiteKey="abc123"
    )
    result = task.to_request()
    assert result["type"] == "CustomTask"
    assert result["class"] == "Basilisk"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "abc123"


@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
def test_create_task():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = client.create_task(task=BasiliskTask(websiteURL=WEBSITE_URL, websiteKey=WEBSITE_KEY))
    assert task_id != 0


@pytest.mark.asyncio
@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
async def test_create_task_async():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = await client.create_task_async(task=BasiliskTask(websiteURL=WEBSITE_URL, websiteKey=WEBSITE_KEY))
    assert task_id != 0
