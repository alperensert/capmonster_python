from .CapmonsterClient import CapmonsterClient


class FunCaptchaTaskProxyless(CapmonsterClient):
    def __init__(self, client_key, **kwargs):
        super().__init__(client_key=client_key, **kwargs)
        self.solution = "solution"
        self.result_getter = "token"

    def createTask(self, website_url, website_public_key, js_subdomain=None, data_blob=None):
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "FunCaptchaTaskProxyless",
                "websiteURL": website_url,
                "websitePublicKey": website_public_key
            }
        }
        if js_subdomain is not None: data["task"]["funcaptchaApiJSSubdomain"] = js_subdomain
        if data_blob is not None: data["task"]["data"] = data_blob
        task = self.make_request(method="createTask", data=data)
        self.checkResponse(response=task)
        return task.json()["taskId"]
