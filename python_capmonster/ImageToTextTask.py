from .CapmonsterClient import CapmonsterClient
from .exceptions import CapmonsterException
from base64 import b64encode
import time


class ImageToTextTask(CapmonsterClient):
    def __init__(self, client_key):
        super().__init__(client_key=client_key)

    def createTask(self, file_path, module=None):
        image = open(file_path, "rb")
        img_base64 = b64encode(image.read()).decode("ascii")
        data = {
            "clientKey": self.client_key,
            "task":
            {
                "type": "ImageToTextTask",
                "body": img_base64
            }
        }
        if module is not None: data["task"]["СapMonsterModule"] = module
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
            return task_result.get("solution").get("text")
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
                return task_result.get("solution").get("text")
            elif task_result.get("solution") is not None:
                i += 1
                time.sleep(1)
                continue
            elif i >= maximum_time:
                raise CapmonsterException(None, 61, "Maximum time is exceed.")
