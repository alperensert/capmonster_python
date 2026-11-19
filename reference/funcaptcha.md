# FunCaptcha

Solves FunCaptcha (Arkose Labs) challenges.

**API type:** `FunCaptchaTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | URL of the page where the captcha is located. |
| `websitePublicKey` | `str` | **required** | FunCaptcha public key (pk). |
| `funcaptchaApiJSSubdomain` | `str \| None` | `None` | Arkose Labs subdomain (surl). Only if it differs from `client-api.arkoselabs.com`. |
| `data` | `str \| None` | `None` | Additional data parameter, required if the site uses `data[blob]`. |
| `cookies` | `str \| None` | `None` | Additional cookies in `cookieName1=value1; cookieName2=value2` format. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |
