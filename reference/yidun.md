# Yidun (NECaptcha)

Solves Yidun (NECaptcha) challenges. Supports standard and Enterprise versions.

**API type:** `YidunTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Full URL of the page with the captcha. |
| `websiteKey` | `str` | **required** | The `siteKey` value found on the page. |
| `yidunGetLib` | `str \| None` | `None` | Full URL to the JS file loading the captcha. Recommended for Enterprise. |
| `yidunApiServerSubdomain` | `str \| None` | `None` | Subdomain of the Yidun API server. Required for custom/Enterprise servers. |
| `challenge` | `str \| None` | `None` | Unique identifier of the current captcha (Enterprise). |
| `hcg` | `str \| None` | `None` | Captcha hash used in the request (Enterprise). |
| `hct` | `int \| None` | `None` | Numeric timestamp for Enterprise validation. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |
