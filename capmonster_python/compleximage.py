from .capmonster import UserAgent


class ComplexImageTask(UserAgent):
    def __init__(self, client_key):
        super(ComplexImageTask, self).__init__(client_key)

    def create_task(self, _class: str, grid: str = None,
                    task_definition: str = None,
                    image_urls: list = None,
                    images_base64: list = None,
                    task: str = None,
                    websiteUrl: str = None):
        if _class != "recaptcha" or _class != "hcaptcha":
            raise ValueError("Currently only recaptcha or hcaptcha is supported as _class value.")
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "ComplexImageTask",
                "class": _class,
                "metadata": {}
            }
        }
        if image_urls is not None:
            data["task"]["imageUrls"] = image_urls
        elif images_base64 is not None:
            data["task"]["imagesBase64"] = images_base64
        else:
            raise ValueError("image_urls or images_base64 must be sent")
        if _class == "recaptcha":
            if grid is None:
                raise ValueError("Grid parameter must sent with recaptcha")
            else:
                data["task"]["metadata"]["Grid"] = grid
            if task is not None:
                data["task"]["metadata"]["Task"] = task
            elif task_definition is not None:
                data["task"]["metadata"]["TaskDefinition"] = task_definition
            else:
                raise ValueError("task_definition or task parameter must be sent")
        elif _class == "hcaptcha":
            if task is not None:
                data["task"]["metadata"]["Task"] = task
            else:
                raise ValueError("task parameter must be sent with hcaptcha")
        if websiteUrl is not None:
            data["task"]["websiteUrl"] = websiteUrl
        data, is_user_agent = self._add_user_agent(data)
        return self._make_request("createTask", data).get("taskId")
