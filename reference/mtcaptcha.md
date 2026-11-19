# MTCaptcha

Solves MTCaptcha challenges.

**API type:** `MTCaptchaTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | URL of the page where the captcha is solved. |
| `websiteKey` | `str` | **required** | MTCaptcha site key (passed as `sk` in network requests). |
| `pageAction` | `str \| None` | `None` | Action parameter (passed as `act` in requests). Only needed if different from default. |
| `isInvisible` | `bool \| None` | `None` | Set to `True` if the captcha is invisible. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |
