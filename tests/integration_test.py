import os

import pytest

from capmonster_python import (
    CapmonsterClient,
    RecaptchaV2Task,
    RecaptchaV3Task,
)

API_KEY = os.getenv("API_KEY")

pytestmark = pytest.mark.skipif(API_KEY is None, reason="API_KEY is not set")

RECAPTCHA_V2_URL = "https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=high"
RECAPTCHA_V2_KEY = "6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd"

RECAPTCHA_V3_URL = "https://2captcha.com/demo/recaptcha-v3"
RECAPTCHA_V3_KEY = "6LfB5_IbAAAAAMCtsjEHEHKqcB9iQocwwxTiihJu"


# --- RecaptchaV2 sync ---

def test_recaptcha_v2_solve():
    client = CapmonsterClient(API_KEY)
    task = RecaptchaV2Task(websiteURL=RECAPTCHA_V2_URL, websiteKey=RECAPTCHA_V2_KEY)
    result = client.solve(task)
    assert "gRecaptchaResponse" in result
    assert len(result["gRecaptchaResponse"]) > 0


def test_recaptcha_v2_create_and_join():
    client = CapmonsterClient(API_KEY)
    task = RecaptchaV2Task(websiteURL=RECAPTCHA_V2_URL, websiteKey=RECAPTCHA_V2_KEY)
    task_id = client.create_task(task)
    assert task_id != 0
    result = client.join_task_result(task_id)
    assert "gRecaptchaResponse" in result


# --- RecaptchaV2 async ---

@pytest.mark.asyncio
async def test_recaptcha_v2_solve_async():
    client = CapmonsterClient(API_KEY)
    task = RecaptchaV2Task(websiteURL=RECAPTCHA_V2_URL, websiteKey=RECAPTCHA_V2_KEY)
    result = await client.solve_async(task)
    assert "gRecaptchaResponse" in result
    assert len(result["gRecaptchaResponse"]) > 0


@pytest.mark.asyncio
async def test_recaptcha_v2_create_and_join_async():
    client = CapmonsterClient(API_KEY)
    task = RecaptchaV2Task(websiteURL=RECAPTCHA_V2_URL, websiteKey=RECAPTCHA_V2_KEY)
    task_id = await client.create_task_async(task)
    assert task_id != 0
    result = await client.join_task_result_async(task_id)
    assert "gRecaptchaResponse" in result


# --- RecaptchaV3 sync ---

def test_recaptcha_v3_solve():
    client = CapmonsterClient(API_KEY)
    task = RecaptchaV3Task(
        websiteURL=RECAPTCHA_V3_URL,
        websiteKey=RECAPTCHA_V3_KEY,
        minScore=0.3,
        pageAction="verify",
    )
    result = client.solve(task)
    assert "gRecaptchaResponse" in result
    assert len(result["gRecaptchaResponse"]) > 0


def test_recaptcha_v3_create_and_join():
    client = CapmonsterClient(API_KEY)
    task = RecaptchaV3Task(
        websiteURL=RECAPTCHA_V3_URL,
        websiteKey=RECAPTCHA_V3_KEY,
        minScore=0.3,
    )
    task_id = client.create_task(task)
    assert task_id != 0
    result = client.join_task_result(task_id)
    assert "gRecaptchaResponse" in result


# --- RecaptchaV3 async ---

@pytest.mark.asyncio
async def test_recaptcha_v3_solve_async():
    client = CapmonsterClient(API_KEY)
    task = RecaptchaV3Task(
        websiteURL=RECAPTCHA_V3_URL,
        websiteKey=RECAPTCHA_V3_KEY,
        minScore=0.3,
        pageAction="verify",
    )
    result = await client.solve_async(task)
    assert "gRecaptchaResponse" in result
    assert len(result["gRecaptchaResponse"]) > 0


@pytest.mark.asyncio
async def test_recaptcha_v3_create_and_join_async():
    client = CapmonsterClient(API_KEY)
    task = RecaptchaV3Task(
        websiteURL=RECAPTCHA_V3_URL,
        websiteKey=RECAPTCHA_V3_KEY,
        minScore=0.3,
    )
    task_id = await client.create_task_async(task)
    assert task_id != 0
    result = await client.join_task_result_async(task_id)
    assert "gRecaptchaResponse" in result


# --- Balance / report (lightweight API checks) ---

def test_get_balance():
    client = CapmonsterClient(API_KEY)
    balance = client.get_balance()
    assert isinstance(balance, float)
    assert balance >= 0


@pytest.mark.asyncio
async def test_get_balance_async():
    client = CapmonsterClient(API_KEY)
    balance = await client.get_balance_async()
    assert isinstance(balance, float)
    assert balance >= 0


def test_get_user_agent():
    client = CapmonsterClient(API_KEY)
    ua = client.get_user_agent()
    assert "Mozilla" in ua


@pytest.mark.asyncio
async def test_get_user_agent_async():
    client = CapmonsterClient(API_KEY)
    ua = await client.get_user_agent_async()
    assert "Mozilla" in ua
