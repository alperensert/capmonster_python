---
icon: code
label: Examples
order: 80
---

# Examples

Below are example usages for various task types, shown in both async and sync format using `CapmonsterClient`.

---

## Context Manager

Using a context manager ensures HTTP connections are properly closed when you're done.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV2Task

async def main():
    async with CapmonsterClient(api_key="<API_KEY>") as client:
        task = RecaptchaV2Task(
            websiteURL="https://example.com",
            websiteKey="<site_key>"
        )
        task_id = await client.create_task_async(task=task)
        result = await client.get_task_result_async(task_id=task_id)
        print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, RecaptchaV2Task

with CapmonsterClient(api_key="<API_KEY>") as client:
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="<site_key>"
    )
    task_id = client.create_task(task=task)
    result = client.get_task_result(task_id=task_id)
    print(result)
```
+++

---

## solve() Convenience Method

The `solve()` method combines `create_task` + `join_task_result` into a single call.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV2Task

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    result = await client.solve_async(RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="<site_key>"
    ))
    print(result.get("gRecaptchaResponse"))

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, RecaptchaV2Task

client = CapmonsterClient(api_key="<API_KEY>")
result = client.solve(RecaptchaV2Task(
    websiteURL="https://example.com",
    websiteKey="<site_key>"
))
print(result.get("gRecaptchaResponse"))
```
+++

---

## Configurable Polling

Customize the polling behavior when waiting for task results with `max_retries` and `retry_delay`.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV2Task

async def main():
    client = CapmonsterClient(
        api_key="<API_KEY>",
        max_retries=60,
        retry_delay=2.0
    )
    result = await client.solve_async(RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="<site_key>"
    ))
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, RecaptchaV2Task

client = CapmonsterClient(
    api_key="<API_KEY>",
    max_retries=60,
    retry_delay=2.0
)
result = client.solve(RecaptchaV2Task(
    websiteURL="https://example.com",
    websiteKey="<site_key>"
))
print(result)
```
+++

---

## reCAPTCHA v2

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV2Task

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = RecaptchaV2Task(
        websiteURL="https://example.com",
        websiteKey="<site_key>",
        isInvisible=False
    )
    task_id = await client.create_task_async(task=task)
    result = await client.get_task_result_async(task_id=task_id)
    print(result.get("gRecaptchaResponse"))

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, RecaptchaV2Task

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(task=RecaptchaV2Task(
    websiteURL="https://example.com",
    websiteKey="<site_key>",
    isInvisible=False
))
response = client.get_task_result(task_id=task_id)
print(response.get("gRecaptchaResponse"))
```
+++

---

## reCAPTCHA v2 Enterprise

Used for solving Google reCAPTCHA V2 Enterprise challenges.
Optional support for `enterprisePayload`, custom `apiDomain`, and `cookies`.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV2EnterpriseTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = RecaptchaV2EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="<site_key>",
        enterprisePayload="{\"s\":\"abc123\"}",
        cookies="cookie=value;cookie_2=value2"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result.get("gRecaptchaResponse"))

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, RecaptchaV2EnterpriseTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(RecaptchaV2EnterpriseTask(
    websiteURL="https://example.com",
    websiteKey="<site_key>",
    enterprisePayload="{\"s\":\"abc123\"}",
    cookies="cookie=value;cookie_2=value2"
))
result = client.get_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```
+++

---

## reCAPTCHA v3

Used for solving score-based reCAPTCHA v3 challenges without requiring a proxy.
You can optionally provide `minScore` and `pageAction` to match expected interaction patterns.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV3Task

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = RecaptchaV3Task(
        websiteURL="https://example.com",
        websiteKey="<site_key>",
        minScore=0.5,
        pageAction="verify"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result.get("gRecaptchaResponse"))

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, RecaptchaV3Task

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(RecaptchaV3Task(
    websiteURL="https://example.com",
    websiteKey="<site_key>",
    minScore=0.5,
    pageAction="verify"
))
result = client.get_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```
+++

---

## reCAPTCHA v3 Enterprise [!badge text="NEW" variant="success"]

Used for solving Google reCAPTCHA v3 Enterprise challenges.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, RecaptchaV3EnterpriseTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = RecaptchaV3EnterpriseTask(
        websiteURL="https://example.com",
        websiteKey="<site_key>",
        minScore=0.7,
        pageAction="login"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result.get("gRecaptchaResponse"))

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, RecaptchaV3EnterpriseTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(RecaptchaV3EnterpriseTask(
    websiteURL="https://example.com",
    websiteKey="<site_key>",
    minScore=0.7,
    pageAction="login"
))
result = client.get_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```
+++

---

## ImageToText

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, ImageToTextTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = ImageToTextTask(
        body="<base64-image>",
        recognizingThreshold=95
    )
    task_id = await client.create_task_async(task=task)
    result = await client.get_task_result_async(task_id=task_id)
    print(result.get("text"))

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, ImageToTextTask

client = CapmonsterClient(api_key="<API_KEY>")
task = ImageToTextTask(
    body="<base64-image>",
    recognizingThreshold=95
)
task_id = client.create_task(task=task)
response = client.get_task_result(task_id=task_id)
print(response.get("text"))
```
+++

---

## GeeTest v3

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, GeeTestV3Task

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = GeeTestV3Task(
        websiteURL="https://example.com",
        gt="<gt-value>",
        challenge="<challenge-value>"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, GeeTestV3Task

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(GeeTestV3Task(
    websiteURL="https://example.com",
    gt="<gt-value>",
    challenge="<challenge-value>"
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## GeeTest v4

Used for solving advanced GeeTest v4 captchas which require both `gt` and `initParameters`.
The challenge is generated dynamically per user and must be fresh.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, GeeTestV4Task

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = GeeTestV4Task(
        websiteURL="https://example.com",
        gt="<gt-value>",
        initParameters={"riskType": "slide"}
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, GeeTestV4Task

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(GeeTestV4Task(
    websiteURL="https://example.com",
    gt="<gt-value>",
    initParameters={"riskType": "slide"}
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## TurnstileTask (Token-based)

For solving Cloudflare Turnstile captchas using token mode. No proxy required.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, TurnstileTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = TurnstileTask(
        websiteURL="https://example.com",
        websiteKey="turnstile-site-key"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, TurnstileTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(TurnstileTask(
    websiteURL="https://example.com",
    websiteKey="turnstile-site-key"
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## TurnstileCloudFlareTask (cf_clearance)

Used for bypassing complex Cloudflare protection involving `cf_clearance` cookie and HTML snapshot.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, TurnstileCloudFlareTask, ProxyPayload

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = TurnstileCloudFlareTask(
        cloudflareTaskType="cf_clearance",
        websiteURL="https://example.com",
        websiteKey="<website_key>",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        htmlPageBase64="<base64-encoded-page>",
        proxy=ProxyPayload(
            proxyType="https",
            proxyAddress="192.168.1.1",
            proxyPort=8000)
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, TurnstileCloudFlareTask, ProxyPayload

client = CapmonsterClient(api_key="<API_KEY>")
task = TurnstileCloudFlareTask(
    cloudflareTaskType="cf_clearance",
    websiteURL="https://example.com",
    websiteKey="<website_key>",
    userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    htmlPageBase64="<base64-encoded-page>",
    proxy=ProxyPayload(
        proxyType="https",
        proxyAddress="192.168.1.1",
        proxyPort=8000)
)
task_id = client.create_task(task=task)
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Cloudflare Waiting Room [!badge text="NEW" variant="success"]

Used for bypassing Cloudflare Waiting Room challenges. Proxy is required.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, TurnstileWaitingRoomTask, ProxyPayload

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = TurnstileWaitingRoomTask(
        websiteURL="https://example.com",
        websiteKey="<website_key>",
        htmlPageBase64="<base64-encoded-page>",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        proxy=ProxyPayload(
            proxyType="https",
            proxyAddress="192.168.1.1",
            proxyPort=8080)
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, TurnstileWaitingRoomTask, ProxyPayload

client = CapmonsterClient(api_key="<API_KEY>")
task = TurnstileWaitingRoomTask(
    websiteURL="https://example.com",
    websiteKey="<website_key>",
    htmlPageBase64="<base64-encoded-page>",
    userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    proxy=ProxyPayload(
        proxyType="https",
        proxyAddress="192.168.1.1",
        proxyPort=8080)
)
task_id = client.create_task(task=task)
result = client.get_task_result(task_id)
print(result)
```
+++

---

## DataDome

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, DataDomeTask, DataDomeMetadata

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = DataDomeTask(
        websiteURL="https://example.com",
        metadata=DataDomeMetadata(
            datadomeCookie="datadome=...",
            captchaUrl="https://captcha-url"
        )
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, DataDomeTask, DataDomeMetadata

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(DataDomeTask(
    websiteURL="https://example.com",
    metadata=DataDomeMetadata(
        datadomeCookie="datadome=...",
        captchaUrl="https://captcha-url"
    )
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Complex Image reCAPTCHA

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, ComplexImageRecaptchaTask, ComplexImageRecaptchaMetadata

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = ComplexImageRecaptchaTask(
        imageUrls=["https://cdn.example.com/captcha1.png"],
        metadata=ComplexImageRecaptchaMetadata(Task="Click on traffic lights", Grid="3x3")
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, ComplexImageRecaptchaTask, ComplexImageRecaptchaMetadata

client = CapmonsterClient(api_key="<API_KEY>")
task = ComplexImageRecaptchaTask(
    imageUrls=["https://cdn.example.com/captcha1.png"],
    metadata=ComplexImageRecaptchaMetadata(Task="Click on traffic lights", Grid="3x3")
)
task_id = client.create_task(task=task)
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Imperva

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, ImpervaTask, ImpervaTaskMetadata

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = ImpervaTask(
        websiteURL="https://example.com",
        metadata=ImpervaTaskMetadata(
            incapsulaScriptUrl="https://example.com/js.inc",
            incapsulaCookie="visid_incap_12345=...",
        )
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, ImpervaTask, ImpervaTaskMetadata

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(ImpervaTask(
    websiteURL="https://example.com",
    metadata=ImpervaTaskMetadata(
        incapsulaScriptUrl="https://example.com/js.inc",
        incapsulaCookie="visid_incap_12345=...",
    )
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Amazon WAF [!badge text="NEW" variant="success"]

Used for solving Amazon AWS WAF captcha and challenge pages.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, AmazonTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = AmazonTask(
        websiteURL="https://example.com",
        websiteKey="<apiKey>",
        captchaScript="https://example.com/jsapi.js",
        challengeScript="https://example.com/challenge.js",
        context="<window.gokuProps.context>",
        iv="<window.gokuProps.iv>"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, AmazonTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(AmazonTask(
    websiteURL="https://example.com",
    websiteKey="<apiKey>",
    captchaScript="https://example.com/jsapi.js",
    challengeScript="https://example.com/challenge.js",
    context="<window.gokuProps.context>",
    iv="<window.gokuProps.iv>"
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## FunCaptcha [!badge text="NEW" variant="success"]

Used for solving FunCaptcha (Arkose Labs) challenges.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, FunCaptchaTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = FunCaptchaTask(
        websiteURL="https://example.com",
        websitePublicKey="<public_key>"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, FunCaptchaTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(FunCaptchaTask(
    websiteURL="https://example.com",
    websitePublicKey="<public_key>"
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Basilisk

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, BasiliskTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = BasiliskTask(
        websiteURL="https://example.com",
        websiteKey="site_key_value"
    )
    task_id = await client.create_task_async(task=task)
    result = await client.get_task_result_async(task_id=task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, BasiliskTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(BasiliskTask(
    websiteURL="https://example.com",
    websiteKey="site_key_value"
))
result = client.get_task_result(task_id=task_id)
print(result)
```
+++

---

## Binance

Used specifically for login flows involving Binance CAPTCHA protection.
You must supply a valid `validateId` (such as `securityId`, `validateId`, or similar) retrieved from the page.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, BinanceTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = BinanceTask(
        websiteURL="https://binance.com",
        websiteKey="binance-key",
        validateId="securityCheckResponseValidateId_value"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, BinanceTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(BinanceTask(
    websiteURL="https://binance.com",
    websiteKey="binance-key",
    validateId="securityCheckResponseValidateId_value"
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Temu

Used to bypass CAPTCHA challenges on Temu using extracted cookies.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, TemuTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = TemuTask(
        websiteURL="https://temu.com",
        cookie="session_id=abc123;"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, TemuTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(TemuTask(
    websiteURL="https://temu.com",
    cookie="session_id=abc123;cookie_2=value2;"
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## TenDI

Used to solve TenDI-based captcha challenges with a known `websiteKey` (captchaAppId).

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, TenDITask, ProxyPayload

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = TenDITask(
        websiteURL="https://example.com",
        websiteKey="189123456",
        proxy=ProxyPayload(
            proxyType="https",
            proxyAddress="192.168.1.1",
            proxyPort=8080,
            proxyLogin="<login>",
            proxyPassword="<password>"
        )
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, TenDITask, ProxyPayload

client = CapmonsterClient(api_key="<API_KEY>")
task = TenDITask(
    websiteURL="https://example.com",
    websiteKey="189123456",
    proxy=ProxyPayload(
        proxyType="https",
        proxyAddress="192.168.1.1",
        proxyPort=8080,
        proxyLogin="<login>",
        proxyPassword="<password>"
    )
)
task_id = client.create_task(task=task)
result = client.get_task_result(task_id)
print(result)
```
+++

---

## MTCaptcha [!badge text="NEW" variant="success"]

Used for solving MTCaptcha challenges.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, MTCaptchaTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = MTCaptchaTask(
        websiteURL="https://example.com",
        websiteKey="<mtcaptcha_site_key>"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, MTCaptchaTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(MTCaptchaTask(
    websiteURL="https://example.com",
    websiteKey="<mtcaptcha_site_key>"
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Yidun (NECaptcha) [!badge text="NEW" variant="success"]

Used for solving Yidun (NECaptcha) challenges.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, YidunTask

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = YidunTask(
        websiteURL="https://example.com",
        websiteKey="<yidun_site_key>"
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, YidunTask

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(YidunTask(
    websiteURL="https://example.com",
    websiteKey="<yidun_site_key>"
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Altcha [!badge text="NEW" variant="success"]

Used for solving Altcha proof-of-work challenges.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, AltchaTask, AltchaMetadata

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = AltchaTask(
        websiteURL="https://example.com",
        metadata=AltchaMetadata(
            challenge="<challenge>",
            iterations="<iterations>",
            salt="<salt>",
            signature="<signature>"
        )
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, AltchaTask, AltchaMetadata

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(AltchaTask(
    websiteURL="https://example.com",
    metadata=AltchaMetadata(
        challenge="<challenge>",
        iterations="<iterations>",
        salt="<salt>",
        signature="<signature>"
    )
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## Castle [!badge text="NEW" variant="success"]

Used for solving Castle challenges.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, CastleTask, CastleMetadata

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = CastleTask(
        websiteURL="https://example.com",
        websiteKey="<publishable_key>",
        metadata=CastleMetadata(
            wUrl="https://example.com/cw.js",
            swUrl="https://example.com/csw.js"
        )
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, CastleTask, CastleMetadata

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(CastleTask(
    websiteURL="https://example.com",
    websiteKey="<publishable_key>",
    metadata=CastleMetadata(
        wUrl="https://example.com/cw.js",
        swUrl="https://example.com/csw.js"
    )
))
result = client.get_task_result(task_id)
print(result)
```
+++

---

## TSPD [!badge text="NEW" variant="success"]

Used for solving TSPD challenges. Proxy is required.

+++ Async
```python
import asyncio
from capmonster_python import CapmonsterClient, TSPDTask, TSPDMetadata, ProxyPayload

async def main():
    client = CapmonsterClient(api_key="<API_KEY>")
    task = TSPDTask(
        websiteURL="https://example.com",
        userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        metadata=TSPDMetadata(
            tspdCookie="<tspd_cookies>",
            htmlPageBase64="<base64-encoded-page>"
        ),
        proxy=ProxyPayload(
            proxyType="https",
            proxyAddress="192.168.1.1",
            proxyPort=8080)
    )
    task_id = await client.create_task_async(task)
    result = await client.get_task_result_async(task_id)
    print(result)

asyncio.run(main())
```
+++ Sync
```python
from capmonster_python import CapmonsterClient, TSPDTask, TSPDMetadata, ProxyPayload

client = CapmonsterClient(api_key="<API_KEY>")
task_id = client.create_task(TSPDTask(
    websiteURL="https://example.com",
    userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    metadata=TSPDMetadata(
        tspdCookie="<tspd_cookies>",
        htmlPageBase64="<base64-encoded-page>"
    ),
    proxy=ProxyPayload(
        proxyType="https",
        proxyAddress="192.168.1.1",
        proxyPort=8080)
))
result = client.get_task_result(task_id)
print(result)
```
+++
