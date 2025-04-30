class CapmonsterException(Exception):
    """
    Generic exception class for all errors.

    Notes:
        This will be raised for errors that are not caught elsewhere.
        These errors can be related HTTP requests, API responses, or other issues.
    """
    pass


class CapmonsterAPIException(CapmonsterException):
    """
    Raised when the Capmonster API returns an error.

    Attributes:
        error_id: The error ID returned by the API.
        error_code: The error code returned by the API.
        error_description: The error description returned by the API.

    Notes:
        - Error codes are defined in the API documentation.
    """

    def __init__(self, error_id, error_code, error_description, *args, **kwargs):
        super(CapmonsterAPIException, self).__init__("[{}:{}]{}".format(error_code, error_id, error_description))
        self.error_description = error_description
        self.error_id = error_id
        self.error_code = error_code

    def __str__(self):
        return "[{}] {}".format(self.error_code, self.error_description)


class CapmonsterValidationException(CapmonsterException):
    """
    Raised when a Capmonster task configuration is invalid.

    Attributes:
        message: The error message describing the invalid configuration.
        field: The field in the configuration that caused the error, if applicable.
        task: The task type that caused the error, if applicable.

    Notes:
        - This error only raises when the validation fails within the SDK task creation.
    """

    def __init__(self, message: str, *, field: str = None, task: str = None):
        self.message = message
        self.field = field
        self.task = task
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        base = f"[CapmonsterValidationError] {self.message}"
        if self.field:
            base += f" (field: {self.field})"
        if self.task:
            base += f" [task: {self.task}]"
        return base
