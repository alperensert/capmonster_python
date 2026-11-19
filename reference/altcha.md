# Altcha

Solves Altcha proof-of-work challenges.

**API type:** `CustomTask` (with `class: "altcha"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | Main page URL where Altcha is located. |
| `websiteKey` | `str` | `""` | For this task, sending an empty string is allowed. |
| `metadata` | `AltchaMetadata` | **required** | Altcha-specific metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

## AltchaMetadata

| Parameter | Type | Description |
|-----------|------|-------------|
| `challenge` | `str` | Unique task identifier obtained from the website. |
| `iterations` | `str` | Number of iterations (corresponds to `maxnumber` value). |
| `salt` | `str` | Salt obtained from the site, used for hash generation. |
| `signature` | `str` | Digital signature of the request. |
