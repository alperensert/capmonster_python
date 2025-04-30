# 📘 API Reference

Welcome to the **Capmonster Python** API reference.

This section provides detailed documentation for all available task types and core classes in the Capmonster ecosystem.
Whether you're solving reCAPTCHA, Turnstile, or advanced behavioral CAPTCHAs like DataDome or Imperva, this reference
will guide you through the available models, parameters, and behaviors.

---

## Overview

Capmonster Python v4 is fully typed with [Pydantic](https://docs.pydantic.dev/) and exposes task models via clear class
structures. All classes include:

- ✅ Type-annotated attributes
- 🧩 Google-style docstrings
- 🛠 `to_request()` methods for raw dict generation
- 🔁 Sync/Async-ready usage with `CapmonsterClient`

---

## Usage Notes

- All tasks are **instantiable Pydantic models**
- If you are solving proxy-based CAPTCHAs, configure `proxy` and `userAgent` attributes
- Task classes **do not make API calls** — use them with `CapmonsterClient`

---
