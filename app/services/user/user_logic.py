from app.helpers.base_helpers import BaseLogic
from app.helpers.config_helper import ConfigHelper
from app.helpers.mongo_helper import MongoWrapper
from app.definitions import account_definition, user_definition, transaction_definition
from app.helpers.policy_helper import *


class UserLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()
        self.cfg_helper = ConfigHelper()
        self.user_table_name = self.cfg_helper.get_config("USER")["table_name"]
        self.account_table_name = self.cfg_helper.get_config("ACCOUNT")["table_name"]

    def add_account(self, request_body):
        data = request_body['data']

        check_schema(data, account_definition.account_schema)
        processed_data = preprocess(data, account_definition.account_schema)

        account_existence = self.mongo_wrapper.exists(self.account_table_name, processed_data)
        if account_existence:
            raise AccountExists()
        else:
            self.mongo_wrapper.insert(self.account_table_name, processed_data)
            message = {
                'is_successful': True,
                'message': 'Account added successfully',
                'account': processed_data
            }
        return message

    def remove_account(self, request_body):
        data = request_body['data']
        required_fields = ['owner_national_id', 'serial']
        check_schema(data, account_definition.account_schema, required_fields)

        account = self.mongo_wrapper.select(self.account_table_name, data)
        if len(account) == 0:
            raise AccountNotFound()
        else:
            self.mongo_wrapper.delete(self.account_table_name, data)
            message = {
                'is_successful': True,
                'message': 'Account removed successfully',
            }
            return message

    def deposit(self, request_body):
        data = request_body['data']
        pass

    def withdraw(self, request_body):
        data = request_body['data']
        pass

    def transfer(self, request_body):
        data = request_body['data']
        pass

    def check_balance(self, request_body):
        data = request_body['data']
        pass

    def select_accounts(self, request_body):
        data = request_body['data']
        pass

    def get_user(self, request_body):
        data = request_body['data']
        pass
