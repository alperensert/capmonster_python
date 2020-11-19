import requests
import urllib3
import json
from .exceptions import CapmonsterException


class CapmonsterClient(object):
    client_key = None
    BALANCE_URL = "/getBalance"
    TASK_RESULT_URL = "/getTaskResult"
    CREATE_TASK_URL = "/createTask"
    SOFT_ID = 30

    def __init__(self, client_key, host="https://api.capmonster.cloud"):
        self.client_key = client_key
        self.host = host
        try:
            response = requests.post(url=f"{self.host}{self.BALANCE_URL}", json={"clientKey": self.client_key}).json()
        except json.decoder.JSONDecodeError:
            raise CapmonsterException("JSONDecodeError", -1, "Capmonster is returned empty content.")
        if response["errorId"] != 0: raise CapmonsterException(response["errorId"], response["errorCode"], response["errorDescription"])
        else: self.session = requests.Session()

    def checkResponse(self, response):
        if response["errorId"] != 0:
            raise CapmonsterException(response["errorId"], response["errorCode"], response["errorDescription"])
        else:
            return True

    def checkReady(self, response):
        status = response.get("status")
        if status == "processing": return False
        elif status == "ready": return True

    def make_request(self, method, data):
        if method == "getBalance":
            method = self.BALANCE_URL
        elif method == "getTaskResult":
            method = self.TASK_RESULT_URL
        elif method == "createTask":
            method = self.CREATE_TASK_URL
            data["softId"] = self.SOFT_ID
        else:
            raise CapmonsterException("-1", "-1", "-1")
        try:
            response = self.session.post(url=f"{self.host}{method}", json=data)
            return response.json()
        except Exception as err:
            raise CapmonsterException("-1", type(err), "Capmonster.cloud returned 0 bytes.")

    def getBalance(self):
        data = {
            "clientKey": self.client_key
        }
        response = self.make_request(method="getBalance", data=data)
        self.checkResponse(response=response)
        return response.get("balance")
