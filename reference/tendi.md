# TenDI

Solves TenDI-based captcha challenges.

**API type:** `CustomTask` (with `class: "TenDI"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the page with the captcha. |
| `websiteKey` | `str` | **required** | captchaAppId — unique parameter for your site. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `metadata` | `TenDIMetadata \| None` | `None` | Optional TenDI-specific metadata. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

## TenDIMetadata [!badge text="NEW" variant="success"]

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `captchaUrl` | `str \| None` | `None` | Link to the captcha script, if the site loads it from a custom domain. |
| `aidEncrypted` | `str \| None` | `None` | Single-use encrypted Aid value issued by the site, if it uses one. |
