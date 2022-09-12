from app.helpers.base_helpers import BaseLogic
from app.helpers.config_helper import ConfigHelper
from app.helpers.mongo_helper import MongoWrapper


class UserLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()
        self.cfg_helper = ConfigHelper()
        self.user_table_name = self.cfg_helper.get_config("USER")["table_name"]
        self.account_table_name = self.cfg_helper.get_config("ACCOUNT")["table_name"]

    def add_account(self, request_body):
        pass

    def remove_account(self, request_body):
        mongo_helper = self.mongo_wrapper
        pass

    def deposit(self, request_body):
        mongo_helper = self.mongo_wrapper
        pass

    def withdraw(self, request_body):
        mongo_helper = self.mongo_wrapper
        pass

    def transfer(self, request_body):
        mongo_helper = self.mongo_wrapper
        pass

    def check_balance(self, request_body):
        mongo_helper = self.mongo_wrapper
        pass

    def select_accounts(self, request_body):
        mongo_helper = self.mongo_wrapper
        pass

    def get_user(self, request_body):
        mongo_helper = self.mongo_wrapper
        pass
