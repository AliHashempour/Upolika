import uuid
from app.helpers.base_helpers import BaseLogic
from app.helpers.config_helper import ConfigHelper
from app.helpers.mongo_helper import MongoWrapper
from app.definitions import account_definition, user_definition, transaction_definition
from app.helpers.policy_helper import *


class ManagementLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()
        self.cfg_helper = ConfigHelper()
        self.user_table_name = self.cfg_helper.get_config("USER")["table_name"]
        self.account_table_name = self.cfg_helper.get_config("ACCOUNT")["table_name"]

    def sign_up(self, request_body):
        data = request_body['data']

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

    def login_user(self, request_body):
        data = request_body['data']
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
                'token': user_token,
                'user': record
            }
            return message

    def add_user(self, request_body):
        data = request_body['data']

        check_role(request_body, for_admin=True)
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

    def remove_user(self, request_body):
        data = request_body['data']

        check_role(request_body, for_admin=True)
        check_schema(data, user_definition.user_schema)

        user = self.mongo_wrapper.select(self.user_table_name, data)
        if len(user) == 0:
            raise UserNotFound()
        else:
            acknowledged = self.mongo_wrapper.delete(self.user_table_name, data)
            if acknowledged:
                message = {
                    'is_successful': True,
                    'message': 'User removed successfully',
                }
                return message

    def select_all_users(self, request_body):
        data = request_body['data']

        check_role(request_body, for_admin=True)

        users = self.mongo_wrapper.select(self.user_table_name, data)
        message = {
            'is_successful': True,
            'total_users': len(users),
            'result': users}

        return message

    def add_account(self, request_body):
        data = request_body['data']

        check_role(request_body, for_admin=True)
        check_schema(data, account_definition.account_schema)
        processed_data = preprocess(data, account_definition.account_schema)

        account_existence = self.mongo_wrapper.exists(self.account_table_name, processed_data)

        if account_existence is True:
            raise AccountExists()
        else:
            self.mongo_wrapper.insert(self.account_table_name, processed_data)
            message = {
                'is_successful': True,
                'message': 'Account added successfully',
            }

            return message

    def remove_account(self, request_body):
        data = request_body['data']

        check_role(request_body, for_admin=True)
        check_schema(data, user_definition.user_schema)

        account = self.mongo_wrapper.select(self.account_table_name, data)
        if len(account) == 0:
            raise AccountNotFound()
        else:
            acknowledged = self.mongo_wrapper.delete(self.account_table_name, data)
            if acknowledged:
                message = {
                    'is_successful': True,
                    'message': 'Account removed successfully',
                }
                return message

    def select_all_accounts(self, request_body):
        data = request_body['data']

        check_role(request_body, for_admin=True)

        accounts = self.mongo_wrapper.select(self.account_table_name, data)
        message = {
            'is_successful': True,
            'total_accounts': len(accounts),
            'result': accounts}

        return message

    def find_account(self, request_body):
        data = request_body['data']
        required_fields = ['serial_number']
        check_role(request_body, for_admin=True)
        check_schema(data, account_definition.account_schema, required_fields)

        acc = self.mongo_wrapper.select(self.account_table_name, data)
        if len(acc) == 0:
            raise AccountNotFound()
        else:
            message = {
                'is_successful': True,
                'message': 'Account found successfully',
                'account': acc[0]
            }
            return message

    def update_user(self, request_body):
        data = request_body['data']
        national_id = data['national_id']

        check_role(request_body, for_admin=True)
        check_schema(data, user_definition.user_schema)
        preprocessed_data = preprocess(data, user_definition.user_schema)

        user = self.mongo_wrapper.select(self.user_table_name, {'national_id': national_id})
        if len(user) == 0:
            raise UserNotFound()
        else:
            acknowledged = self.mongo_wrapper.update(self.user_table_name,
                                                     {'national_id': national_id},
                                                     preprocessed_data)
            if acknowledged:
                message = {
                    'is_successful': True,
                    'message': 'User updated successfully',
                }
                return message
