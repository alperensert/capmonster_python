from functools import wraps


class CapmonsterException(Exception):
    def __init__(self, error_id, error_code, error_description, *args, **kwargs):
        super(CapmonsterException, self).__init__("[{}:{}]{}".format(error_code, error_id, error_description))
        self.error_description = error_description
        self.error_id = error_id
        self.error_code = error_code

    def __str__(self):
        return "[{}] {}".format(self.error_code, self.error_description)


def check_response():
    def checker(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            rf = f(*args, **kwargs)
            if type(rf) == dict:
                if rf.get("errorId") == 0:
                    return rf
                else:
                    raise CapmonsterException(error_id=rf.get("errorId"),
                                              error_code=rf.get("errorCode"),
                                              error_description=rf.get("errorDescription"))
            else:
                raise CapmonsterException(error_id=-1,
                                          error_code="CAPMONSTER_API_ERROR",
                                          error_description="Sometimes can be happen if capmonster_python "
                                                            "servers there is too much intensity")
        return wrap
    return checker
