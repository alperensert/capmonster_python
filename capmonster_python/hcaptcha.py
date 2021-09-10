from .capmonster import Proxy, UserAgent
from .utils import CapmonsterException
from typing import Union


class HCaptchaTask(UserAgent, Proxy):
    def __init__(self, client_key):
        super(HCaptchaTask, self).__init__(client_key)

    def create_task(self, website_url: str, website_key: str, is_invisible: bool = None, custom_data: str = None,
                    cookies: Union[dict, list, str] = None):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "HCaptchaTask",
                "websiteURL": website_url,
                "websiteKey": website_key
            }
        }
        if cookies is not None:
            data = self._add_cookies(cookies, data)
        if is_invisible is not None:
            data["task"]["isInvisible"] = is_invisible
        if custom_data is not None:
            data, is_user_agent = self._add_user_agent(data)
            if is_user_agent is False:
                raise CapmonsterException(-1,
                                          "USER_AGENT_ERROR",
                                          "You must provide an user agent if you submit captcha with custom_data")
            data["task"]["data"] = custom_data
        if custom_data is None:
            data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        return self._make_request("createTask", data).get("taskId")
