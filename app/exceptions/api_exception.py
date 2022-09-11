class PermissionDeniedException(Exception):
    def __init__(self):
        super(PermissionDeniedException, self).__init__("PERMISSION DENIED")


class InvalidInputException(Exception):
    def __init__(self, param, value):
        super(InvalidInputException, self).__init__("INVALID INPUT %s: %s" % (param, value))


class NotAuthenticatedException(InvalidInputException):
    def __init__(self):
        super(NotAuthenticatedException, self).__init__("API_KEY", "Not Authenticated")


class NotAuthorizedException(InvalidInputException):
    def __init__(self):
        super(NotAuthorizedException, self).__init__("token", "Not Authorized")


class InvalidConfigException(Exception):
    def __init__(self, param, value):
        super(InvalidConfigException, self).__init__("UNDEFINED PARAM %s: %s" % (param, value))
