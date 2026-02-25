# TenDI

Solves TenDI-based captcha challenges.

**API type:** `CustomTask` (with `class: "TenDI"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the page with the captcha. |
| `websiteKey` | `str` | **required** | captchaAppId — unique parameter for your site. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload` | **required** | Proxy settings. |
