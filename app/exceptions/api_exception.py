from app.exceptions.general_exception import AppException


class InvalidInput(Exception):
    def __init__(self, param, value):
        super(InvalidInput, self).__init__("Invalid Input {} : {}".format(param, value))


class MethodPermissionDenied(Exception):
    def __init__(self):
        super(MethodPermissionDenied, self).__init__(" method permission denied")


class NotAuthorized(InvalidInput):
    def __init__(self):
        super(NotAuthorized, self).__init__("token", "Not Authorized")


class InvalidFieldName(AppException):
    def __init__(self, field_name):
        super(InvalidFieldName, self).__init__("Field {} is invalid.".format(field_name))


class RequiredFieldError(AppException):
    def __init__(self, field_name):
        super(RequiredFieldError, self).__init__("Field {} is required.".format(field_name))
