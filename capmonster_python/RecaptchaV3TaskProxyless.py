from .CapmonsterClient import CapmonsterClient
from .CapmonsterClient import CapmonsterException


class RecaptchaV3TaskProxyless(CapmonsterClient):
    def __init__(self, client_key, **kwargs):
        super().__init__(client_key=client_key, **kwargs)
        self.solution = "solution"
        self.result_getter = "gRecaptchaResponse"

    def createTask(self, website_url, website_key, minimum_score=0.3, page_action="verify"):
        if not (0.9 >= minimum_score >= 0.1):
            raise CapmonsterException(None, 99, "Minimum score must be between 0.1 and 0.9")
        data = {
            "clientKey": self.client_key,
            "task":
                {
                    "type": "RecaptchaV3TaskProxyless",
                    "websiteURL": website_url,
                    "websiteKey": website_key,
                    "minScore": minimum_score,
                    "pageAction": page_action
                }
        }
        task = self.make_request(method="createTask", data=data)
        self.checkResponse(response=task)
        return task.json().get("taskId")

