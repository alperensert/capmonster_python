from .capmonster import Proxy, UserAgent
from typing import Union


class FuncaptchaTask(UserAgent, Proxy):
    def __init__(self, client_key):
        super(FuncaptchaTask, self).__init__(client_key)

    def create_task(self, website_url: str, website_public_key: str, api_js_subdomain: str = None,
                    data_blob: str = None, cookies: Union[dict, list, str] = None):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "FunCaptchaTask",
                "websiteURL": website_url,
                "websitePublicKey": website_public_key
            }
        }
        if data_blob is not None:
            data["task"]["data"] = data_blob
        data, is_proxy = self._is_proxy_task(data)
        if is_proxy:
            data, is_user_agent = self._add_user_agent(data)
            if cookies is not None:
                data = self._add_cookies(cookies, data)
        if api_js_subdomain is not None:
            data["task"]["funcaptchaApiJSSubdomain"] = api_js_subdomain
        return self._make_request("createTask", data).get("taskId")
