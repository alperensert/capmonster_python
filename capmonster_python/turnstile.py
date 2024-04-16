from .capmonster import Proxy, UserAgent
from typing import Union


class TurnstileTask(UserAgent, Proxy):
    def __init__(self, client_key):
        super(TurnstileTask, self).__init__(client_key)

    def create_task(self, website_url: str, website_key: str,
                    no_cache: bool = None):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "TurnstileTask",
                "websiteURL": website_url,
                "websiteKey": website_key
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        if no_cache:
            data["task"]["nocache"] = no_cache
        return self._make_request("createTask", data).get("taskId")
