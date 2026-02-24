import pytest
import respx
from httpx import Response

from capmonster_python import (
    CapmonsterClient, RecaptchaV2Task, RecaptchaV3Task,
    CapmonsterAPIException, ProxyPayload, FunCaptchaTask
)

BASE_URL = "https://api.capmonster.cloud"


@respx.mock
def test_get_balance():
    respx.post(f"{BASE_URL}/getBalance").mock(
        return_value=Response(200, json={"errorId": 0, "balance": 42.5})
    )
    client = CapmonsterClient("test_key")
    assert client.get_balance() == 42.5


@respx.mock
@pytest.mark.asyncio
async def test_get_balance_async():
    respx.post(f"{BASE_URL}/getBalance").mock(
        return_value=Response(200, json={"errorId": 0, "balance": 10.0})
    )
    client = CapmonsterClient("test_key")
    assert await client.get_balance_async() == 10.0


@respx.mock
def test_create_task():
    respx.post(f"{BASE_URL}/createTask").mock(
        return_value=Response(200, json={"errorId": 0, "taskId": 123456})
    )
    client = CapmonsterClient("test_key")
    task = RecaptchaV2Task(websiteURL="https://example.com", websiteKey="key123")
    task_id = client.create_task(task)
    assert task_id == 123456


@respx.mock
@pytest.mark.asyncio
async def test_create_task_async():
    respx.post(f"{BASE_URL}/createTask").mock(
        return_value=Response(200, json={"errorId": 0, "taskId": 789})
    )
    client = CapmonsterClient("test_key")
    task = RecaptchaV2Task(websiteURL="https://example.com", websiteKey="key123")
    task_id = await client.create_task_async(task)
    assert task_id == 789


@respx.mock
def test_get_task_result_ready():
    respx.post(f"{BASE_URL}/getTaskResult").mock(
        return_value=Response(200, json={
            "errorId": 0,
            "status": "ready",
            "solution": {"gRecaptchaResponse": "token_abc"}
        })
    )
    client = CapmonsterClient("test_key")
    result = client.get_task_result(123)
    assert result["gRecaptchaResponse"] == "token_abc"


@respx.mock
def test_get_task_result_processing():
    respx.post(f"{BASE_URL}/getTaskResult").mock(
        return_value=Response(200, json={
            "errorId": 0,
            "status": "processing"
        })
    )
    client = CapmonsterClient("test_key")
    result = client.get_task_result(123)
    assert result == {}


@respx.mock
def test_join_task_result_polls_then_succeeds():
    route = respx.post(f"{BASE_URL}/getTaskResult")
    route.side_effect = [
        Response(200, json={"errorId": 0, "status": "processing"}),
        Response(200, json={"errorId": 0, "status": "processing"}),
        Response(200, json={"errorId": 0, "status": "ready", "solution": {"token": "done"}}),
    ]
    client = CapmonsterClient("test_key", retry_delay=0)
    result = client.join_task_result(123)
    assert result["token"] == "done"
    assert route.call_count == 3


@respx.mock
def test_join_task_result_exceeds_retries():
    respx.post(f"{BASE_URL}/getTaskResult").mock(
        return_value=Response(200, json={"errorId": 0, "status": "processing"})
    )
    client = CapmonsterClient("test_key", max_retries=2, retry_delay=0)
    with pytest.raises(CapmonsterAPIException) as exc_info:
        client.join_task_result(123)
    assert "ERROR_MAXIMUM_TIME_EXCEED" in str(exc_info.value)


@respx.mock
@pytest.mark.asyncio
async def test_join_task_result_async_polls_then_succeeds():
    route = respx.post(f"{BASE_URL}/getTaskResult")
    route.side_effect = [
        Response(200, json={"errorId": 0, "status": "processing"}),
        Response(200, json={"errorId": 0, "status": "ready", "solution": {"token": "async_done"}}),
    ]
    client = CapmonsterClient("test_key", retry_delay=0)
    result = await client.join_task_result_async(123)
    assert result["token"] == "async_done"


@respx.mock
def test_solve_convenience():
    respx.post(f"{BASE_URL}/createTask").mock(
        return_value=Response(200, json={"errorId": 0, "taskId": 999})
    )
    respx.post(f"{BASE_URL}/getTaskResult").mock(
        return_value=Response(200, json={
            "errorId": 0, "status": "ready",
            "solution": {"gRecaptchaResponse": "solved"}
        })
    )
    client = CapmonsterClient("test_key", retry_delay=0)
    task = RecaptchaV3Task(websiteURL="https://example.com", websiteKey="key", minScore=0.5)
    result = client.solve(task)
    assert result["gRecaptchaResponse"] == "solved"


@respx.mock
@pytest.mark.asyncio
async def test_solve_async_convenience():
    respx.post(f"{BASE_URL}/createTask").mock(
        return_value=Response(200, json={"errorId": 0, "taskId": 888})
    )
    respx.post(f"{BASE_URL}/getTaskResult").mock(
        return_value=Response(200, json={
            "errorId": 0, "status": "ready",
            "solution": {"token": "async_solved"}
        })
    )
    client = CapmonsterClient("test_key", retry_delay=0)
    task = FunCaptchaTask(websiteURL="https://example.com", websitePublicKey="pk")
    result = await client.solve_async(task)
    assert result["token"] == "async_solved"


@respx.mock
def test_api_error_raises_exception():
    respx.post(f"{BASE_URL}/getBalance").mock(
        return_value=Response(200, json={
            "errorId": 1,
            "errorCode": "ERROR_KEY_DOES_NOT_EXIST",
            "errorDescription": "Account authorization key not found"
        })
    )
    client = CapmonsterClient("bad_key")
    with pytest.raises(CapmonsterAPIException) as exc_info:
        client.get_balance()
    assert exc_info.value.error_code == "ERROR_KEY_DOES_NOT_EXIST"


@respx.mock
def test_context_manager():
    respx.post(f"{BASE_URL}/getBalance").mock(
        return_value=Response(200, json={"errorId": 0, "balance": 5.0})
    )
    with CapmonsterClient("test_key") as client:
        balance = client.get_balance()
    assert balance == 5.0


@respx.mock
@pytest.mark.asyncio
async def test_async_context_manager():
    respx.post(f"{BASE_URL}/getBalance").mock(
        return_value=Response(200, json={"errorId": 0, "balance": 3.0})
    )
    async with CapmonsterClient("test_key") as client:
        balance = await client.get_balance_async()
    assert balance == 3.0


def test_proxy_payload_serialization():
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="key",
        proxy=ProxyPayload(
            proxyType="socks5",
            proxyAddress="192.168.1.1",
            proxyPort=1080,
            proxyLogin="user",
            proxyPassword="pass"
        )
    )
    result = task.to_request()
    assert result["proxyType"] == "socks5"
    assert result["proxyAddress"] == "192.168.1.1"
    assert result["proxyPort"] == 1080
    assert result["proxyLogin"] == "user"
    assert result["proxyPassword"] == "pass"
    assert "proxy" not in result


def test_configurable_retry_params():
    client = CapmonsterClient("key", max_retries=5, retry_delay=0.5)
    assert client._CapmonsterClient__max_retries == 5
    assert client._CapmonsterClient__retry_delay == 0.5
