class InvalidInputException(Exception):
    def __init__(self, param, value):
        super(InvalidInputException, self).__init__("Invalid Input {} : {}".format(param, value))


class NotAuthorizedException(InvalidInputException):
    def __init__(self):
        super(NotAuthorizedException, self).__init__("token", "Not Authorized")
