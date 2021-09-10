import unittest
from inspect import stack
from os import environ
from capmonster_python import *

client_key = environ["KEY"]
acceptable_error_codes = ["ERROR_CAPTCHA_UNSOLVABLE", "ERROR_MAXIMUM_TIME_EXCEED"]


class TestImageToText(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestImageToText, self).__init__(*args, **kwargs)
        self.captcha = ImageToTextTask(client_key)

    def test_text_captcha(self):
        task_id = self.captcha.create_task(image_path="tests/utils/text_captcha.png", recognizing_threshold=50)
        self.assertIs(type(task_id), int)
        solution = self.captcha.join_task_result(task_id)
        self.assertIs(type(solution), dict)
        self.assertIn("text", solution)
        del solution, task_id

    def test_encoded_image_input(self):
        with open("tests/utils/text_captcha_encoded.txt", "r") as tce:
            captcha_img = tce.read()
        task_id = self.captcha.create_task(base64_encoded_image=captcha_img, recognizing_threshold=50)
        self.assertIs(type(task_id), int)
        solution = self.captcha.join_task_result(task_id)
        self.assertIs(type(solution), dict)
        self.assertIn("text", solution)
        del solution, task_id, captcha_img

    def test_numeric_captcha(self):
        task_id = self.captcha.create_task(image_path="tests/utils/numeric_captcha.png", recognizing_threshold=50,
                                           numeric=1)
        self.assertIs(type(task_id), int)
        solution = self.captcha.join_task_result(task_id)
        self.assertIs(type(solution), dict)
        self.assertIn("text", solution)
        del solution, task_id


class TestRecaptchaV2(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRecaptchaV2, self).__init__(*args, **kwargs)
        self.captcha = RecaptchaV2Task(client_key)
        self.dump_cookies = {
            "cookie_1": "value_1",
            "cookie_2": "value_2",
            "cookie_3": "value_3"
        }

    def test_proxyless_recaptchav2(self):
        task_id = self.captcha.create_task("https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level"
                                           "=high", "6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd",
                                           cookies=self.dump_cookies)
        self.assertIs(type(task_id), int)
        solution = self.captcha.join_task_result(task_id)
        self.assertIs(type(solution), dict)
        self.assertIn("gRecaptchaResponse", solution)
        del task_id, solution

    def test_proxy_recaptchav2(self):
        self.captcha.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")
        self.captcha.set_proxy("http", "8.8.8.8", 8080)
        task_id = self.captcha.create_task("https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level"
                                           "=high", "6Lcg7CMUAAAAANphynKgn9YAgA4tQ2KI_iqRyTwd",
                                           cookies=self.dump_cookies, no_cache=True)
        self.assertIs(type(task_id), int)
        solution = self.captcha.join_task_result(task_id)
        self.assertIs(type(solution), dict)
        self.assertIn("gRecaptchaResponse", solution)
        self.captcha.disable_proxy()
        self.captcha.reset_user_agent()


class TestRecaptchaV3(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRecaptchaV3, self).__init__(*args, **kwargs)
        self.captcha = RecaptchaV3Task(client_key)

    def test_recaptchav3(self):
        task_id = self.captcha.create_task("https://lessons.zennolab.com/captchas/recaptcha/v3.php?level=beta",
                                           "6Le0xVgUAAAAAIt20XEB4rVhYOODgTl00d8juDob", 0.6, "myverify")
        self.assertIs(type(task_id), int)
        solution = self.captcha.join_task_result(task_id)
        self.assertIs(type(solution), dict)
        self.assertIn("gRecaptchaResponse", solution)
        del solution, task_id


class TestFuncaptchaTask(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestFuncaptchaTask, self).__init__(*args, **kwargs)
        self.captcha = FuncaptchaTask(client_key)
        self.dump_cookies = {
            "cookie_1": "value_1",
            "cookie_2": "value_2",
            "cookie_3": "value_3"
        }

    def test_proxyless_funcaptcha(self):
        try:
            task_id = self.captcha.create_task("https://funcaptcha.com/fc/api/nojs/?pkey=69A21A01-CC7B-B9C6-0F9A"
                                               "-E7FA06677FFC", "69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC",
                                               data_blob="{\"blob\":\"dyXvXANMbHj1iDyz.Qj97JtSqR2n%2BuoY1V%2FbdgbrG7p"
                                                         "%2FmKiqdU9AwJ6MifEt0np4vfYn6TTJDJEfZDlcz9Q1XMn9przeOV%2FCr2"
                                                         "%2FIpi%2FC1s%3D\"}")
            self.assertIs(type(task_id), int)
            solution = self.captcha.join_task_result(task_id)
            self.assertIs(type(solution), dict)
            self.assertIn("token", solution)
            del solution, task_id
        except CapmonsterException as err:
            if any(err.error_code in s for s in acceptable_error_codes):
                print("Raised error code in " + stack()[0][3] + " but it's ok: {}".format(err.error_code))
                pass

    def test_proxy_funcaptcha(self):
        try:
            self.captcha.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")
            self.captcha.set_proxy("http", "8.8.8.8", 8080)
            task_id = self.captcha.create_task("https://funcaptcha.com/fc/api/nojs/?pkey=69A21A01-CC7B-B9C6-0F9A"
                                               "-E7FA06677FFC", "69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC",
                                               data_blob="{\"blob\":\"dyXvXANMbHj1iDyz.Qj97JtSqR2n%2BuoY1V%2FbdgbrG7p"
                                                         "%2FmKiqdU9AwJ6MifEt0np4vfYn6TTJDJEfZDlcz9Q1XMn9przeOV%2FCr2"
                                                         "%2FIpi%2FC1s%3D\"}")
            self.assertIs(type(task_id), int)
            solution = self.captcha.join_task_result(task_id)
            self.assertIs(type(solution), dict)
            self.assertIn("token", solution)
            self.captcha.disable_proxy()
            self.captcha.reset_user_agent()
            del solution, task_id
        except CapmonsterException as err:
            if any(err.error_code in s for s in acceptable_error_codes):
                print("Raised error code in " + stack()[0][3] + " but it's ok: {}".format(err.error_code))
                pass


class TestHCaptcha(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHCaptcha, self).__init__(*args, **kwargs)
        self.captcha = HCaptchaTask(client_key)
        self.dump_cookies = {
            "cookie_1": "value_1",
            "cookie_2": "value_2",
            "cookie_3": "value_3"
        }

    def test_proxyless_hcaptcha(self):
        try:
            self.captcha.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")
            task_id = self.captcha.create_task("https://lessons.zennolab.com/captchas/hcaptcha/?level=easy",
                                               "472fc7af-86a4-4382-9a49-ca9090474471", cookies=self.dump_cookies)
            self.assertIs(type(task_id), int)
            solution = self.captcha.join_task_result(task_id)
            self.assertIs(type(solution), dict)
            self.assertIn("gRecaptchaResponse", solution)
            del solution, task_id
        except CapmonsterException as err:
            if any(err.error_code in s for s in acceptable_error_codes):
                print("Raised error code in " + stack()[0][3] + " but it's ok: {}".format(err.error_code))
                pass

    def test_proxy_hcaptcha(self):
        try:
            self.captcha.set_proxy("http", "8.8.8.8", 8080)
            task_id = self.captcha.create_task("https://lessons.zennolab.com/captchas/hcaptcha/?level=moderate",
                                               "d391ffb1-bc91-4ef8-a45a-2e2213af091b", cookies=self.dump_cookies)
            self.assertIs(type(task_id), int)
            solution = self.captcha.join_task_result(task_id)
            self.assertIs(type(solution), dict)
            self.assertIn("gRecaptchaResponse", solution)
            self.captcha.disable_proxy()
            self.captcha.reset_user_agent()
            del solution, task_id
        except CapmonsterException as err:
            if any(err.error_code in s for s in acceptable_error_codes):
                print("Raised error code in " + stack()[0][3] + " but it's ok: {}".format(err.error_code))
                pass

    def test_invisible_hcaptcha(self):
        try:
            task_id = self.captcha.create_task(
                "https://lessons.zennolab.com/captchas/hcaptcha/invisible.php?level=moderate",
                "d391ffb1-bc91-4ef8-a45a-2e2213af091b", is_invisible=True)
            self.assertIs(type(task_id), int)
            solution = self.captcha.join_task_result(task_id)
            self.assertIs(type(solution), dict)
            self.assertIn("gRecaptchaResponse", solution)
            del solution, task_id
        except CapmonsterException as err:
            if any(err.error_code in s for s in acceptable_error_codes):
                print("Raised error code in " + stack()[0][3] + " but it's ok: {}".format(err.error_code))
                pass


if __name__ == "__main__":
    unittest.main()
