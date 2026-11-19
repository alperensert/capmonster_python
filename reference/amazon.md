# Amazon WAF

Solves Amazon AWS WAF captcha and challenge pages.

**API type:** `AmazonTask`

Supports multiple solving options:
- **Option 1:** `websiteURL` + `websiteKey` + `captchaScript` (simple captcha)
- **Option 2:** `websiteURL` + `websiteKey` + `challengeScript` + `context` + `iv` (full challenge)
- **Option 3:** `websiteURL` + `challengeScript` (invisible challenge only)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Main page address where the captcha is solved. |
| `websiteKey` | `str \| None` | `None` | Found in the `apiKey` field when rendering captcha. |
| `captchaScript` | `str \| None` | `None` | Link to `jsapi.js` or `captcha.js` on the HTML page. |
| `challengeScript` | `str \| None` | `None` | Link to `challenge.js`. |
| `context` | `str \| None` | `None` | Obtained from `window.gokuProps.context`. |
| `iv` | `str \| None` | `None` | Obtained from `window.gokuProps.iv`. |
| `cookieSolution` | `bool \| None` | `None` | If `True`, returns `aws-waf-token` cookie instead of voucher/token. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |
