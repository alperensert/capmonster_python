# Temu

Solves CAPTCHA challenges on Temu using extracted cookies.

**API type:** `CustomTask` (with `class: "Temu"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Full URL of the page where the CAPTCHA is loaded. |
| `cookie` | `str` | **required** | Cookies obtained from the CAPTCHA page. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
