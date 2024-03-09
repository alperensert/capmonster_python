import requests
import asyncio
from time import sleep
from .utils import *


class Capmonster:
    """A class that interacts with the Capmonster API."""
    __SOFT_ID = 30
    _HOST_URL = "https://api.capmonster.cloud"
    _CREATE_TASK_URL = "/createTask"
    _TASK_RESULT_URL = "/getTaskResult"
    _BALANCE_URL = "/getBalance"
    _INCORRECT_IMAGE_CAPTCHA_URL = "/reportIncorrectImageCaptcha"
    _INCORRECT_TOKEN_CAPTCHA_URL = "/reportIncorrectTokenCaptcha"

    def __init__(self, client_key):
        self._client_key = client_key

    def get_balance(self) -> float:
        """
        Retrieves the balance of the client.

        :return: The balance of the client as a float.
        """
        data = {"clientKey": self._client_key}
        return self._make_request("getBalance", data).get("balance")

    def get_task_result(self, task_id: int):
        """
        :param task_id: The ID of the task for which the result is requested.
        :return: The result of the task if it is ready, otherwise False.
        """
        data = {
            "clientKey": self._client_key,
            "taskId": task_id
        }
        result = self._make_request("getTaskResult", data)
        is_ready = self._is_ready(result)
        if is_ready:
            return result.get("solution")
        else:
            return False

    def join_task_result(self, task_id: int, maximum_time: int = 120):
        for i in range(0, maximum_time + 1, 2):
            result = self.get_task_result(task_id)
            if result is not False and result is not None:
                return result
            elif result is False:
                i += 1
                sleep(2)
        raise CapmonsterException(
            61, "ERROR_MAXIMUM_TIME_EXCEED", "Maximum time is exceed.")

    async def join_task_result_async(self, task_id: int, maximum_time: int = 120):
        for i in range(0, maximum_time + 1, 2):
            result = self.get_task_result(task_id)
            if result is not False and result is not None:
                return result
            elif result is False:
                i += 1
                await asyncio.sleep(2)
        raise CapmonsterException(
            61, "ERROR_MAXIMUM_TIME_EXCEED", "Maximum time is exceed.")

    def report_incorrect_captcha(self, captcha_type: str, task_id: int) -> bool:
        """
        Reports an incorrect captcha.

        :param captcha_type: The type of captcha ("image" or "token").
        :param task_id: The ID of the task.
        :return: True if the captcha is successfully reported, False otherwise.
        :raises CapmonsterException: If the captcha type is invalid.
        """
        valid_captcha_types = ["image", "token"]
        
        if captcha_type not in valid_captcha_types:
            raise CapmonsterException(
                1, "ERROR_INCORRECT_CAPTCHA_TYPE", "Valid captcha_type parameters are only 'image' or 'token'.")
        try:
            self._report_incorrect_captcha(
                captcha_type=captcha_type, task_id=task_id)
            return True
        except:
            return False

    @check_response()
    def _report_incorrect_captcha(self, captcha_type: str, task_id: int):
        data = {
            "clientKey": self._client_key,
            "taskId": task_id
        }
        if captcha_type == "image":
            response = self._make_request("reportIncorrectImageCaptcha", data)
        else:
            response = self._make_request("reportIncorrectTokenCaptcha", data)
        return response

    @staticmethod
    def _is_ready(response: dict):
        status = response.get("status")
        if status == "processing":
            return False
        elif status == "ready":
            return True

    @check_response()
    def _make_request(self, method: str, data: dict):
        _method = None
        if method == "getBalance":
            _method = self._BALANCE_URL
        elif method == "getTaskResult":
            _method = self._TASK_RESULT_URL
        elif method == "createTask":
            _method = self._CREATE_TASK_URL
            data["softId"] = self.__SOFT_ID
        elif method == "reportIncorrectImageCaptcha":
            _method = self._INCORRECT_IMAGE_CAPTCHA_URL
        elif method == "reportIncorrectTokenCaptcha":
            _method = self._INCORRECT_TOKEN_CAPTCHA_URL
        try:
            response = requests.post("{}{}".format(
                self._HOST_URL, _method), json=data).json()
        except Exception as err:
            raise CapmonsterException(-1, type(err).__name__, str(err))
        return response

    @staticmethod
    def _add_cookies(cookies, data):
        if cookies is None:
            return data
        str_cookies = ""
        if type(cookies) is dict:
            for key, value in cookies.items():
                if value == list(cookies.items())[-1][1]:
                    str_cookies += "{}={}".format(key, value)
                else:
                    str_cookies += "{}={};".format(key, value)
        elif type(cookies) is list:
            for i in cookies:
                if not len(cookies) % 2 == 0:
                    raise AttributeError(
                        "List cookies length must be even numbers")
                if cookies.index(i) % 2 == 0:
                    str_cookies += "{}=".format(i)
                elif cookies[cookies.index(i)] == cookies[-1]:
                    str_cookies += "{}".format(i)
                elif cookies.index(i) % 2 == 1:
                    str_cookies += "{};".format(i)
        elif type(cookies) is str:
            data["task"]["cookies"] = cookies
            return data
        data["task"]["cookies"] = str_cookies
        return data


class Proxy(Capmonster):
    def __init__(self, client_key):
        super().__init__(client_key)
        self._proxy_type = None
        self._proxy_address = None
        self._proxy_port = None
        self._proxy_login = None
        self._proxy_password = None

    def set_proxy(self, proxy_type: str, proxy_address: str, proxy_port: int,
                  proxy_login: str = None, proxy_password: str = None):
        """
        Sets the proxy settings for the client.

        :param proxy_type: The type of the proxy. (e.g. "HTTP", "SOCKS5")
        :param proxy_address: The address of the proxy server.
        :param proxy_port: The port number of the proxy server.
        :param proxy_login: (optional) The login username for proxy authentication.
        :param proxy_password: (optional) The login password for proxy authentication.
        :return: None
        """
        self._proxy_type = proxy_type
        self._proxy_address = proxy_address
        self._proxy_port = proxy_port
        self._proxy_login = proxy_login
        self._proxy_password = proxy_password

    def disable_proxy(self):
        """
        Disables the proxy settings.

        :return: None
        """
        self._proxy_type = None
        self._proxy_address = None
        self._proxy_port = None
        self._proxy_login = None
        self._proxy_password = None

    def _is_proxy_task(self, data: dict):
        """
        Determine for is this a proxy task or not?
        e.g. if you are not set the values with set_proxy method, it is a proxyless method, or if you are set up it is a
        proxy task.
        """
        if self._proxy_type and self._proxy_address and self._proxy_port:
            data["task"]["proxyType"] = self._proxy_type
            data["task"]["proxyAddress"] = self._proxy_address
            data["task"]["proxyPort"] = self._proxy_port
            if self._proxy_login and self._proxy_password:
                data["task"]["proxyLogin"] = self._proxy_login
                data["task"]["proxyPassword"] = self._proxy_password
            return data, True
        data["task"]["type"] += "Proxyless"
        return data, False


class UserAgent(Capmonster):
    def __init__(self, client_key):
        super().__init__(client_key)
        self._user_agent = None
        self._fallback = False

    def set_user_agent(self, user_agent: str):
        """
        Set the user agent for the instance.

        :param user_agent: The user agent string to set.
        :return: None
        """
        self._user_agent = user_agent

    def reset_user_agent(self):
        """
        Reset the user agent to None.

        :return:
        """
        self._user_agent = None

    def _add_user_agent(self, data):
        data["task"]["fallbackToActualUA"] = self._fallback
        if self._user_agent:
            data["task"]["userAgent"] = self._user_agent
            return data, True
        return data, False

    def set_fallback_to_actual_user_agent(self, fallback: bool):
        """
        Set the fallback value for the actual user agent.

        :param fallback: A boolean value indicating whether to enable or disable the fallback.
        :type fallback: bool
        :return: None
        """
        self._fallback = fallback
