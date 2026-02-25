# DataDome

Solves DataDome captcha challenges.

**API type:** `CustomTask` (with `class: "DataDome"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the page with the captcha. |
| `metadata` | `DataDomeMetadata` | **required** | Additional captcha metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

## DataDomeMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `datadomeCookie` | `str` | **required** | DataDome cookies from `document.cookie`. |
| `htmlPageBase64` | `str \| None` | `None` | Base64-encoded captcha page data. |
| `captchaUrl` | `str \| None` | `None` | Link to the captcha (e.g. `https://geo.captcha-delivery.com/captcha/?initialCid=...`). |

!!!warning
Exactly one of `htmlPageBase64` or `captchaUrl` must be provided (not both, not neither).
!!!
