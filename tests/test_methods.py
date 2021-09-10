import unittest
from os import environ
from capmonster_python import ImageToTextTask

client_key = environ["KEY"]


class TestMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMethods, self).__init__(*args, **kwargs)
        self.captcha = ImageToTextTask(client_key)

    def test_get_balance(self):
        balance = self.captcha.get_balance()
        self.assertIs(type(balance), float)

    def test_join_task_result(self):
        task_id = self.captcha.create_task(image_path="tests/utils/text_captcha.png", recognizing_threshold=50)
        solution = self.captcha.join_task_result(task_id)
        self.assertIs(type(solution), dict)
        self.assertIn("text", solution)


if __name__ == "__main__":
    unittest.main()
