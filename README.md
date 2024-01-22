Capmonster.cloud for Python
=
![PyPI - Wheel](https://img.shields.io/pypi/wheel/capmonster-python?style=plastic) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/capmonster_python?style=flat) ![GitHub last commit](https://img.shields.io/github/last-commit/alperensert/capmonster_python?style=flat) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/alperensert/capmonster_python?style=flat) ![PyPI - Downloads](https://img.shields.io/pypi/dm/capmonster_python?style=flat) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alperensert/capmonster_python?style=flat) ![GitHub Repo stars](https://img.shields.io/github/stars/alperensert/capmonster_python?style=social)

[Capmonster.cloud](https://capmonster.cloud) package for Python3

If you have any problem with usage, [read the documentation](https://alperensert.github.io/capmonster_python)
or [create an issue](https://github.com/alperensert/capmonster_python/issues/new)

*At least 2x cheaper, up to 30x faster than manual recognition services.*

### Installation

```
pip install capmonster_python
```

### Supported captcha types

- Image to text
- Recaptcha v2
- Recaptcha v2 Enterprise
- Recaptcha v3
- Fun Captcha
- HCaptcha
- GeeTest
- Turnstile Task
- Data Dome

Usage examples
-

#### ImageToText

```python
from capmonster_python import ImageToTextTask

capmonster = ImageToTextTask("API_KEY")
task_id = capmonster.create_task(image_path="img.png")
result = capmonster.join_task_result(task_id)
print(result.get("text"))
```

#### Recaptcha v2

```python
from capmonster_python import RecaptchaV2Task

capmonster = RecaptchaV2Task("API_KEY")
task_id = capmonster.create_task("website_url", "website_key")
result = capmonster.join_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```

#### Recaptcha v2 enterprise

```python
from capmonster_python import RecaptchaV2EnterpriseTask

capmonster = RecaptchaV2EnterpriseTask("API_KEY")
task_id = capmonster.create_task("website_url", "website_key", {"s": "payload value"}, "api_domain")
result = capmonster.join_task_result(task_id)
print(result.get("gRecaptchaResponse"))
```

#### GeeTest

```python
from capmonster_python import GeeTestTask

capmonster = GeeTestTask("API_KEY")
task_id = capmonster.create_task("website_url", "gt", "challenge")
result = capmonster.join_task_result(task_id)
print(result.get("challenge"))
print(result.get("seccode"))
print(result.get("validate"))
```

#### Report incorrect captchas

```python
from capmonster_python import RecaptchaV2Task

capmonster = RecaptchaV2Task("API_KEY")
task_id = capmonster.create_task("website_url", "website_key")
result = capmonster.join_task_result(task_id)
report_result = capmonster.report_incorrect_captcha("token", task_id)
print(report_result)
```

For other examples and api documentation please visit [wiki](https://alperensert.github.io/capmonster_python)