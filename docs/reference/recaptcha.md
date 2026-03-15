# reCAPTCHA

---

## RecaptchaV2Task

Solves reCAPTCHA v2 challenges (visible and invisible).

**API type:** `RecaptchaV2Task`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the webpage containing the captcha. |
| `websiteKey` | `str` | **required** | reCAPTCHA site key. |
| `recaptchaDataSValue` | `str \| None` | `None` | One-time `data-s` token for custom implementations. Must be fresh per attempt. |
| `isInvisible` | `bool \| None` | `None` | Set to `True` for invisible reCAPTCHA. |
| `cookies` | `str \| None` | `None` | Additional cookies in the format: `name1=val1; name2=val2`. |
| `nocache` | `bool \| None` | `None` | Set to `True` to force fresh token generation (prevents reuse of cached tokens). |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

---

## RecaptchaV2EnterpriseTask

Solves Google reCAPTCHA V2 Enterprise challenges.

**API type:** `RecaptchaV2EnterpriseTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the webpage with reCAPTCHA Enterprise. |
| `websiteKey` | `str` | **required** | reCAPTCHA site key. |
| `pageAction` | `str \| None` | `None` | Action parameter if different from default `"verify"`. |
| `enterprisePayload` | `str \| None` | `None` | Additional parameters passed to `grecaptcha.enterprise.render`. |
| `apiDomain` | `str \| None` | `None` | Custom domain for loading reCAPTCHA Enterprise. |
| `cookies` | `str \| None` | `None` | Cookies to send with the request. |
| `nocache` | `bool \| None` | `None` | Set to `True` to force fresh token generation (prevents reuse of cached tokens). |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

---

## RecaptchaV3Task

Solves score-based reCAPTCHA v3 challenges. No proxy required.

**API type:** `RecaptchaV3TaskProxyless`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the webpage with the captcha. |
| `websiteKey` | `str` | **required** | reCAPTCHA site key. |
| `minScore` | `float \| None` | `None` | Minimum acceptable score (0.1 – 0.9). |
| `pageAction` | `str \| None` | `None` | Widget action value defined by the site owner. Default: `verify`. |
| `isEnterprise` | `bool \| None` | `None` | Set to `True` to solve as Enterprise (equivalent to `RecaptchaV3EnterpriseTask`). |
| `nocache` | `bool \| None` | `None` | Set to `True` to force fresh token generation (prevents reuse of cached tokens). |

---

## RecaptchaV3EnterpriseTask [!badge text="NEW" variant="success"]

Solves Google reCAPTCHA v3 Enterprise challenges.

**API type:** `RecaptchaV3EnterpriseTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Address of the webpage with reCAPTCHA Enterprise. |
| `websiteKey` | `str` | **required** | reCAPTCHA site key. |
| `minScore` | `float \| None` | `None` | Minimum acceptable score (0.1 – 0.9). |
| `pageAction` | `str \| None` | `None` | Widget action value defined by the site owner. Default: `verify`. |
| `nocache` | `bool \| None` | `None` | Set to `True` to force fresh token generation (prevents reuse of cached tokens). |
