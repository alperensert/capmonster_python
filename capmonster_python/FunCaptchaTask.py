from .CapmonsterClient import CapmonsterClient
from .exceptions import CapmonsterException
import time


class FunCaptchaTask(CapmonsterClient):
    def __init__(self, client_key, **kwargs):
        super().__init__(client_key=client_key, **kwargs)
        self.userAgent = kwargs.get("userAgent")

    def createTask(self, website_url, website_public_key, proxyAddress, proxyPort: int, proxyLogin, proxyPassword, proxyType="https", js_subdomain=None, data_blob=None):
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "FunCaptchaTaskProxyless",
                "websiteURL": website_url,
                "websitePublicKey": website_public_key,
                "proxyType": proxyType,
                "proxyAddress": proxyAddress,
                "proxyPort": proxyPort,
                "proxyLogin": proxyLogin,
                "proxyPassword": proxyPassword,
                "userAgent": self.userAgent
            }
        }
        if js_subdomain is not None: data["task"]["funcaptchaApiJSSubdomain"] = js_subdomain
        if data_blob is not None: data["task"]["data"] = data_blob
        task = self.make_request(method="createTask", data=data)
        self.checkResponse(response=task)
        return task.json()["taskId"]

    def getTaskResult(self, taskId):
        data = {
            "clientKey": self.client_key,
            "taskId": taskId
        }
        task_result = self.make_request(method="getTaskResult", data=data)
        self.checkResponse(response=task_result)
        is_ready = self.checkReady(response=task_result)
        task_result = task_result.json()
        if is_ready:
            return task_result.get("solution").get("token")
        else:
            return False

    def joinTaskResult(self, taskId, maximum_time=120):
        data = {
            "clientKey": self.client_key,
            "taskId": taskId
        }
        i = 0
        while True:
            task_result = self.make_request(method="getTaskResult", data=data)
            self.checkResponse(response=task_result)
            is_ready = self.checkReady(response=task_result)
            task_result = task_result.json()
            if is_ready and task_result.get("solution") is not None:
                return task_result.get("solution").get("token")
            elif i >= maximum_time:
                raise CapmonsterException(None, 61, "Maximum time is exceed.")
            elif task_result.get("solution") is not None:
                i += 1
                time.sleep(2)
                continue
