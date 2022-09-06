from app.helpers.base_helpers import BaseLogic


class UserLogic(BaseLogic):
    def __init__(self):
        super().__init__()

    @staticmethod
    def select_users(data):
        return data
