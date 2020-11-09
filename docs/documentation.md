## ImageToTextTask
- client_key: Your unique key for solving captchas.

##### function: **createTask**(file_path, module)
> file_path: your text-captcha image's path. \
> module: default is None, you can select from below \
> return value: taskId (as string)
- botdetect
- facebook
- hotmail
- mailru
- solvemedia
- steam
- vk
- yandex
- yandexnew
- yandexwave
- universal (all other text captcha types)

##### function: **getTaskResult**(taskId)
> taskId: the task's id returning from createTask function. \
> return value: if result is ready: resultText. if is not ready: False

##### function: **joinTaskResult**(taskId, maximum_time)
> taskId: the task's id returning from createTask function. \
> maximum_time: time to wait for captcha result. default: 150 (seconds) \
> return value: if result is ready: resultText. if result waiting more than maximum_time: raise CapmonsterException

## NoCaptchaTask
- client_key: Your unique key for solving captchas.
- user_agent: Browser user agent, default is Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.132 Safari/537.36

##### function: **createTask**(website_url, website_key, proxyAddress, proxyPort, proxyLogin, proxyPassword, proxyType)
> website_url: the website url where the recaptcha is located. \
> website_key: the website's recaptcha public key. etc. `<div class="g-recaptcha" data-sitekey="THAT_ONE"></div>` \
> proxyPort: example: 8080 (integer) \
> proxyLogin: Login for proxy which requires authorizaiton (basic) \
> proxyPassword: Proxy password \
> proxyType: http or https \
> proxyAddress: Proxy IP address IPv4/IPv6. Not allowed to use:
> - host names instead of IPs
> - transparent proxies (where client IP is visible)
> - proxies from local networks

##### function: **getTaskResult**(taskId)
> taskId: the task's id returning from createTask function. \
> return value: if result is ready: gRecaptchaResponse. if is not ready: False

##### function: **joinTaskResult**(taskId, maximum_time)
> taskId: the task's id returning from createTask function. \
> maximum_time: time to wait for captcha result. default: 150 (seconds) \
> return value: if result is ready: gRecaptchaResponse. if result waiting more than maximum_time: raise CapmonsterException

## NoCaptchaTaskProxyless
- client_key: Your unique key for solving captchas.
- user_agent: Browser user agent, default is Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.132 Safari/537.36

##### function: **createTask**(website_url, website_key)
> website_url: the website url where the recaptcha is located. \
> website_key: the website's recaptcha public key. etc. `<div class="g-recaptcha" data-sitekey="THAT_ONE"></div>` \

##### function: **getTaskResult**(taskId)
> taskId: the task's id returning from createTask function. \
> return value: if result is ready: gRecaptchaResponse. if is not ready: False

##### function: **joinTaskResult**(taskId, maximum_time)
> taskId: the task's id returning from createTask function. \
> maximum_time: time to wait for captcha result. default: 150 (seconds) \
> return value: if result is ready: gRecaptchaResponse. if result waiting more than maximum_time: raise CapmonsterException

## RecaptchaV3TaskProxyless
- client_key: Your unique key for solving captchas.

##### function: **createTask**(website_url, website_key, minimum_score, page_action)
> website_url: the website url where the recaptcha is located. \
> website_key: the website's recaptcha public key. etc. `<div class="g-recaptcha" data-sitekey="THAT_ONE"></div>` \
> minimum_score: an integer value between 0.1 and 0.9 \
> page_action: Widget action value. Website owner defines what user is doing on the page through this parameter. Default value: verify

##### function: **getTaskResult**(taskId)
> taskId: the task's id returning from createTask function. \
> return value: if result is ready: gRecaptchaResponse. if is not ready: False

##### function: **joinTaskResult**(taskId, maximum_time)
> taskId: the task's id returning from createTask function. \
> maximum_time: time to wait for captcha result. default: 150 (seconds) \
> return value: if result is ready: gRecaptchaResponse. if result waiting more than maximum_time: raise CapmonsterException

## FunCaptchaTaskProxyless
- client_key: Your unique key for solving captchas.

##### function: **createTask**(website_url, website_key, js_subdomain, data_blob)
> website_url: the website url where the funcaptcha is located. \
> website_key: the website's funcaptcha public key. etc. `<div id="funcaptcha" data-pkey="THAT_ONE"></div>` \
> js_subdomain: A special subdomain of funcaptcha.com, from which the JS captcha widget should be loaded. Most FunCaptcha installations work from shared domains, so this option is only needed in certain rare cases. \
> data_blob: Additional parameter that may be required by FunCaptcha implementation. See capmonster.cloud documentation for more information.

##### function: **getTaskResult**(taskId)
> taskId: the task's id returning from createTask function. \
> return value: if result is ready: token. if is not ready: False

##### function: **joinTaskResult**(taskId, maximum_time)
> taskId: the task's id returning from createTask function. \
> maximum_time: time to wait for captcha result. default: 150 (seconds) \
> return value: if result is ready: token. if result waiting more than maximum_time: raise CapmonsterException

## FunCaptchaTask
- client_key: Your unique key for solving captchas.

##### function: **createTask**(website_url, website_key, js_subdomain, data_blob)
> website_url: the website url where the funcaptcha is located. \
> website_key: the website's funcaptcha public key. etc. `<div id="funcaptcha" data-pkey="THAT_ONE"></div>` \
> js_subdomain: A special subdomain of funcaptcha.com, from which the JS captcha widget should be loaded. Most FunCaptcha installations work from shared domains, so this option is only needed in certain rare cases. \
> data_blob: Additional parameter that may be required by FunCaptcha implementation. See capmonster.cloud documentation for more information. \
> proxyPort: example: 8080 (integer) \
> proxyLogin: Login for proxy which requires authorizaiton (basic) \
> proxyPassword: Proxy password \
> proxyType: http, https, socks4 or socks5 \
> proxyAddress: Proxy IP address IPv4/IPv6. Not allowed to use:
> - host names instead of IPs
> - transparent proxies (where client IP is visible)
> - proxies from local networks

##### function: **getTaskResult**(taskId)
> taskId: the task's id returning from createTask function. \
> return value: if result is ready: token. if is not ready: False

##### function: **joinTaskResult**(taskId, maximum_time)
> taskId: the task's id returning from createTask function. \
> maximum_time: time to wait for captcha result. default: 150 (seconds) \
> return value: if result is ready: token. if result waiting more than maximum_time: raise CapmonsterException

#### Globals
##### function: **getBalance**()
> return value:  
>
## Examples
Examples are located in [here](https://github.com/alperensert/python_capmonster/blob/master/README.md). If you have issue with anything, feel free to create an issue or [e-mail me](mailto:alperenssrt@gmail.com)

## Exceptions
| Code | Description |
|------|-------------|
|ERROR_KEY_DOES_NOT_EXIST|Account authorization key not found in the system or has incorrect format (length is not)|
|ERROR_ZERO_CAPTCHA_FILESIZE|The size of the captcha you are uploading is less than 100 bytes.|
|ERROR_TOO_BIG_CAPTCHA_FILESIZE|The size of the captcha you are uploading is more than 50,000 bytes.|
|ERROR_ZERO_BALANCE|Account has zero balance|
|ERROR_IP_NOT_ALLOWED|Request with current account key is not allowed from your IP|
|ERROR_CAPTCHA_UNSOLVABLE|This type of captchas is not supported by the service or the image does not contain an answer, perhaps it is too noisy. It could also mean that the image is corrupted or was incorrectly rendered.|
|ERROR_NO_SUCH_CAPCHA_ID, WRONG_CAPTCHA_ID|The captcha that you are requesting was not found. Make sure you are requesting a status update only within 5 minutes of uploading.|
|CAPTCHA_NOT_READY|The captcha has not yet been solved|
|ERROR_IP_BANNED|You have exceeded the limit of requests with the wrong api key, check the correctness of your api key in the control panel and after some time, try again|
|ERROR_NO_SUCH_METHOD|This method is not supported or empty|