# Image-Based

---

## ImageToTextTask

Solves image-based captchas by recognizing text from a base64-encoded image.

**API type:** `ImageToTextTask`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `body` | `str` | **required** | Base64-encoded image body. Must be without line breaks. |
| `capMonsterModule` | `str \| None` | `None` | Recognition module name (e.g. `"yandex"`). |
| `recognizingThreshold` | `int \| None` | `None` | Confidence threshold (0–100). You won't be charged if confidence is below this value. |
| `case` | `bool \| None` | `None` | Set to `True` if the captcha is case-sensitive. |
| `numeric` | `Literal[0, 1] \| None` | `None` | Set to `1` if the captcha contains only numbers. |
| `math` | `bool \| None` | `None` | Set to `True` if the captcha requires a math operation. |

---

## ComplexImageRecaptchaTask

Solves complex image-based reCAPTCHA challenges (grid selection tasks).

**API type:** `ComplexImageTask` (with `class: "recaptcha"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `imageUrls` | `list[str] \| None` | `None` | List of image URLs for the captcha parts. |
| `imagesBase64` | `list[str] \| None` | `None` | List of base64-encoded images for the captcha parts. |
| `metadata` | `ComplexImageRecaptchaMetadata` | **required** | Metadata describing the task. |

!!!warning
Exactly one of `imageUrls` or `imagesBase64` must be provided (not both, not neither).
!!!

### ComplexImageRecaptchaMetadata

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `Task` | `str \| None` | `None` | Textual task description (e.g. `"Click on traffic lights"`). |
| `TaskDefinition` | `str \| None` | `None` | Technical task type identifier. |
| `Grid` | `Literal["4x4", "3x3", "1x1"]` | **required** | Grid size of the captcha. |

Exactly one of `Task` or `TaskDefinition` must be set.

---

## ComplexImageRecognitionTask

Solves complex image recognition tasks (rotate, match, etc.).

**API type:** `ComplexImageTask` (with `class: "recognition"`)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `imagesBase64` | `list[str]` | **required** | List of base64-encoded images. |
| `task` | `Literal["oocl_rotate_new", "oocl_rotate_double_new", "betpunch_3x3_rotate", "bls", "shein"]` | **required** | Type of recognition task. |
