class AppException(Exception):
    def __init__(self, message):
        super(AppException, self).__init__(message)


class InvalidFieldName(AppException):
    def __init__(self, field_name):
        super(InvalidFieldName, self).__init__("Field %s is invalid." % field_name)


class RequiredFieldError(AppException):
    def __init__(self, field_name):
        super(RequiredFieldError, self).__init__("Field %s is required." % field_name)
