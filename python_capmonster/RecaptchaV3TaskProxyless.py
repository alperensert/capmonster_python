from .CapmonsterClient import CapmonsterClient
from .exceptions import CapmonsterException
import time


class RecaptchaV3TaskProxyless(CapmonsterClient):
    def __init__(self, client_key):
        super().__init__(client_key=client_key)

    def createTask(self, website_url, website_key, minimum_score=0.3, page_action="verify"):
        if not (0.9 >= minimum_score >= 0.1): raise CapmonsterException(None, 99, "Minimum score must be between 0.1 and 0.9")
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
        return task.get("taskId")

    def getTaskResult(self, taskId):
        data = {
            "clientKey": self.client_key,
            "taskId": taskId
        }
        task_result = self.make_request(method="getTaskResult", data=data)
        self.checkResponse(response=task_result)
        is_ready = self.checkReady(response=task_result)
        if is_ready:
            return task_result.get("solution").get("gRecaptchaResponse")
        else:
            return False

    def joinTaskResult(self, taskId, maximum_time=150):
        data = {
            "clientKey": self.client_key,
            "taskId": taskId
        }
        i = 0
        while True:
            task_result = self.make_request(method="getTaskResult", data=data)
            self.checkResponse(response=task_result)
            is_ready = self.checkReady(response=task_result)
            if is_ready and task_result.get("solution") is not None:
                return task_result.get("solution").get("gRecaptchaResponse")
            elif task_result.get("solution") is not None:
                i += 1
                time.sleep(1)
                continue
            elif i >= maximum_time:
                raise CapmonsterException(None, 61, "Maximum time is exceed.")