from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from capmonster_python import RecaptchaV2Task
from time import sleep


class RecaptchaV2Selenium:
    def __init__(self, _client_key, _headless):
        self.options = Options()
        self.options.headless = _headless
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        self.captcha = RecaptchaV2Task(_client_key)
        self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=self.options)
        self.website_url = "https://www.google.com/recaptcha/api2/demo"

    def _get_site_key(self):
        self.browser.get("https://www.google.com/recaptcha/api2/demo")
        return self.browser.find_element(By.ID, "recaptcha-demo").get_attribute("data-sitekey")

    def _solve_recaptcha(self):
        self.captcha.set_user_agent(self.user_agent)
        task_id = self.captcha.create_task(website_url=self.website_url,
                                           website_key=self._get_site_key(),
                                           no_cache=True)
        print("# Task created successfully with the following id: {}".format(task_id))
        return self.captcha.join_task_result(task_id=task_id, maximum_time=180).get("gRecaptchaResponse")

    def submit_form(self):
        self.browser.execute_script("document.getElementsByClassName('g-recaptcha-response')[0].innerHTML = "
                                    f"'{self._solve_recaptcha()}';")
        print("# Response received and placed to g-recaptcha-response textarea")
        self.browser.find_element(By.ID, "recaptcha-demo-submit").click()
        sleep(5)
        source = self.browser.find_element(By.CLASS_NAME, "recaptcha-success")
        self.browser.close()
        return source


if __name__ == "__main__":
    from os import environ
    client_key = environ["API_KEY"]
    headless = environ["HEADLESS"]
    environ["WDM_LOG_LEVEL"] = "0"
    recaptcha_selenium = RecaptchaV2Selenium(client_key, headless)
    assert recaptcha_selenium.submit_form() is not None
    print("# Submit is succeed, test is OK")
