from .capmonster import Capmonster


class RecaptchaV3Task(Capmonster):
    def __init__(self, client_key):
        super().__init__(client_key)

    def create_task(self, website_url: str, website_key: str, minimum_score: float = 0.3, page_action: str = None):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "RecaptchaV3TaskProxyless",
                "websiteURL": website_url,
                "websiteKey": website_key
            }
        }
        if 0.1 <= minimum_score <= 0.9:
            data["task"]["minScore"] = minimum_score
        if page_action is not None:
            data["task"]["pageAction"] = page_action
        return self._make_request("createTask", data).get("taskId")
