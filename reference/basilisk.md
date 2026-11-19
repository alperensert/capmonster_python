# Basilisk

Solves Basilisk CAPTCHA challenges.

**API type:** `CustomTask` (with `class: "Basilisk"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the main page where the captcha is solved. |
| `websiteKey` | `str` | **required** | Found in the `data-sitekey` attribute of the captcha container. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
