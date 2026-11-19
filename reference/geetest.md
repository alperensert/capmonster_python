# GeeTest

---

## GeeTestV3Task

Solves GeeTest V3 captcha challenges.

**API type:** `GeeTestTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the page with the captcha. |
| `gt` | `str` | **required** | GeeTest identifier key for the domain. |
| `challenge` | `str` | **required** | Dynamic challenge key. Must be fresh per request — reusing a stale value causes `ERROR_TOKEN_EXPIRED`. |
| `geetestApiServerSubdomain` | `str \| None` | `None` | GeeTest API subdomain (must differ from `api.geetest.com`). |
| `geetestGetLib` | `str \| None` | `None` | Path to the captcha script. Must be passed as a JSON string. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

---

## GeeTestV4Task

Solves GeeTest V4 captcha challenges. Automatically sets `version: 4`.

**API type:** `GeeTestTask` (with `version: 4`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the page with the captcha. |
| `gt` | `str` | **required** | GeeTest identifier key for the domain. |
| `initParameters` | `object \| None` | `None` | Extra parameters for v4 (e.g. `{"riskType": "slide"}`). |
| `geetestApiServerSubdomain` | `str \| None` | `None` | GeeTest API subdomain (must differ from `api.geetest.com`). |
| `geetestGetLib` | `str \| None` | `None` | Path to the captcha script. Must be passed as a JSON string. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |
