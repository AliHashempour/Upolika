class AppException(Exception):
    def __init__(self, message):
        super(AppException, self).__init__(message)
        