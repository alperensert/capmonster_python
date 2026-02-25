# Turnstile

---

## TurnstileTask

Solves Cloudflare Turnstile captchas in token mode. No proxy required.

**API type:** `TurnstileTaskProxyless`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Page address where the captcha is solved. |
| `websiteKey` | `str` | **required** | Turnstile site key. |
| `pageAction` | `str \| None` | `None` | Action field from the captcha callback function. |
| `data` | `str \| None` | `None` | Value of the `cData` parameter. |

---

## TurnstileCloudFlareTask

Solves Cloudflare challenges that return either a token or a `cf_clearance` cookie. Extends `TurnstileTask`.

**API type:** `TurnstileTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Page address where the captcha is solved. |
| `websiteKey` | `str` | **required** | Turnstile site key. |
| `cloudflareTaskType` | `Literal["token", "cf_clearance"]` | `"token"` | Cloudflare challenge type. |
| `userAgent` | `str` | **required** | Browser User-Agent string (must be from Windows OS). |
| `apiJsUrl` | `str \| None` | `None` | Captcha script URL. **Required** for `token` type. |
| `htmlPageBase64` | `str \| None` | `None` | Base64-encoded HTML page. **Required** for `cf_clearance` type. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. **Required** for `cf_clearance`, must be omitted for `token`. |
| `pageAction` | `str \| None` | `None` | Action field from the captcha callback function. |
| `data` | `str \| None` | `None` | Value of the `cData` parameter. |

### Validation rules

- **`token` type:** `apiJsUrl` is required; `proxy` must be omitted.
- **`cf_clearance` type:** `htmlPageBase64` and `proxy` are both required.

---

## TurnstileWaitingRoomTask [!badge text="NEW" variant="success"]

Solves Cloudflare Waiting Room challenges. Returns a `cf_clearance` cookie. Proxy is required.

**API type:** `TurnstileTask` (with `cloudflareTaskType: "wait_room"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | URL of the page containing the waiting room check. |
| `websiteKey` | `str` | **required** | Cloudflare site key. |
| `htmlPageBase64` | `str` | **required** | Base64-encoded HTML page containing the waiting room. |
| `userAgent` | `str` | **required** | Browser User-Agent string (must be from Windows OS). |
| `proxy` | `ProxyPayload` | **required** | Proxy settings. |
