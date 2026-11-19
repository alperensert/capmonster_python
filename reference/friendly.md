# Friendly Captcha [!badge text="NEW" variant="success"]

Solves Friendly Captcha (V1 and V2).

**API type:** `CustomTask` (with `class: "friendly"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Full URL of the page with the captcha. |
| `websiteKey` | `str` | **required** | Friendly Captcha site key. |
| `metadata` | `FriendlyMetadata` | **required** | Friendly-specific metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

## FriendlyMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `apiGetLib` | `str` | **required** | V1: `widget.module.min.js` of `friendly-challenge`; V2: the `site.min.js` loaded on the page. |
