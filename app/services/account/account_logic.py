from app.helpers.base_helpers import BaseLogic
from app.helpers.config_helper import ConfigHelper
from app.helpers.mongo_helper import MongoWrapper


class AccountLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()
        self.cfg_helper = ConfigHelper()
        self.account_table_name = self.cfg_helper.get_config("ACCOUNT")["table_name"]

    def update_balance(self, request_body):
        mongo_helper = self.mongo_wrapper

    def add_transaction(self, request_body):
        mongo_helper = self.mongo_wrapper

    def get_transactions(self, request_body):
        mongo_helper = self.mongo_wrapper

    def get_account(self, request_body):
        mongo_helper = self.mongo_wrapper
