import requests
from bs4 import BeautifulSoup
from capmonster_python import RecaptchaV2Task


class RecaptchaRequest:
    def __init__(self, _client_key: str):
        self.captcha = RecaptchaV2Task(_client_key)
        self.s = requests.Session()
        self.s.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
        self.website_url = "https://google.com/recaptcha/api2/demo"
        self.expected = "Verification Success... Hooray!"

    def _form_html(self):
        return self.s.get(self.website_url).text

    def _site_token(self):
        site_key = BeautifulSoup(self._form_html(), "html.parser").find("div", {"id": "recaptcha-demo"})["data-sitekey"]
        print("# Site key found: {}".format(site_key))
        task_id = self.captcha.create_task(website_url=self.website_url, website_key=site_key)
        print("# Task created successfully")
        result = self.captcha.join_task_result(task_id=task_id)
        print("# Response received")
        return result.get("gRecaptchaResponse")

    def submit_form(self):
        result = self._site_token()
        data = {
            "g-recaptcha-response": result
        }
        return self.s.post(self.website_url, data=data).text


if __name__ == "__main__":
    from os import environ
    client_key = environ["API_KEY"]
    example_request = RecaptchaRequest(client_key)
    assert example_request.expected in example_request.submit_form()
    print("# Submit succeed, test is OK")
