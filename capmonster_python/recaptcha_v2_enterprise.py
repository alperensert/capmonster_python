from typing import Union
from .capmonster import Proxy, UserAgent


class RecaptchaV2EnterpriseTask(UserAgent, Proxy):
    def __init__(self, client_key):
        super(RecaptchaV2EnterpriseTask, self).__init__(client_key)

    def create_task(self, website_url: str, website_key: str,
                    enterprise_payload=None, api_domain: str = None,
                    cookies: Union[dict, list, str] = None,
                    no_cache: bool = None):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "RecaptchaV2EnterpriseTask",
                "websiteURL": website_url,
                "websiteKey": website_key
            }
        }
        data, is_proxy = self._is_proxy_task(data)
        data, is_user_agent = self._add_user_agent(data)
        data = self._add_cookies(cookies, data)
        if enterprise_payload is not None:
            data["task"]["enterprisePayload"] = enterprise_payload
        if api_domain is not None:
            data["task"]["apiDomain"] = api_domain
        if no_cache:
            data["task"]["nocache"] = no_cache
        return self._make_request("createTask", data).get("taskId")
