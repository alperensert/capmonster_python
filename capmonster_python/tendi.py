from .capmonster import UserAgent

class TenDITask(UserAgent):
    def __init__(self, client_key):
        super(TenDITask, self).__init__(client_key)

    def create_task(self, website_url: str, website_key: str):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "CustomTask",
                "class": "TenDI",
                "websiteURL": website_url,
                "websiteKey": website_key
            }
        }

        data, is_user_agent = self._add_user_agent(data)
        return self._make_request("createTask", data).get("taskId")
