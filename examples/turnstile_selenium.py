from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from capmonster_python import TurnstileTask
from time import sleep


class TurnstileSelenium:
    def __init__(self, _client_key, _headless):
        self.options = Options()
        self.options.headless = _headless
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        self.captcha = TurnstileTask(_client_key)
        self.browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=self.options)
        self.website_url = "http://tsmanaged.zlsupport.com"

    def _get_site_key(self):
        self.browser.get(self.website_url)
        return self.browser.find_elements(By.TAG_NAME, "script")[1].get_attribute("innerHTML").split("sitekey: '")[1].split("'")[0]

    def _solve_turnstile(self):
        self.captcha.set_user_agent(self.user_agent)
        task_id = self.captcha.create_task(website_url=self.website_url,
                                           website_key=self._get_site_key(),
                                           no_cache=True)
        print("# Task created successfully with the following id: {}".format(task_id))
        return self.captcha.join_task_result(task_id=task_id, maximum_time=180).get("token")

    def submit_form(self):
        token = self._solve_turnstile()
        self.browser.find_element(By.NAME, "username").send_keys("test")
        self.browser.find_element(By.NAME, "password").send_keys("test")
        self.browser.execute_script(f"document.getElementById('token').value = '{token}'")
        print("# Response received and placed to textarea")
        self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        sleep(5)
        source = self.browser.find_element(By.TAG_NAME, "code")
        self.browser.close()
        return source


if __name__ == "__main__":
    from os import environ
    client_key = environ["API_KEY"]
    headless = environ["HEADLESS"]
    environ["WDM_LOG_LEVEL"] = "0"
    turnstile_selenium = TurnstileSelenium(client_key, headless)
    assert turnstile_selenium.submit_form() is not None
    print("# Submit is succeed, test is OK")
