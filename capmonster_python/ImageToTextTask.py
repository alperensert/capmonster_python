from .CapmonsterClient import CapmonsterClient
from .exceptions import CapmonsterException
from base64 import b64encode
import time


class ImageToTextTask(CapmonsterClient):
    def __init__(self, client_key):
        super().__init__(client_key=client_key)

    def createTask(self, file_path=None, base64_image: bytes = None, module=None):
        if file_path is None and base64_image is None:
            return False
        elif file_path is not None:
            image = open(file_path, "rb")
            img_base64 = b64encode(image.read()).decode("ascii")
        elif base64_image is not None:
            img_base64 = base64_image
        else:
            return False
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
        return task.json().get("taskId")

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
            return task_result.get("solution").get("text")
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
                return task_result.get("solution").get("text")
            elif i >= maximum_time:
                raise CapmonsterException(None, 61, "Maximum time is exceed.")
            elif task_result.get("solution") is not None:
                i += 1
                time.sleep(2)
                continue
