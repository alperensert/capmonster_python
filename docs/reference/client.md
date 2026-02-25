# CapmonsterClient

The main client for interacting with the Capmonster Cloud API. Supports both synchronous and asynchronous usage, context manager protocol, and configurable polling.

## Constructor

```python
CapmonsterClient(api_key: str, timeout: float = 30.0, max_retries: int = 120, retry_delay: float = 1.0)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | `str` | **required** | Your Capmonster Cloud API key. |
| `timeout` | `float` | `30.0` | HTTP request timeout in seconds. |
| `max_retries` | `int` | `120` | Maximum number of polling attempts in `join_task_result` / `solve`. |
| `retry_delay` | `float` | `1.0` | Delay in seconds between polling attempts. |

## Context Manager

`CapmonsterClient` supports both sync and async context managers to ensure HTTP connections are properly closed.

+++ Sync
```python
with CapmonsterClient(api_key="YOUR_KEY") as client:
    result = client.solve(task)
```
+++ Async
```python
async with CapmonsterClient(api_key="YOUR_KEY") as client:
    result = await client.solve_async(task)
```
+++

---

## Methods

### `get_balance`

Fetches the current account balance.

```python
def get_balance(self) -> float
async def get_balance_async(self) -> float
```

**Returns:** `float` — The account balance. Defaults to `0.0` if not found.

---

### `create_task`

Creates a captcha-solving task and returns the task ID.

```python
def create_task(self, task: TaskPayload, callback_url: str | None = None) -> int
async def create_task_async(self, task: TaskPayload, callback_url: str | None = None) -> int
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `task` | `TaskPayload` | **required** | The task configuration payload. |
| `callback_url` | `str \| None` | `None` | Optional URL to be called on task completion. |

**Returns:** `int` — The unique task identifier.

**Raises:** `CapmonsterException` if the request fails or the response contains no valid task ID.

---

### `get_task_result`

Fetches the result of a completed task (single poll, no waiting).

```python
def get_task_result(self, task_id: int) -> dict
async def get_task_result_async(self, task_id: int) -> dict
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `task_id` | `int` | The task identifier returned by `create_task`. |

**Returns:** `dict` — The solution dictionary, or `{}` if the task is not yet ready.

---

### `join_task_result`

Polls for the task result until it is ready, up to `max_retries` attempts with `retry_delay` between each.

```python
def join_task_result(self, task_id: int) -> dict
async def join_task_result_async(self, task_id: int) -> dict
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `task_id` | `int` | The task identifier returned by `create_task`. |

**Returns:** `dict` — The solution dictionary from the completed task.

**Raises:** `CapmonsterAPIException` with code `ERROR_MAXIMUM_TIME_EXCEED` if polling exhausts all retries.

---

### `solve`

Convenience method that creates a task and polls for its result in one call. Equivalent to `create_task()` followed by `join_task_result()`.

```python
def solve(self, task: TaskPayload, callback_url: str | None = None) -> dict
async def solve_async(self, task: TaskPayload, callback_url: str | None = None) -> dict
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `task` | `TaskPayload` | **required** | The task configuration payload. |
| `callback_url` | `str \| None` | `None` | Optional callback URL for task completion. |

**Returns:** `dict` — The solution dictionary from the completed task.
