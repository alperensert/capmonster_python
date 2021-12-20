import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from capmonster_python import FuncaptchaTask
from time import sleep


class FuncaptchaSelenium:
    def __init__(self, _client_key, _headless):
        self.options = Options()
        self.options.headless = _headless
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        self.captcha = FuncaptchaTask(_client_key)
        self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=self.options)
        self.website_url = "https://client-demo.arkoselabs.com/solo-animals"
        self.expected = "Solved!"

    def _get_site_key(self):
        self.browser.get(self.website_url)
        return re.search("public_key: \"(.+?)\",", self.browser.page_source).group(1)

    def _solve_funcaptcha(self):
        self.captcha.set_user_agent(self.user_agent)
        task_id = self.captcha.create_task(website_url=self.website_url,
                                           website_public_key=self._get_site_key())
        print("# Task created successfully with the following id: {}".format(task_id))
        return self.captcha.join_task_result(task_id=task_id, maximum_time=180).get("token")

    def submit_form(self):
        self.browser.execute_script("""
        document.getElementById('FunCaptcha-Token').value = decodeURIComponent('{0}')
        document.getElementById('verification-token').value = decodeURIComponent('{0}')
        document.getElementById('submit-btn').disabled = false
        """.format(self._solve_funcaptcha()))
        print("# Response received and placed to (FunCaptcha-Token and verifaction-token) textarea")
        self.browser.find_element(By.ID, "submit-btn").click()
        sleep(5)
        h3_text = self.browser.find_element(By.CSS_SELECTOR, "h3").text
        self.browser.close()
        return h3_text


if __name__ == "__main__":
    from os import environ
    client_key = environ["API_KEY"]
    headless = environ["HEADLESS"]
    environ["WDM_LOG_LEVEL"] = "0"
    funcaptcha_selenium = FuncaptchaSelenium(client_key, headless)
    assert funcaptcha_selenium.expected in funcaptcha_selenium.submit_form()
    print("# Submit is succeed, test is OK")
