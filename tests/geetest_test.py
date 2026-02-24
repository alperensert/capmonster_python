import os

import pytest

from capmonster_python import CapmonsterClient, GeeTestV4Task

API_KEY = os.getenv("API_KEY")
WEBSITE_URL = "https://faucetpay.io/account/logi"
GT = "4eb8b0c2b27f3365b9244d9da81638c6"


def test_to_request():
    task = GeeTestV4Task(
        websiteURL="https://example.com",
        gt="gt_example"
    )
    result = task.to_request()
    assert result["type"] == "GeeTestTask"
    assert result["gt"] == "gt_example"
    assert result["websiteURL"] == "https://example.com"


@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
def test_create_task():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = client.create_task(task=GeeTestV4Task(websiteURL=WEBSITE_URL, gt=GT))
    assert task_id != 0


@pytest.mark.asyncio
@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
async def test_create_task_async():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = await client.create_task_async(task=GeeTestV4Task(websiteURL=WEBSITE_URL, gt=GT))
    assert task_id != 0
