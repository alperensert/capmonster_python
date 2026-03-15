import pytest
import respx
from httpx import Response

from capmonster_python import (
    CapmonsterClient, RecaptchaV2Task, RecaptchaV2EnterpriseTask,
    RecaptchaV3Task, RecaptchaV3EnterpriseTask,
    CapmonsterAPIException, CapmonsterException, ProxyPayload,
    FunCaptchaTask, RecaptchaClickTask, HuntTask
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


def test_default_retry_delay_is_two_seconds():
    client = CapmonsterClient("key")
    assert client._CapmonsterClient__retry_delay == 2.0


@respx.mock
def test_report_incorrect_image():
    respx.post(f"{BASE_URL}/reportIncorrectImageCaptcha").mock(
        return_value=Response(200, json={"errorId": 0, "status": "success"})
    )
    client = CapmonsterClient("test_key")
    client.report_incorrect_image(123)


@respx.mock
@pytest.mark.asyncio
async def test_report_incorrect_image_async():
    respx.post(f"{BASE_URL}/reportIncorrectImageCaptcha").mock(
        return_value=Response(200, json={"errorId": 0, "status": "success"})
    )
    client = CapmonsterClient("test_key")
    await client.report_incorrect_image_async(123)


@respx.mock
def test_report_incorrect_token():
    respx.post(f"{BASE_URL}/reportIncorrectTokenCaptcha").mock(
        return_value=Response(200, json={"errorId": 0, "status": "success"})
    )
    client = CapmonsterClient("test_key")
    client.report_incorrect_token(456)


@respx.mock
@pytest.mark.asyncio
async def test_report_incorrect_token_async():
    respx.post(f"{BASE_URL}/reportIncorrectTokenCaptcha").mock(
        return_value=Response(200, json={"errorId": 0, "status": "success"})
    )
    client = CapmonsterClient("test_key")
    await client.report_incorrect_token_async(456)


@respx.mock
def test_get_user_agent():
    respx.get("https://capmonster.cloud/api/useragent/actual").mock(
        return_value=Response(200, text="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    )
    client = CapmonsterClient("test_key")
    ua = client.get_user_agent()
    assert "Mozilla" in ua


@respx.mock
@pytest.mark.asyncio
async def test_get_user_agent_async():
    respx.get("https://capmonster.cloud/api/useragent/actual").mock(
        return_value=Response(200, text="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    )
    client = CapmonsterClient("test_key")
    ua = await client.get_user_agent_async()
    assert "Mozilla" in ua


def test_nocache_recaptcha_v2():
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="key123",
        nocache=True
    )
    result = task.to_request()
    assert result["nocache"] is True


def test_nocache_recaptcha_v3():
    task = RecaptchaV3Task(
        websiteURL="https://example.com",
        websiteKey="key123",
        nocache=True
    )
    result = task.to_request()
    assert result["nocache"] is True


def test_nocache_excluded_when_none():
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="key123"
    )
    result = task.to_request()
    assert "nocache" not in result


def test_recaptcha_click_task():
    task = RecaptchaClickTask(
        websiteURL="https://example.com",
        websiteKey="key123"
    )
    result = task.to_request()
    assert result["type"] == "RecaptchaClickTask"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "key123"


def test_recaptcha_click_task_with_proxy():
    task = RecaptchaClickTask(
        websiteURL="https://example.com",
        websiteKey="key123",
        proxy=ProxyPayload(
            proxyType="http",
            proxyAddress="1.2.3.4",
            proxyPort=8080
        )
    )
    result = task.to_request()
    assert result["proxyType"] == "http"
    assert result["proxyAddress"] == "1.2.3.4"
    assert "proxy" not in result


def test_hunt_task():
    task = HuntTask(
        websiteURL="https://example.com",
        websiteKey="key123"
    )
    result = task.to_request()
    assert result["type"] == "HuntTask"
    assert result["websiteURL"] == "https://example.com"
    assert result["websiteKey"] == "key123"


def test_hunt_task_with_proxy():
    task = HuntTask(
        websiteURL="https://example.com",
        websiteKey="key123",
        proxy=ProxyPayload(
            proxyType="socks5",
            proxyAddress="10.0.0.1",
            proxyPort=1080
        )
    )
    result = task.to_request()
    assert result["proxyType"] == "socks5"
    assert "proxy" not in result


def test_recaptcha_v2_cookies():
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="key123",
        cookies="session=abc; token=xyz"
    )
    result = task.to_request()
    assert result["cookies"] == "session=abc; token=xyz"


def test_recaptcha_v2_cookies_excluded_when_none():
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="key123"
    )
    result = task.to_request()
    assert "cookies" not in result


def test_recaptcha_v2_enterprise_page_action():
    task = RecaptchaV2EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="key123",
        pageAction="login_test"
    )
    result = task.to_request()
    assert result["pageAction"] == "login_test"


def test_recaptcha_v2_enterprise_page_action_excluded_when_none():
    task = RecaptchaV2EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="key123"
    )
    result = task.to_request()
    assert "pageAction" not in result


def test_recaptcha_v3_is_enterprise():
    task = RecaptchaV3Task(
        websiteURL="https://example.com",
        websiteKey="key123",
        isEnterprise=True
    )
    result = task.to_request()
    assert result["isEnterprise"] is True


def test_recaptcha_v3_is_enterprise_excluded_when_none():
    task = RecaptchaV3Task(
        websiteURL="https://example.com",
        websiteKey="key123"
    )
    result = task.to_request()
    assert "isEnterprise" not in result


# --- Report methods: error paths and payload verification ---

@respx.mock
def test_report_incorrect_image_sends_correct_payload():
    route = respx.post(f"{BASE_URL}/reportIncorrectImageCaptcha").mock(
        return_value=Response(200, json={"errorId": 0, "status": "success"})
    )
    client = CapmonsterClient("my_api_key")
    client.report_incorrect_image(999)
    request_body = route.calls[0].request.content
    import json
    payload = json.loads(request_body)
    assert payload["clientKey"] == "my_api_key"
    assert payload["taskId"] == 999


@respx.mock
def test_report_incorrect_token_sends_correct_payload():
    route = respx.post(f"{BASE_URL}/reportIncorrectTokenCaptcha").mock(
        return_value=Response(200, json={"errorId": 0, "status": "success"})
    )
    client = CapmonsterClient("my_api_key")
    client.report_incorrect_token(777)
    request_body = route.calls[0].request.content
    import json
    payload = json.loads(request_body)
    assert payload["clientKey"] == "my_api_key"
    assert payload["taskId"] == 777


@respx.mock
def test_report_incorrect_image_api_error():
    respx.post(f"{BASE_URL}/reportIncorrectImageCaptcha").mock(
        return_value=Response(200, json={
            "errorId": 1,
            "errorCode": "ERROR_NO_SUCH_CAPCHA_ID",
            "errorDescription": "Task not found"
        })
    )
    client = CapmonsterClient("test_key")
    with pytest.raises(CapmonsterAPIException) as exc_info:
        client.report_incorrect_image(99999)
    assert exc_info.value.error_code == "ERROR_NO_SUCH_CAPCHA_ID"


@respx.mock
def test_report_incorrect_token_api_error():
    respx.post(f"{BASE_URL}/reportIncorrectTokenCaptcha").mock(
        return_value=Response(200, json={
            "errorId": 1,
            "errorCode": "ERROR_NO_SUCH_CAPCHA_ID",
            "errorDescription": "Task not found"
        })
    )
    client = CapmonsterClient("test_key")
    with pytest.raises(CapmonsterAPIException) as exc_info:
        client.report_incorrect_token(99999)
    assert exc_info.value.error_code == "ERROR_NO_SUCH_CAPCHA_ID"


@respx.mock
@pytest.mark.asyncio
async def test_report_incorrect_image_api_error_async():
    respx.post(f"{BASE_URL}/reportIncorrectImageCaptcha").mock(
        return_value=Response(200, json={
            "errorId": 1,
            "errorCode": "ERROR_NO_SUCH_CAPCHA_ID",
            "errorDescription": "Task not found"
        })
    )
    client = CapmonsterClient("test_key")
    with pytest.raises(CapmonsterAPIException) as exc_info:
        await client.report_incorrect_image_async(99999)
    assert exc_info.value.error_code == "ERROR_NO_SUCH_CAPCHA_ID"


@respx.mock
@pytest.mark.asyncio
async def test_report_incorrect_token_api_error_async():
    respx.post(f"{BASE_URL}/reportIncorrectTokenCaptcha").mock(
        return_value=Response(200, json={
            "errorId": 1,
            "errorCode": "ERROR_NO_SUCH_CAPCHA_ID",
            "errorDescription": "Task not found"
        })
    )
    client = CapmonsterClient("test_key")
    with pytest.raises(CapmonsterAPIException) as exc_info:
        await client.report_incorrect_token_async(99999)
    assert exc_info.value.error_code == "ERROR_NO_SUCH_CAPCHA_ID"


# --- get_user_agent: error path ---

@respx.mock
def test_get_user_agent_network_error():
    respx.get("https://capmonster.cloud/api/useragent/actual").mock(
        side_effect=ConnectionError("Connection refused")
    )
    client = CapmonsterClient("test_key")
    with pytest.raises(CapmonsterException):
        client.get_user_agent()


@respx.mock
@pytest.mark.asyncio
async def test_get_user_agent_network_error_async():
    respx.get("https://capmonster.cloud/api/useragent/actual").mock(
        side_effect=ConnectionError("Connection refused")
    )
    client = CapmonsterClient("test_key")
    with pytest.raises(CapmonsterException):
        await client.get_user_agent_async()


# --- nocache: V2Enterprise and V3Enterprise ---

def test_nocache_recaptcha_v2_enterprise():
    task = RecaptchaV2EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="key123",
        nocache=True
    )
    result = task.to_request()
    assert result["nocache"] is True


def test_nocache_recaptcha_v2_enterprise_excluded_when_none():
    task = RecaptchaV2EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="key123"
    )
    result = task.to_request()
    assert "nocache" not in result


def test_nocache_recaptcha_v3_enterprise():
    task = RecaptchaV3EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="key123",
        nocache=True
    )
    result = task.to_request()
    assert result["nocache"] is True


def test_nocache_recaptcha_v3_enterprise_excluded_when_none():
    task = RecaptchaV3EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="key123"
    )
    result = task.to_request()
    assert "nocache" not in result


# --- RecaptchaV2: cookies + proxy together ---

def test_recaptcha_v2_cookies_and_proxy_together():
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="key123",
        cookies="session=abc; token=xyz",
        proxy=ProxyPayload(
            proxyType="http",
            proxyAddress="1.2.3.4",
            proxyPort=8080
        )
    )
    result = task.to_request()
    assert result["cookies"] == "session=abc; token=xyz"
    assert result["proxyType"] == "http"
    assert result["proxyAddress"] == "1.2.3.4"
    assert result["proxyPort"] == 8080
    assert "proxy" not in result


# --- isEnterprise explicit False ---

def test_recaptcha_v3_is_enterprise_false():
    task = RecaptchaV3Task(
        websiteURL="https://example.com",
        websiteKey="key123",
        isEnterprise=False
    )
    result = task.to_request()
    assert result["isEnterprise"] is False
