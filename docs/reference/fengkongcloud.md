# FengkongCloud [!badge text="NEW" variant="success"]

Solves FengkongCloud captcha challenges. No proxy.

**API type:** `CustomTask` (with `class: "fengkongcloud"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the main page with the captcha. |
| `websiteKey` | `str` | **required** | The `siteKey` value found on the page. |
| `metadata` | `FengkongCloudMetadata \| None` | `None` | Optional metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |

## FengkongCloudMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `apiJsUrl` | `str \| None` | `None` | Link to `smcp.min.js`. |
