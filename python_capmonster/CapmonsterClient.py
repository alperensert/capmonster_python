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
        if response.get("errorId") != 0:
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
        except requests.exceptions.HTTPError as err:
            self.err_string = "http_error"
            for errArg in err.args:
                if "Network is unreachable" in str(errArg):
                    self.err_string = "Network is unreachable"
                if "Connection refused" in str(errArg):
                    self.err_string = "Connection refused"
            return 0
        except requests.exceptions.ConnectTimeout:
            self.err_string = "Connection timeout"
            return 0
        except urllib3.exceptions.ConnectTimeoutError:
            self.err_string = "Connection timeout"
            return 0
        except requests.exceptions.ReadTimeout:
            self.err_string = "Read timeout"
            return 0
        except urllib3.exceptions.MaxRetryError as err:
            self.err_string = "Connection retry error: " + err.reason
            return 0
        except requests.exceptions.ConnectionError:
            self.err_string = "Connection refused"
            return 0
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            self.err_string = "JSON Decode error"
            return 0

    def getBalance(self):
        data = {
            "clientKey": self.client_key
        }
        response = self.make_request(method="getBalance", data=data)
        self.checkResponse(response=response)
        return response.get("balance")
