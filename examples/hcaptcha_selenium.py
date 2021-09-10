from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from capmonster_python import HCaptchaTask
from time import sleep


class HCaptchaSelenium:
    def __init__(self, _client_key, _headless):
        self.options = Options()
        self.options.headless = _headless
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
        self.captcha = HCaptchaTask(_client_key)
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=self.options)
        self.website_url = "http://hcaptcha.jawne.info.pl/"
        self.expected = "Your request have submitted successfully"

    def _get_site_key(self):
        self.browser.get(self.website_url)
        return self.browser.find_element_by_class_name("h-captcha").get_attribute("data-sitekey")

    def _solve_hcaptcha(self):
        self.captcha.set_user_agent(self.user_agent)
        print("# User agent setted")
        task_id = self.captcha.create_task(website_url=self.website_url,
                                           website_key=self._get_site_key())
        print("# Task created successfully with the following id: {}".format(task_id))
        return self.captcha.join_task_result(task_id=task_id, maximum_time=180).get("gRecaptchaResponse")

    def submit_form(self):
        self.browser.execute_script("document.querySelector(\"textarea[name='g-recaptcha-response'"
                                    "]\").value = '{}'".format(self._solve_hcaptcha()))
        print("# Response received and placed to textarea")
        self.browser.find_element_by_id("fname").send_keys("xxx")
        self.browser.find_element_by_css_selector("input[type='submit']").click()
        sleep(5)
        source = self.browser.page_source
        self.browser.close()
        return source


if __name__ == "__main__":
    from os import environ
    client_key = environ["API_KEY"]
    headless = environ["HEADLESS"]
    environ["WDM_LOG_LEVEL"] = "0"
    hcaptcha_selenium = HCaptchaSelenium(client_key, headless)
    assert hcaptcha_selenium.expected in hcaptcha_selenium.submit_form()
    print("# Submit succeed, test is OK")
