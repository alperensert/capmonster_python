import os

import pytest

from capmonster_python import RecaptchaV2Task, CapmonsterClient

API_KEY = os.getenv("API_KEY")
WEBSITE_URL = "https://www.google.com/recaptcha/api2/demo"
WEBSITE_KEY = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"


def test_to_request():
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="abc123",
        isInvisible=True,
    )
    result = task.to_request()
    assert result["type"] == "RecaptchaV2Task"
    assert result["websiteKey"] == "abc123"
    assert result["isInvisible"] is True


@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
def test_create_task():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = client.create_task(task=RecaptchaV2Task(websiteURL=WEBSITE_URL, websiteKey=WEBSITE_KEY))
    assert task_id != 0


@pytest.mark.asyncio
@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
async def test_create_task_async():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = await client.create_task_async(task=RecaptchaV2Task(websiteURL=WEBSITE_URL, websiteKey=WEBSITE_KEY))
    assert task_id != 0
