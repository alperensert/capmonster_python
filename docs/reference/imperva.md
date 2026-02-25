# Imperva

Solves Imperva (Incapsula) challenges.

**API type:** `CustomTask` (with `class: "Imperva"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `websiteURL` | `str` | **required** | URL of the target website. |
| `metadata` | `ImpervaTaskMetadata` | **required** | Imperva-specific metadata. |
| `userAgent` | `str \| None` | `None` | Browser User-Agent string. |

## ImpervaTaskMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `incapsulaScriptUrl` | `str` | **required** | Name/URL of the Incapsula JS file. |
| `incapsulaCookie` | `str` | **required** | Cookies from Incapsula (via `document.cookie`). |
| `reese84UrlEndpoint` | `str \| None` | `None` | Endpoint where reese84 fingerprint is sent (ends with `?d=site.com`). |
