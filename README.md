# Capmonster Python

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/capmonster-python?style=for-the-badge)](https://pypi.org/project/capmonster-python/)
[![GitHub Release](https://img.shields.io/github/v/release/alperensert/capmonster_python?style=for-the-badge)](https://github.com/alperensert/capmonster_python/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/alperensert/capmonster_python?style=for-the-badge)](https://github.com/alperensert/capmonster_python/commits/master)
[![GitHub Repo stars](https://img.shields.io/github/stars/alperensert/capmonster_python?style=for-the-badge&color=rgb(255%2C%20255%2C%20143)&cacheSeconds=3600)](https://github.com/alperensert/capmonster_python)

A modern, strongly-typed Python SDK for [CapMonster Cloud](https://capmonster.cloud/) — solve reCAPTCHA, Turnstile, GeeTest, and 20+ other CAPTCHA types with both sync and async support.

## Installation

```bash
pip install capmonster_python
```

> [!IMPORTANT]
> This is **v4** of Capmonster Python, which includes breaking changes from v3.x.
> For the legacy API: `pip install capmonster_python==3.2`

## Quick Start

```python
from capmonster_python import CapmonsterClient, RecaptchaV2Task

client = CapmonsterClient(api_key="YOUR_API_KEY")

task = RecaptchaV2Task(
    websiteURL="https://example.com",
    websiteKey="SITE_KEY_HERE"
)

result = client.solve(task)
print(result)  # {"gRecaptchaResponse": "03AGdBq24..."}
```

### Async

```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV3Task

async def main():
    async with CapmonsterClient(api_key="YOUR_API_KEY") as client:
        task = RecaptchaV3Task(
            websiteURL="https://example.com",
            websiteKey="SITE_KEY_HERE",
            minScore=0.5,
            pageAction="verify"
        )
        result = await client.solve_async(task)
        print(result)

asyncio.run(main())
```

### With Proxy

```python
from capmonster_python import CapmonsterClient, RecaptchaV2Task, ProxyPayload

client = CapmonsterClient(api_key="YOUR_API_KEY")

task = RecaptchaV2Task(
    websiteURL="https://example.com",
    websiteKey="SITE_KEY_HERE",
    proxy=ProxyPayload(
        proxyType="http",
        proxyAddress="1.2.3.4",
        proxyPort=8080,
        proxyLogin="user",
        proxyPassword="pass"
    )
)

result = client.solve(task)
```

## Client API

```python
CapmonsterClient(api_key, timeout=30.0, max_retries=120, retry_delay=2.0)
```

| Method | Description |
|--------|-------------|
| `solve(task)` | Create task and poll until solved |
| `create_task(task)` | Create a task, returns `task_id` |
| `join_task_result(task_id)` | Poll until result is ready |
| `get_task_result(task_id)` | Single poll (no waiting) |
| `get_balance()` | Get account balance |
| `get_user_agent()` | Get current valid User-Agent string |
| `report_incorrect_image(task_id)` | Report bad image captcha solution |
| `report_incorrect_token(task_id)` | Report bad token captcha solution |

All methods have async variants with the `_async` suffix (e.g. `solve_async`, `get_balance_async`).

Both sync and async context managers are supported for proper connection cleanup.

## Supported CAPTCHA Types

### reCAPTCHA

| CAPTCHA Type | Class | Proxy |
|---|---|---|
| reCAPTCHA v2 | `RecaptchaV2Task` | Optional |
| reCAPTCHA v2 Enterprise | `RecaptchaV2EnterpriseTask` | Optional |
| reCAPTCHA v3 | `RecaptchaV3Task` | No |
| reCAPTCHA v3 Enterprise | `RecaptchaV3EnterpriseTask` | No |
| reCAPTCHA Click | `RecaptchaClickTask` | Optional |

### Cloudflare

| CAPTCHA Type | Class | Proxy |
|---|---|---|
| Turnstile | `TurnstileTask` | No |
| Turnstile Challenge (cf_clearance) | `TurnstileCloudFlareTask` | Required |
| Turnstile Waiting Room | `TurnstileWaitingRoomTask` | Required |

### Image-Based

| CAPTCHA Type | Class | Proxy |
|---|---|---|
| Image-to-Text OCR | `ImageToTextTask` | No |
| Complex Image (reCAPTCHA grid) | `ComplexImageRecaptchaTask` | No |
| Complex Image Recognition | `ComplexImageRecognitionTask` | No |

### Behavioral / Interactive

| CAPTCHA Type | Class | Proxy |
|---|---|---|
| GeeTest v3 | `GeeTestV3Task` | Optional |
| GeeTest v4 | `GeeTestV4Task` | Optional |
| FunCaptcha (Arkose Labs) | `FunCaptchaTask` | Optional |
| Hunt | `HuntTask` | Optional |

### Enterprise Protection

| CAPTCHA Type | Class | Proxy |
|---|---|---|
| DataDome | `DataDomeTask` | Required |
| Imperva (Incapsula) | `ImpervaTask` | Required |
| Amazon WAF | `AmazonTask` | Optional |
| TSPD | `TSPDTask` | Optional |

### Platform-Specific

| CAPTCHA Type | Class | Proxy |
|---|---|---|
| Binance | `BinanceTask` | Required |
| Temu | `TemuTask` | No |
| TenDI | `TenDITask` | Required |

### Other

| CAPTCHA Type | Class | Proxy |
|---|---|---|
| Altcha | `AltchaTask` | No |
| Basilisk | `BasiliskTask` | No |
| Castle | `CastleTask` | No |
| MTCaptcha | `MTCaptchaTask` | Optional |
| Prosopo | `ProsopoTask` | Optional |
| Yidun | `YidunTask` | Optional |

> Don't see your captcha type? Use `VanillaTaskPayload` to build custom task payloads without waiting for an SDK update.

## Advanced Usage

### Callback URLs

```python
result = client.solve(task, callback_url="https://yoursite.com/callback")
```

### Report Incorrect Solutions

```python
task_id = client.create_task(task)
result = client.join_task_result(task_id)

# If the token was rejected by the target site:
client.report_incorrect_token(task_id)
```

### Fresh Token Generation

Use `nocache=True` on reCAPTCHA tasks to prevent cached token reuse:

```python
task = RecaptchaV2Task(
    websiteURL="https://example.com",
    websiteKey="SITE_KEY_HERE",
    nocache=True
)
```

## Documentation

Full API reference available at [alperensert.github.io/capmonster_python](https://alperensert.github.io/capmonster_python/).

## Support

- Found a bug? [Open an issue](https://github.com/alperensert/capmonster_python/issues)
- Contact: business@alperen.io

> [!NOTE]
> Support is limited to questions and issues related to this project. Custom integrations and application-specific logic are outside the scope of support.

## License

[MIT License](/LICENSE)
