from .capmonster import Capmonster

class AmazonWafTask(Capmonster):
    def __init__(self, client_key):
        super(AmazonWafTask, self).__init__(client_key)

    def create_task(self, website_url: str, website_key: str, challenge_script: str, captcha_script: str,
                    context: str, iv: str, cookieSolution: bool = False):
        data = {
            "clientKey": self._client_key,
            "task": {
                "type": "AmazonTaskProxyless",
                "websiteURL": website_url,
                "websiteKey": website_key,
                "challengeScript": challenge_script,
                "captchaScript": captcha_script,
                "context": context,
                "iv": iv,
                "cookieSolution": cookieSolution
            }
        }
        return self._make_request("createTask", data).get("taskId")