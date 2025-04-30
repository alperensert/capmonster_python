class CapmonsterException(Exception):
    def __init__(self, error_id, error_code, error_description, *args, **kwargs):
        super(CapmonsterException, self).__init__("[{}:{}]{}".format(error_code, error_id, error_description))
        self.error_description = error_description
        self.error_id = error_id
        self.error_code = error_code

    def __str__(self):
        return "[{}] {}".format(self.error_code, self.error_description)
