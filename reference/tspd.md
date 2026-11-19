# TSPD

Solves TSPD challenges. Proxy is required.

**API type:** `CustomTask` (with `class: "tspd"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | URL of the page with the TSPD challenge. |
| `metadata` | `TSPDMetadata` | **required** | TSPD-specific metadata. |
| `userAgent` | `str` | **required** | Browser User-Agent string (must be from Windows OS). |
| `proxy` | `ProxyPayload` | **required** | Proxy settings. |

## TSPDMetadata

| Parameter | Type | Description |
|-----------|------|-------------|
| `tspdCookie` | `str` | Cookies obtained on the TSPD challenge page. |
| `htmlPageBase64` | `str` | Entire TSPD page encoded in base64. |
