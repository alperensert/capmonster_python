from .capmonster import Capmonster, CapmonsterException
from base64 import b64encode


class ImageToTextTask(Capmonster):
    def __init__(self, client_key):
        super().__init__(client_key)

    def create_task(self, image_path: str = None, base64_encoded_image: str = None, module: str = None,
                    recognizing_threshold: int = None, case: bool = None, numeric: int = None,
                    math: bool = None):
        if base64_encoded_image is None and image_path is None:
            raise CapmonsterException(error_id=-1,
                                      error_code="ERROR_NOTHING_GIVEN",
                                      error_description="You have to give image_path or base64_encoded_image")
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "ImageToTextTask"
            }
        }
        if base64_encoded_image is None:
            img_body = self._from_path(image_path)
            data["task"]["body"] = img_body
        else:
            data["task"]["body"] = base64_encoded_image
        if module is not None:
            data["task"]["СapMonsterModule"] = module
        if recognizing_threshold is not None and (0 <= recognizing_threshold <= 100):
            data["task"]["recognizingThreshold"] = recognizing_threshold
        if case is not None:
            data["task"]["Case"] = case
        if numeric is not None and (0 <= numeric <= 1):
            data["task"]["numeric"] = numeric
        if math is not None:
            data["task"]["math"] = math
        return self._make_request("createTask", data).get("taskId")

    @staticmethod
    def _from_path(image_path: str):
        with open(image_path, "rb") as img:
            base64_img = b64encode(img.read()).decode("ascii")
        return base64_img
