import requests
from re import search
from bs4 import BeautifulSoup
from capmonster_python import TurnstileTask


class TurnstileRequest:
    def __init__(self, _client_key: str):
        self.captcha = TurnstileTask(_client_key)
        self.s = requests.Session()
        self.s.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
        self.website_url = "http://tsmanaged.zlsupport.com"
        self.expected = 'Success!'

    def _form_html(self):
        return self.s.get(self.website_url).text

    def _site_token(self):
        site_key = search(r"sitekey: '(.+?)'", BeautifulSoup(self._form_html(), "html.parser").find_all("script")[1].text).group(1)
        print("# Site key found: {}".format(site_key))
        task_id = self.captcha.create_task(website_url=self.website_url, website_key=site_key)
        print("# Task created successfully")
        result = self.captcha.join_task_result(task_id=task_id)
        print("# Response received")
        return result.get("token")

    def submit_form(self):
        result = self._site_token()
        data = {
            'username': 'test',
            'password': 'test',
            'token': result,
        }
        response = self.s.post(self.website_url+'/send', data=data, headers=self.s.headers, verify=False)
        return BeautifulSoup(response.text, "html.parser").title.string


if __name__ == "__main__":
    from os import environ
    client_key = environ["API_KEY"]
    example_request = TurnstileRequest(client_key)
    assert example_request.expected in example_request.submit_form()
    print("# Submit succeed, test is OK")

