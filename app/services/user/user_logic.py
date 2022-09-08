from app.helpers.base_helpers import BaseLogic
from app.helpers.mongo_helper import MongoWrapper


class UserLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()

    def add_account(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def remove_account(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def deposit(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def withdraw(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def transfer(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def check_balance(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def select_accounts(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def get_user(self, data):
        mongo_helper = self.mongo_wrapper
        return data
