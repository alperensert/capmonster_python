from .CapmonsterClient import CapmonsterClient
from base64 import b64encode


class ImageToTextTask(CapmonsterClient):
    def __init__(self, client_key):
        super().__init__(client_key=client_key)
        self.solution = "solution"
        self.result_getter = "text"

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
        if module is not None:
            data["task"]["СapMonsterModule"] = module
        task = self.make_request(method="createTask", data=data)
        self.checkResponse(response=task)
        return task.json().get("taskId")
