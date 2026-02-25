# Abstract Base Classes

These are the base classes used internally to build all task payloads. You typically don't instantiate them directly, but they are useful for understanding the type hierarchy and for building custom tasks via `VanillaTaskPayload`.

---

## TaskPayload

```python
class TaskPayload(BaseModel, ABC)
```

Abstract base model for all task payloads. Every task type inherits from this class.

| Attribute | Type | Description |
|-----------|------|-------------|
| `type` | `str` | The task type identifier sent to the Capmonster API (e.g. `"RecaptchaV2Task"`). |

### Methods

#### `to_request() -> dict[str, Any]`

Abstract method. Converts the task instance into a dictionary suitable for the API request body.

---

## ProxyPayload

```python
class ProxyPayload(BaseModel)
```

Proxy configuration model. Used by tasks that support or require proxy settings.

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `proxyType` | `Literal["http", "https", "socks4", "socks5"]` | **required** | Type of the proxy. |
| `proxyAddress` | `str` | **required** | IPv4/IPv6 proxy address. Hostnames and local proxies are not allowed. |
| `proxyPort` | `int` | **required** | Port of the proxy. |
| `proxyLogin` | `str \| None` | `None` | Username for proxy authentication. |
| `proxyPassword` | `str \| None` | `None` | Password for proxy authentication. |

### Example

```python
from capmonster_python import ProxyPayload

proxy = ProxyPayload(
    proxyType="https",
    proxyAddress="192.168.1.1",
    proxyPort=8080,
    proxyLogin="user",
    proxyPassword="pass"
)
```

---

## UserAgentPayload

```python
class UserAgentPayload(BaseModel, ABC)
```

Mixin base class that adds an optional `userAgent` field to task payloads.

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `userAgent` | `str \| None` | `None` | Browser User-Agent string used for captcha recognition. |

---

## VanillaTaskPayload

```python
class VanillaTaskPayload(TaskPayload, UserAgentPayload)
```

Forward-compatible base class for custom or newly introduced task types. Allows extra fields via Pydantic's `model_config = {"extra": "allow"}`.

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `type` | `str` | **required** | Task type string (e.g. `"CustomTask"`). |
| `proxy` | `ProxyPayload \| None` | `None` | Optional proxy settings. |

Use this as a base to quickly integrate a new task format not yet supported by the SDK:

```python
from capmonster_python import VanillaTaskPayload

class CustomCaptchaTask(VanillaTaskPayload):
    type: str = "NewCustomTask"
    custom_field: str
```
