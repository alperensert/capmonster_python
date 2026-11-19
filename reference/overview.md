# API Reference

Welcome to the **Capmonster Python** API reference.

This section provides detailed documentation for all available task types and core classes in the Capmonster ecosystem.
Whether you're solving reCAPTCHA, Turnstile, or advanced behavioral CAPTCHAs like DataDome or Imperva, this reference
will guide you through the available models, parameters, and behaviors.

---

## Overview

Capmonster Python v4 is fully typed with [Pydantic](https://docs.pydantic.dev/) and exposes task models via clear class
structures. All classes include:

- Type-annotated attributes
- Google-style docstrings
- `to_request()` methods for raw dict generation
- Sync/Async-ready usage with `CapmonsterClient`

---

## What's New in 5.1

- **6 new task types** — Alibaba, Friendly Captcha, FengkongCloud, ARCaptcha, HeyTap, Proton
- **Task cost** — `solve_detailed()` and the other `*_detailed` methods return a `TaskResult` with the task's `cost`
- **New fields** — `minScore` for reCAPTCHA v2 Enterprise, TenDI `metadata`, DataDome `datadomeVersion`, Turnstile `pageData`, image recognition `taskArgument` and new tasks
- **Fixes** — `HuntTask` uses the current `CustomTask`/`HUNT` request; Imperva sends `incapsulaCookies`; image recognition adds `bls_3x3` with `taskArgument`
- **Deprecated** (warning now, removed in 6.0) — `RecaptchaClickTask`, `TemuTask`, `CastleTask`, `HuntTask(websiteKey=...)`, `ImpervaTaskMetadata(incapsulaCookie=...)`, `ComplexImageRecognitionTask(task="bls")`

## What's New in 5.0

- **Context manager** — use `with` / `async with` to auto-close HTTP connections
- **`solve()` / `solve_async()`** — convenience method combining `create_task` + `join_task_result`
- **Configurable polling** — set `max_retries` and `retry_delay` on `CapmonsterClient`
- **9 new task types** — FunCaptcha, Amazon WAF, reCAPTCHA v3 Enterprise, Cloudflare Waiting Room, MTCaptcha, Yidun, Altcha, Castle, TSPD

---

## Usage Notes

- All tasks are **instantiable Pydantic models**
- If you are solving proxy-based CAPTCHAs, configure `proxy` and `userAgent` attributes
- Task classes **do not make API calls** — use them with `CapmonsterClient`

---
