# Hunt

Solves Hunt captcha challenges, or generates an X-HD value. Proxy is required.

**API type:** `CustomTask` (with `class: "HUNT"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Full URL of the page with the Hunt captcha. |
| `metadata` | `HuntMetadata` | **required** | Hunt-specific metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload` | **required** | Proxy settings. |

## HuntMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `apiGetLib` | `str` | **required** | Full URL of the Hunt `api.js` file. |
| `data` | `str \| None` | `None` | The `meta.token` value returned by the site. |
| `widgetUrl` | `str \| None` | `None` | Full URL of the Hunt widget, including the query string. |

Pass only `apiGetLib` to generate X-HD. To solve the captcha, add either `data` or `widgetUrl`, never both.

!!!warning Deprecated
`HuntTask(websiteURL=..., websiteKey=...)` without `metadata` still sends the old `HuntTask` request, emits a
`DeprecationWarning`, and will be removed in 6.0.
!!!
