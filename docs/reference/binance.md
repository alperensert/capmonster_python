# Binance

Solves Binance CAPTCHA challenges. Use only for login flows.

**API type:** `BinanceTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the main page where the captcha is solved. |
| `websiteKey` | `str` | **required** | A unique parameter for your website's section. |
| `validateId` | `str` | **required** | Dynamic key — the value of `validateId`, `securityId`, or `securityCheckResponseValidateId`. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |
