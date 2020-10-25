from .CapmonsterClient import CapmonsterClient
from .exceptions import CapmonsterException
import time


class NoCaptchaTask(CapmonsterClient):
    def __init__(self, client_key, user_agent=False):
        super().__init__(client_key=client_key)
        if user_agent: self.user_agent = user_agent
        else: self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.132 Safari/537.36"

    def createTask(self, website_url, website_key, proxyAddress, proxyPort, proxyLogin, proxyPassword, proxyType="https"):
        data = {
            "clientKey": self.client_key,
            "task":
            {
                "type": "NoCaptchaTaskProxyless",
                "websiteURL": website_url,
                "websiteKey": website_key,
                "proxyType": proxyType,
                "proxyAddress": proxyAddress,
                "proxyPort": proxyPort,
                "proxyLogin": proxyLogin,
                "proxyPassword": proxyPassword,
                "userAgent": self.user_agent
            }
        }
        task = self.make_request(method="createTask", data=data)
        self.checkResponse(response=task)
        return task["taskId"]

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
