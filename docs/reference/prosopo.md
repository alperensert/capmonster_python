# Prosopo

Solves Prosopo CAPTCHA challenges.

**API type:** `ProsopoTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Full URL of the CAPTCHA page. |
| `websiteKey` | `str` | **required** | The `siteKey` parameter value from the page. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |
