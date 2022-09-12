class AppException(Exception):
    def __init__(self, message):
        super(AppException, self).__init__(message)


class InvalidFieldName(AppException):
    def __init__(self, field_name):
        super(InvalidFieldName, self).__init__("Field {} is invalid.".format(field_name))


class RequiredFieldError(AppException):
    def __init__(self, field_name):
        super(RequiredFieldError, self).__init__("Field {} is required.".format(field_name))


class UserExists(AppException):
    def __init__(self):
        super(UserExists, self).__init__("User with this information already exists.")


class InvalidUser(AppException):
    def __init__(self):
        super(InvalidUser, self).__init__("User with this information does not exist.")


class PermissionDenied(AppException):
    def __init__(self, role):
        super(PermissionDenied, self).__init__("You have to be a {} to perform this action.".format(role))
