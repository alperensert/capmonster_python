# Castle

Solves Castle challenges.

**API type:** `CustomTask` (with `class: "Castle"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | URL of the page where Castle is located. |
| `websiteKey` | `str` | **required** | Castle publishable key. |
| `metadata` | `CastleMetadata` | **required** | Castle-specific metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |
| `proxy` | `ProxyPayload \| None` | `None` | Proxy settings. |

## CastleMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `wUrl` | `str` | **required** | Link to `cw.js` file. |
| `swUrl` | `str` | **required** | Link to `csw.js` file. |
| `count` | `int \| None` | `None` | Number of tokens to generate (default 1, max 49). |
