# HeyTap [!badge text="NEW" variant="success"]

Solves HeyTap captcha challenges. No proxy.

**API type:** `CustomTask` (with `class: "heytap"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the main page with the captcha. |
| `websiteKey` | `str` | **required** | The `siteKey` value found on the page. |
| `metadata` | `HeyTapMetadata \| None` | `None` | Optional metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |

## HeyTapMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `apiServer` | `str \| None` | `None` | API server domain without `https://`; required if not `captcha-sec.heytapmobi.com`. |
