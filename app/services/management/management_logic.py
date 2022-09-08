from app.helpers.base_helpers import BaseLogic
from app.helpers.mongo_helper import MongoWrapper


class ManagementLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()

    def sign_up(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def login_user(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def add_user(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def remove_user(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def select_users(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def add_account(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def remove_account(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def select_accounts(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def find_account(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def update_user(self, data):
        mongo_helper = self.mongo_wrapper
        return data
