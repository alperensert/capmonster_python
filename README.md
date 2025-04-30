# 🤖 Capmonster Python

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/capmonster-python?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alperensert/capmonster_python?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/alperensert/capmonster_python?style=for-the-badge)
![GitHub Release](https://img.shields.io/github/v/release/alperensert/capmonster_python?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/alperensert/capmonster_python?style=for-the-badge&color=rgb(255%2C%20255%2C%20143)&cacheSeconds=3600)

A modern, strongly typed, async-friendly Python SDK for solving CAPTCHA challenges
using [Capmonster.Cloud](https://capmonster.cloud/).

Supports reCAPTCHA v2 & v3, Cloudflare Turnstile, GeeTest (v3 & v4) and [much more](#-supported-captcha-types).

---

## ✨ Features

- ✅ Fully typed Pydantic v2 models
- 🔁 Both sync and async API support
- 🔐 Proxy and User-Agent configuration
- 📦 Supports the most common CAPTCHA types
- 📚 Intuitive API with powerful task building

---

## 🔧 Installation

```bash
pip install capmonster_python
```

> [!IMPORTANT]  
> You're viewing the documentation for **Capmonster Python v4**, which includes breaking changes. If you prefer the
> old syntax used in versions prior to 4.x, you can continue using it by installing the legacy version:  
> ```pip install capmonster_python==3.2```

## 🚀 Quick Start

### Async Example

```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV3Task


async def main():
    client = CapmonsterClient(api_key="YOUR_API_KEY")

    task = RecaptchaV3Task(
        websiteURL="https://example.com",
        websiteKey="SITE_KEY_HERE",
        minScore=0.5,
        pageAction="verify"
    )

    task_id = await client.create_task_async(task)
    result = await client.join_task_result_async(task_id)
    print(result)


asyncio.run(main())

```

### Sync Example

```python
from capmonster_python import CapmonsterClient, RecaptchaV2Task

client = CapmonsterClient(api_key="<YOUR_API_KEY>")

task = RecaptchaV2Task(
    websiteURL="https://example.com",
    websiteKey="SITE_KEY_HERE"
)

task_id = client.create_task(task)
result = client.join_task_result(task_id)
print(result)
```

---

## 🧠 Supported CAPTCHA Types

Capmonster Python v4 supports a wide range of CAPTCHA formats — from mainstream challenges like reCAPTCHA and Turnstile
to enterprise-grade shields like Imperva and DataDome. Each task supports full Pydantic validation ✅ and both sync and
async clients 🔄 unless noted.

| 🔖 Category               | CAPTCHA Type                   | Class Name                    | Proxy Required | Notes                                  |
|---------------------------|--------------------------------|-------------------------------|----------------|----------------------------------------|
| 🧩 reCAPTCHA              | reCAPTCHA v2                   | `RecaptchaV2Task`             | Optional       | Visible / Invisible supported ✅ 🔄     |
|                           | reCAPTCHA v2 Enterprise        | `RecaptchaV2EnterpriseTask`   | Optional       | `enterprisePayload` & `apiDomain` ✅ 🔄 |
|                           | reCAPTCHA v3                   | `RecaptchaV3Task`             | ❌ No           | Score-based, proxyless ✅ 🔄            |
| 🛡️ Cloudflare            | Turnstile (token)              | `TurnstileTask`               | ❌ No           | Lightweight, async-ready ✅ 🔄          |
|                           | Turnstile (cf_clearance)       | `TurnstileCloudFlareTask`     | ✅ Yes          | Full HTML + proxy required ✅ 🔄        |
| 📸 Image-based            | Image-to-Text OCR              | `ImageToTextTask`             | ❌ No           | Base64 image + module control ✅ 🔄     |
|                           | Complex Image (Recaptcha-like) | `ComplexImageRecaptchaTask`   | ❌ No           | Grid-based, metadata aware ✅ 🔄        |
|                           | Complex Image Recognition (AI) | `ComplexImageRecognitionTask` | ❌ No           | Supports tasks like Shein, OOCL ✅ 🔄   |
| 🧠 Human Behavior         | GeeTest v3                     | `GeeTestV3Task`               | Optional       | Challenge + `gt` key + freshness ✅ 🔄  |
|                           | GeeTest v4                     | `GeeTestV4Task`               | Optional       | `initParameters` supported ✅ 🔄        |
| 🛡️ Enterprise Protection | DataDome                       | `DataDomeTask`                | ✅ Recommended  | Cookie & page context needed ✅ 🔄      |
|                           | Imperva                        | `ImpervaTask`                 | ✅ Recommended  | Incapsula + Reese84 logic ✅ 🔄         |
| 🏦 Platform-Specific      | Binance Login                  | `BinanceTask`                 | ✅ Yes          | `validateId` for login flow ✅ 🔄       |
|                           | Temu                           | `TemuTask`                    | ❌ No           | Cookie-injected behavioral solver ✅ 🔄 |
|                           | TenDI                          | `TenDITask`                   | ✅ Yes          | Custom captchaAppId field ✅ 🔄         |
| 🧪 Miscellaneous          | Prosopo                        | `ProsopoTask`                 | Optional       | Used in zk or crypto UIs ✅ 🔄          |
|                           | Basilisk                       | `BasiliskTask`                | ❌ No           | Minimalist site-key puzzle ✅ 🔄        |

## 🧩 Advanced Usage

- Callback URLs are supported during task creation.
- Includes auto-retry loop for polling results (up to 120s)

## 💬 Community & Support

Need help or have a question?

- 📧 Contact: business@alperen.io
- 🐛 Found a bug? [Open an issue](https://github.com/alperensert/capmonster_python/issues)

> [!NOTE]  
> Community support is intended only for questions and issues related to this project. Custom usage scenarios,
> integrations, or application-specific logic are outside the scope of support.

## 📄 License

This project is licensed under the [MIT License](/LICENSE).
