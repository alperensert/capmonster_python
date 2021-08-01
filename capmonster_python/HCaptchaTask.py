from .CapmonsterClient import CapmonsterClient


class HCaptchaTask(CapmonsterClient):
    def __init__(self, client_key, **kwargs):
        super().__init__(client_key=client_key, **kwargs)
        self.userAgent = kwargs.get("userAgent")
        self.solution = "solution"
        self.result_getter = "gRecaptchaResponse"

    def createTask(self, website_url, website_key, proxyAddress, proxyPort, proxyLogin, proxyPassword, proxyType="https", cookies=None):
        data = {
            "clientKey": self.client_key,
            "task":
            {
                "type": "HCaptchaTask",
                "websiteURL": website_url,
                "websiteKey": website_key,
                "proxyType": proxyType,
                "proxyAddress": proxyAddress,
                "proxyPort": proxyPort,
                "proxyLogin": proxyLogin,
                "proxyPassword": proxyPassword,
                "userAgent": self.userAgent
            }
        }
        if cookies is not None and type(cookies) == dict or type(cookies) == list:
            add_cookies = ""
            if type(cookies) == dict:
                for key, value in cookies.items():
                    if value == list(cookies.items())[-1][1]:
                        add_cookies += "{}={}".format(key, value)
                    else:
                        add_cookies += "{}={};".format(key, value)
            elif type(cookies) == list:
                for i in cookies:
                    if not len(cookies) % 2 == 0:
                        raise AttributeError("List cookies length must be even numbers")
                    if cookies.index(i) % 2 == 0:
                        add_cookies += "{}=".format(i)
                    elif cookies[cookies.index(i)] == cookies[-1]:
                        add_cookies += "{}".format(i)
                    elif cookies.index(i) % 2 == 1:
                        add_cookies += "{};".format(i)
            data["task"]["cookies"] = add_cookies
            del add_cookies
        task = self.make_request(method="createTask", data=data)
        self.checkResponse(response=task)
        return task.json()["taskId"]
