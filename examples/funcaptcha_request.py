import requests
import re
from capmonster_python import FuncaptchaTask


class FuncaptchaRequest:
    def __init__(self, _client_key: str):
        self.captcha = FuncaptchaTask(_client_key)
        self.s = requests.Session()
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        self.s.headers = {"User-Agent": self.user_agent}
        self.website_url = "https://client-demo.arkoselabs.com/solo-animals"
        self.expected = "Solved!"

    def _form_html(self):
        return self.s.get(self.website_url).text

    def _site_token(self):
        site_key = re.search("public_key: \"(.+?)\"", self._form_html()).group(1)
        print("# Site key is found: {}".format(site_key))
        task_id = self.captcha.create_task(website_url=self.website_url, website_public_key=site_key)
        print("# Task created successfully with the following id: {}".format(task_id))
        result = self.captcha.join_task_result(task_id=task_id)
        print("# Response received")
        return result.get("token")

    def submit_form(self):
        result = self._site_token()
        data = {
            "name": "xx",
            "fc-token": result
        }
        return self.s.post(f"{self.website_url}/verify", data=data).text


if __name__ == "__main__":
    from os import environ
    client_key = environ["API_KEY"]
    example_request = FuncaptchaRequest(client_key)
    assert example_request.expected in example_request.submit_form()
    print("# Submit succeed, test is OK")
