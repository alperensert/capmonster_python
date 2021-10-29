from .capmonster import Proxy, UserAgent


class GeeTestTask(UserAgent, Proxy):
    def __init__(self, client_key):
        super(GeeTestTask, self).__init__(client_key)

    def create_task(self, website_url: str, gt: str, challenge: str,
                    api_server_subdomain: str = None, get_lib: str = None):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "GeeTestTask",
                "websiteURL": website_url,
                "gt": gt,
                "challenge": challenge
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        if api_server_subdomain:
            data["task"]["geetestApiServerSubdomain"] = api_server_subdomain
        if get_lib:
            data["task"]["geetestGetLib"] = get_lib
        return self._make_request("createTask", data).get("taskId")

