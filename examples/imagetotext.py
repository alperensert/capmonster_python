from capmonster_python import ImageToTextTask


class TextNumericExample:
    def __init__(self, _client_key: str):
        self.captcha = ImageToTextTask(_client_key)
        self.image_path_text = "examples/utils/text_captcha.png"
        self.image_path_numeric = "examples/utils/numeric_captcha.png"
        self.expected_1 = "fdamc"
        self.expected_2 = "246477"

    def solve_text(self):
        task_id = self.captcha.create_task(image_path=self.image_path_text, recognizing_threshold=70)
        print("# Task created successfully with the following id: {}".format(task_id))
        result = self.captcha.join_task_result(task_id=task_id)
        print("# Response received: {}".format(result.get("text")))
        return result.get("text")

    def solve_numeric(self):
        task_id = self.captcha.create_task(image_path=self.image_path_numeric, recognizing_threshold=70, numeric=1)
        print("# Task created successfully with the following id: {}".format(task_id))
        result = self.captcha.join_task_result(task_id=task_id)
        print("# Response received: {}".format(result.get("text")))
        return result.get("text")


if __name__ == "__main__":
    from os import environ
    client_key = environ["API_KEY"]
    example_text_numeric = TextNumericExample(client_key)
    assert example_text_numeric.expected_1 in example_text_numeric.solve_text()
    print("# Alphanumeric test is OK")
    assert example_text_numeric.expected_2 in example_text_numeric.solve_numeric()
    print("# Numeric test is OK")
