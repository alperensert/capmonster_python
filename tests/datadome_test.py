import os

import pytest

from capmonster_python import DataDomeTask, DataDomeMetadata, CapmonsterClient

API_KEY = os.getenv("API_KEY")
WEBSITE_URL = "https://antoinevastel.com/bots/datadome"
METADATA = DataDomeMetadata(
    captchaUrl="https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAJxx4dfgwjzwAQW0ctQ%3D%3D&hash"
               "=D66B23AC3F48A302A7654416846381&cid=d3k5rbDsu8cq0kmPHISS3hsC3f4qeL_K12~G33PrE4fbkmDYSul6l0Ze_aG5sUHLKG0676UpTv6GFvUgIActglZF33GTodOoRhEDkMMsuWTodlYa3YYQ9xKy9J89PAWh&t=fe&referer=https%3A%2F%2Fantoinevastel.com%2Fbots%2Fdatadome&s=21705&e=04fc682817ba89bf8fa4b18031fa53294fa0fb7449d95c036a1986413e6dfc7d",
    datadomeCookie="datadome=d3k5rbDsu8cq0kmPHISS3hsC3f4qeL_K12~G33PrE4fbkmDYSul6l0Ze_aG5sUHLKG0676UpTv6GFvUgIActglZF33GTodOoRhEDkMMsuWTodlYa3YYQ9xKy9J89PAWh"
)


def test_to_request():
    task = DataDomeTask(
        websiteURL="https://example.com",
        metadata=DataDomeMetadata(
            htmlPageBase64="base64_example",
            datadomeCookie="cookie1=value1; cookie2=value2;"
        )
    )
    result = task.to_request()
    assert result["type"] == "CustomTask"
    assert result["class"] == "DataDome"
    assert result["metadata"]["htmlPageBase64"] == "base64_example"
    assert result["metadata"]["datadomeCookie"] == "cookie1=value1; cookie2=value2;"


@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
async def test_create_task_async():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = client.create_task(task=DataDomeTask(websiteURL=WEBSITE_URL, metadata=METADATA))
    assert task_id != 0
    assert task_id != 0


@pytest.mark.asyncio
@pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")
async def test_create_task_async():
    client = CapmonsterClient(API_KEY, timeout=30.0)
    task_id = await client.create_task_async(task=DataDomeTask(websiteURL=WEBSITE_URL, metadata=METADATA))
    assert task_id != 0
