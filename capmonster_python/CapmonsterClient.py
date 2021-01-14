import requests
from .exceptions import *


class CapmonsterClient(object):
    SOFT_ID = 30
    BALANCE_URL = "/getBalance"
    TASK_RESULT_URL = "/getTaskResult"
    CREATE_TASK_URL = "/createTask"

    def __init__(self, client_key, **kwargs):
        self.protocol = "https" if kwargs.get("protocol") == "https" else "http"
        self.client_key = client_key
        self.host = "{protocol}://api.capmonster.cloud".format(protocol=self.protocol)
        self.checkResponse(requests.post(url=f"{self.host}{self.BALANCE_URL}", json={"clientKey": self.client_key}))
        self.session = requests.Session()

    def checkResponse(self, response):
        response_json = response.json()
        if response_json.get("errorId") is not None and response_json.get("errorId") == 0:
            return True
        elif not response.status_code == 200:
            raise CapmonsterException(error_id=-1,
                                      error_code="HTTP_ERROR",
                                      error_description="Sometimes can be happen if capmonster servers there is too much intensity")
        elif not response_json.get("errorId") == 0:
            raise CapmonsterException(error_id=response_json.get("errorId"),
                                      error_code=response_json.get("errorCode"),
                                      error_description=response_json.get("errorDescription"))
        else:
            raise CapmonsterException(error_id=-1,
                                      error_code="HTTP_ERROR",
                                      error_description="Sometimes can be happen if capmonster servers there is too much intensity")

    def checkReady(self, response):
        status = response.json().get("status")
        if status == "processing":
            return False
        elif status == "ready":
            return True
        else:
            raise CapmonsterException(error_id=7,
                                      error_code="ERROR_NO_SUCH_CAPCHA_ID",
                                      error_description="The captcha that you are requesting was not found. Make sure you are requesting a status update only within 5 minutes of uploading.")

    def make_request(self, method, data):
        if method == "getBalance":
            method = self.BALANCE_URL
        elif method == "getTaskResult":
            method = self.TASK_RESULT_URL
        elif method == "createTask":
            method = self.CREATE_TASK_URL
            data["softId"] = self.SOFT_ID
        try:
            response = self.session.post(f"{self.host}{method}", json=data)
        except Exception as err:
            raise CapmonsterException(error_id=-1,
                                      error_code=type(err).__name__,
                                      error_description=str(err))
        return response

    def getBalance(self):
        data = {
            "clientKey": self.client_key
        }
        response = self.make_request(method="getBalance", data=data)
        self.checkResponse(response=response)
        return response.json().get("balance")
