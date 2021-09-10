from .capmonster import Proxy, UserAgent
from typing import Union


class RecaptchaV2Task(UserAgent, Proxy):
    def __init__(self, client_key):
        super(RecaptchaV2Task, self).__init__(client_key)

    def create_task(self, website_url: str, website_key: str,
                    cookies: Union[dict, list, str] = None, recaptcha_s_value: str = None,
                    no_cache: bool = None):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "NoCaptchaTask",
                "websiteURL": website_url,
                "websiteKey": website_key
            }
        }
        data, is_proxy = self._is_proxy_task(data)
        data, is_user_agent = self._add_user_agent(data)
        data = self._add_cookies(cookies, data)
        if recaptcha_s_value is not None:
            data["task"]["recaptchaDataSValue"] = recaptcha_s_value
        if no_cache is not None and no_cache is not False:
            data["task"]["nocache"] = no_cache
        return self._make_request("createTask", data).get("taskId")
