Capmonster.cloud for Python
=
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/capmonster_python?style=flat) ![GitHub last commit](https://img.shields.io/github/last-commit/alperensert/capmonster_python?style=flat) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/alperensert/capmonster_python?style=flat) ![PyPI - Downloads](https://img.shields.io/pypi/dm/capmonster_python?style=flat) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/alperensert/capmonster_python?style=flat) ![GitHub Repo stars](https://img.shields.io/github/stars/alperensert/capmonster_python?style=social)

[Capmonster.cloud](https://capmonster.cloud) package for Python3

If you have any problem with usage, [read the documentation](https://github.com/alperensert/capmonster_python/wiki), [create an issue](https://github.com/alperensert/capmonster_python/issues/new) or [join the community](https://discord.gg/33HwSqb5su)

*At least 2x cheaper, up to 30x faster than manual recognition services.*

### Installation
```
pip install capmonster_python
```

### Supported captcha types
- Image to text
- Recaptcha v2
- Recaptcha v3
- Fun Captcha
- HCaptcha

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

For other examples and api documentation please visit [wiki](https://github.com/alperensert/capmonster_python/wiki)

### Migration from 1.3.2 to 2.x
- v2.x is created for automation and stability.
- If you want to use old version: (no longer supported)
    ```
    pip install capmonster-python==1.3.2
    ```
- If you want to use new version 2.x:
  - All methods, classes and fields are changed for maximum optimization and continuous automation.
    Check out [wiki](https://github.com/alperensert/capmonster_python/wiki) for usage examples and package api.