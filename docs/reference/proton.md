# Proton Captcha [!badge text="NEW" variant="success"]

Solves Proton Captcha challenges. Proxy is required.

**API type:** `CustomTask` (with `class: "proton"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the main page with the captcha. |
| `metadata` | `ProtonMetadata` | **required** | Proton-specific metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload` | **required** | Proxy settings. |

## ProtonMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `HumanVerificationToken` | `str` | **required** | Token from the site's response. |
| `pageAction` | `Literal["login", "signup"]` | **required** | Action on the site. |
