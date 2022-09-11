import uuid
from app.helpers.base_helpers import BaseLogic
from app.helpers.config_helper import ConfigHelper
from app.helpers.mongo_helper import MongoWrapper
from app.definitions import account_definition, user_definition, transaction_definition
from app.helpers.schema_helper import *


class ManagementLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()
        self.cfg_helper = ConfigHelper()
        self.user_table_name = self.cfg_helper.get_config("USER")["table_name"]

    def sign_up(self, data):
        check_schema(data, user_definition.user_schema)
        processed_data = preprocess(data, user_definition.user_schema)

        user_existence = self.mongo_wrapper.exists(self.user_table_name, processed_data)

        if user_existence:
            raise UserExists()
        else:
            self.mongo_wrapper.insert(self.user_table_name, processed_data)

            message = {
                'is_successful': True,
                'message': 'User added successfully',
            }
        return message

    def login_user(self, data):
        required_fields = ['username', 'password']

        check_schema(data, user_definition.user_schema, required_fields)
        processed_data = preprocess(data, user_definition.user_schema)

        record = self.mongo_wrapper.select(self.user_table_name, processed_data)
        if len(record) == 0:
            raise InvalidUser()
        else:
            user_token = str(uuid.uuid4())  # todo set user token in redis in api
            message = {
                'is_successful': True,
                'message': 'User logged in successfully',
                'token': user_token
            }
            return message

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
