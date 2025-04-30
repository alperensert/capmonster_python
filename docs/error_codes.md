# ❗ Error Codes

This page documents common error codes returned by the CapMonster Cloud API along with their meanings and possible
solutions.

---

## 🔐 Authentication & Authorization

### `ERROR_KEY_DOES_NOT_EXIST`

**Invalid API Key**  
The authorization key provided is not recognized or is in the wrong format.  
→ Check your API key from the [CapMonster Dashboard](https://capmonster.cloud/).

### `ERROR_ZERO_BALANCE`

**No Funds**  
Your account balance is zero.  
→ Add credits to continue solving captchas.

### `ERROR_IP_NOT_ALLOWED`

**IP Not Allowed**  
Requests from your current IP address are not allowed.  
→ Add your IP to the **trusted list** in your account settings.

### `ERROR_IP_BANNED`

**IP Banned**  
Too many failed requests with incorrect API key from your IP.  
→ Verify your key, wait a few minutes, and try again.

### `ERROR_IP_BLOCKED`

**Your IP is Blocked**  
Your IP is permanently blocked due to repeated violations or suspicious activity.  
→ Contact CapMonster support.

---

## 🖼️ CAPTCHA File Issues

### `ERROR_TOO_BIG_CAPTCHA_FILESIZE`

**Captcha Image Too Large**  
The image size exceeds 500 KB.  
→ Compress or resize the image before submitting.

### `ERROR_ZERO_CAPTCHA_FILESIZE`

**Captcha Image Too Small**  
The image size is less than 100 bytes.  
→ Ensure the image is valid and properly encoded.

### `ERROR_CAPTCHA_UNSOLVABLE`

**Captcha Unsolvable**  
The image may be too noisy, corrupted, or unsupported by the service.  
→ Try another image or adjust your task.

---

## 🕓 Timing & Task States

### `ERROR_NO_SUCH_CAPCHA_ID` / `WRONG_CAPTCHA_ID`

**Captcha ID Not Found**  
No task found for the given ID, or the request was made after it expired.  
→ Poll results within 5 minutes of task creation.

### `CAPTCHA_NOT_READY`

**Captcha Not Ready**  
The task is still being processed.  
→ Retry after 1–2 seconds.

### `ERROR_RECAPTCHA_TIMEOUT`

**ReCAPTCHA Timeout**  
Task solving took too long, possibly due to slow proxy or server issues.  
→ Use a faster proxy or adjust timeout settings.

---

## 🌐 Domain & SiteKey Errors

### `ERROR_DOMAIN_NOT_ALLOWED`

**Domain Blocked**  
CapMonster Cloud does not support solving captchas for the specified domain.  
→ Use a different domain or provider.

### `ERROR_RECAPTCHA_INVALID_SITEKEY`

**Invalid SiteKey**  
The specified `websiteKey` is not valid.  
→ Double-check the `data-sitekey` on the target page.

### `ERROR_RECAPTCHA_INVALID_DOMAIN`

**Invalid Domain**  
The domain doesn’t match the sitekey's origin.  
→ Ensure both belong to the same origin.

### `ERROR_TOKEN_EXPIRED`

**Token Expired**  
The challenge token has expired.  
→ Create a new task with a fresh token.

---

## 📦 Task Definition Errors

### `ERROR_NO_SUCH_METHOD`

**Incorrect Method**  
The specified task type (in `type`) is invalid or unsupported.

### `ERROR_TASK_NOT_SUPPORTED`

**Incorrect Task Type**  
The task format is not recognized.  
→ Review the `type` value and match it to the correct schema.

### `ERROR_TASK_ABSENT`

**Missing Task Object**  
No `task` object was provided, or the JSON is malformed.

### `ERROR_WRONG_USERAGENT`

**Invalid User-Agent**  
The specified User-Agent string is no longer accepted.  
→ Update to a current, valid browser UA string.

---

## 🌐 Proxy Errors

### `ERROR_PROXY_CONNECT_REFUSED`

**Proxy Connection Failed**  
Unable to reach proxy server.  
→ Test your proxy or replace it.

### `ERROR_PROXY_BANNED`

**Proxy Banned**  
The proxy IP is blocked by the target captcha provider.  
→ Rotate your proxy or try a different provider.

---

## ⚠️ Service Load & Rate Limits

### `ERROR_TOO_MUCH_REQUESTS`

**Too Many Result Polls**  
You polled for the task result too frequently.  
→ Wait at least 2 seconds between requests.

### `ERROR_NO_SLOT_AVAILABLE`

**No Free Servers**  
All recognition servers are currently busy.  
→ Retry after a short delay.

??? warning

    These error codes are related to Capmonster.cloud and not created by us. 

    You can reach the latest version from [here](https://docs.capmonster.cloud/docs/api/api-errors).
