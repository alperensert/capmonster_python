# Exceptions

All exceptions in capmonster_python inherit from `CapmonsterException`.

---

## CapmonsterException

```python
class CapmonsterException(Exception)
```

Generic base exception for all errors. Raised for errors not caught by more specific exception classes, including HTTP request failures and unexpected issues.

---

## CapmonsterAPIException

```python
class CapmonsterAPIException(CapmonsterException)
```

Raised when the Capmonster Cloud API returns an error response.

| Attribute | Type | Description |
|-----------|------|-------------|
| `error_id` | `int` | The numeric error ID returned by the API. |
| `error_code` | `str` | The error code string (e.g. `"ERROR_KEY_DOES_NOT_EXIST"`). |
| `error_description` | `str` | Human-readable error description from the API. |

### Constructor

```python
CapmonsterAPIException(error_id, error_code, error_description)
```

### String representation

```
[ERROR_CODE] Error description
```

---

## CapmonsterValidationException

```python
class CapmonsterValidationException(CapmonsterException)
```

Raised when a task configuration is invalid at the SDK level (before any API call is made).

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | `str` | **required** | Description of the validation error. |
| `field` | `str \| None` | `None` | The field that caused the error, if applicable. |
| `task` | `str \| None` | `None` | The task type that caused the error, if applicable. |

### Constructor

```python
CapmonsterValidationException(message: str, *, field: str = None, task: str = None)
```

### String representation

```
[CapmonsterValidationError] message (field: fieldName) [task: TaskType]
```
