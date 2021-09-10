import requests
from bs4 import BeautifulSoup
from capmonster_python import HCaptchaTask


class HCaptchaRequest:
    def __init__(self, _client_key: str):
        self.captcha = HCaptchaTask(_client_key)
        self.s = requests.Session()
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        self.s.headers = {"User-Agent": self.user_agent}
        self.website_url = "http://hcaptcha.jawne.info.pl/"
        self.expected = "Your request have submitted successfully."

    def _form_html(self):
        return self.s.get(self.website_url).text

    def _site_token(self):
        site_key = BeautifulSoup(self._form_html(), "html.parser").find("div", {"class": "h-captcha"})["data-sitekey"]
        print("# Site key is found: {}".format(site_key))
        self.captcha.set_user_agent(self.user_agent)
        task_id = self.captcha.create_task(website_url=self.website_url, website_key=site_key)
        print("# Task created successfully with the following id: {}".format(task_id))
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
    example_request = HCaptchaRequest(client_key)
    assert example_request.expected in example_request.submit_form()
    print("# Submit is succeed, test is OK")
