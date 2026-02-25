---
icon: home
label: Home
order: 100
---

# Capmonster Python

Welcome to the documentation for **capmonster_python** — a modern, fully typed, async-ready Python SDK
for [Capmonster.Cloud](https://capmonster.cloud/).

Integrate with 20+ CAPTCHA challenge types including reCAPTCHA, Turnstile, GeeTest, FunCaptcha,
Image-to-Text, and more — with both sync and async support out of the box.

---

## Quick Start

- [Installation](installation.md) — Get up and running in seconds
- [Examples](examples.md) — Copy-paste code for every task type
- [API Reference](reference/overview.md) — Full parameter docs for all classes

---

## Features

- Async-first design powered by `httpx`
- Full Pydantic v2 data validation
- Context manager support (`with` / `async with`)
- `solve()` convenience method — create + poll in one call
- Configurable polling (`max_retries`, `retry_delay`)
- Task abstraction for all Capmonster types
- Clear and typed API responses
- Retry logic and error wrapping

---

## Supported Task Types

| Category | Tasks |
|----------|-------|
| **reCAPTCHA** | V2, V2 Enterprise, V3, V3 Enterprise [!badge text="NEW" variant="success"] |
| **Turnstile** | Token, CloudFlare (cf_clearance), Waiting Room [!badge text="NEW" variant="success"] |
| **GeeTest** | V3, V4 |
| **Image-Based** | ImageToText, ComplexImageRecaptcha, ComplexImageRecognition |
| **Enterprise** | DataDome, Imperva, Amazon WAF [!badge text="NEW" variant="success"] |
| **Platform** | Binance, Temu, TenDI |
| **Other** | Prosopo, Basilisk, FunCaptcha [!badge text="NEW" variant="success"], MTCaptcha [!badge text="NEW" variant="success"], Yidun [!badge text="NEW" variant="success"], Altcha [!badge text="NEW" variant="success"], Castle [!badge text="NEW" variant="success"], TSPD [!badge text="NEW" variant="success"] |

---

## Project Status

This library is **actively maintained** and tracks the latest Capmonster Cloud API. It targets Python 3.9+ and is distributed under the MIT license.

!!!warning Disclaimer
This project is an **unofficial, community-maintained** SDK. It is **not affiliated with, endorsed by, or supported by** ZennoLab or Capmonster.Cloud.

The authors of this library make **no guarantees** about the availability, accuracy, or reliability of the Capmonster Cloud service itself. Use at your own risk.

By using this library you agree to comply with the [Capmonster Cloud Terms of Service](https://capmonster.cloud/). The authors accept **no liability** for any damages, account restrictions, or other consequences arising from its use.
!!!
