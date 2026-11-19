# Alibaba [!badge text="NEW" variant="success"]

Solves Alibaba captcha and Alibaba WAF challenges.

**API type:** `CustomTask` (with `class: "alibaba"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Full URL of the page with the captcha. |
| `metadata` | `AlibabaMetadata` | **required** | Alibaba-specific metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

## AlibabaMetadata

`sceneId` and `prefix` are required unless `punishUrl` is set. Pass the other fields only if the website uses them.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `sceneId` | `str \| None` | `None` | Captcha scenario identifier. |
| `prefix` | `str \| None` | `None` | Captcha initialization parameter (subdomain of the `captcha-open` URL). |
| `userId` | `str \| None` | `None` | User or session identifier on the website side. |
| `userUserId` | `str \| None` | `None` | Secondary user identifier. |
| `verifyType` | `str \| None` | `None` | Verification mechanism version, e.g. `"1.0"`. |
| `region` | `str \| None` | `None` | Region that processes the captcha, e.g. `"cn"` or `"sgp"`. |
| `UserCertifyId` | `str \| None` | `None` | Verification ID of the captcha session. |
| `apiGetLib` | `str \| None` | `None` | Link to the captcha JS library used by the website. |
| `punishUrl` | `str \| None` | `None` | Full URL of the `/punish` verification page, including its query string. |
| `cookieRequired` | `bool \| None` | `None` | Return cookies with the solution (Alibaba WAF). |
