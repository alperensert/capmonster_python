from .exceptions import CapmonsterException
from .CapmonsterClient import CapmonsterClient
import time


class HCaptchaTaskProxyless(CapmonsterClient):
    def __init__(self, client_key, **kwargs):
        super().__init__(client_key=client_key, **kwargs)
        self.userAgent = kwargs.get("userAgent")

    def createTask(self, website_url, website_key, cookies=None):
        data = {
            "clientKey": self.client_key,
            "task":
                {
                    "type": "HCaptchaTaskProxyless",
                    "websiteURL": website_url,
                    "websiteKey": website_key,
                    "userAgent": self.userAgent
                }
        }
        if cookies is not None and type(cookies) == dict or type(cookies) == list:
            add_cookies = ""
            if type(cookies) == dict:
                for key, value in cookies.items():
                    if value == list(cookies.items())[-1][1]:
                        add_cookies += "{}={}".format(key, value)
                    else:
                        add_cookies += "{}={};".format(key, value)
            elif type(cookies) == list:
                for i in cookies:
                    if not len(cookies) % 2 == 0:
                        raise AttributeError("List cookies length must be even numbers")
                    if cookies.index(i) % 2 == 0:
                        add_cookies += "{}=".format(i)
                    elif cookies[cookies.index(i)] == cookies[-1]:
                        add_cookies += "{}".format(i)
                    elif cookies.index(i) % 2 == 1:
                        add_cookies += "{};".format(i)
            data["task"]["cookies"] = add_cookies
            del add_cookies
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
        task_result = task_result.json()
        is_ready = self.checkReady(response=task_result)
        if is_ready:
            return task_result.get("solution").get("gRecaptchaResponse")
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
                return task_result.get("solution").get("gRecaptchaResponse")
            elif i >= maximum_time:
                raise CapmonsterException(None, 61, "Maximum time is exceed.")
            elif task_result.get("solution") is not None:
                i += 1
                time.sleep(2)
                continue
