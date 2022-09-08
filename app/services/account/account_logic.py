from app.helpers.base_helpers import BaseLogic
from app.helpers.mongo_helper import MongoWrapper


class AccountLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()

    def update_balance(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def add_transaction(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def get_transactions(self, data):
        mongo_helper = self.mongo_wrapper
        return data

    def get_account(self, data):
        mongo_helper = self.mongo_wrapper
        return data
    
