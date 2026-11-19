# ARCaptcha [!badge text="NEW" variant="success"]

Solves ARCaptcha challenges. No proxy.

**API type:** `ArCaptchaTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the main page with the captcha. |
| `websiteKey` | `str` | **required** | The `siteKey` value found on the page. |
| `isInvisible` | `bool \| None` | `None` | Set to `True` for invisible ARCaptcha. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
