---
icon: book
label: Overview
order: 100
---

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

## What's New

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
