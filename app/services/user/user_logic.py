import datetime

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
        required_fields = ['owner_national_id', 'serial', 'amount']
        check_schema(data, account_definition.account_schema, required_fields)

        res = self.mongo_wrapper.select(self.account_table_name, {'owner_national_id': data['owner_national_id'],
                                                                  'serial': data['serial']})
        if len(res) == 0:
            raise AccountNotFound()
        else:
            account = res[0]
            account['balance'] += data['amount']

            account['transaction_list'] = self.add_transaction(account, data, 'deposit')

            self.mongo_wrapper.update(self.account_table_name, {'owner_national_id': data['owner_national_id'],
                                                                'serial': data['serial']}, account)
            message = {
                'is_successful': True,
                'message': 'Deposit successful',
            }
            return message

    def withdraw(self, request_body):
        data = request_body['data']
        required_fields = ['owner_national_id', 'serial', 'amount']
        check_schema(data, account_definition.account_schema, required_fields)

        res = self.mongo_wrapper.select(self.account_table_name, {'owner_national_id': data['owner_national_id'],
                                                                  'serial': data['serial']})
        if len(res) == 0:
            raise AccountNotFound()
        else:
            account = res[0]
            if data['amount'] > account['balance']:
                raise InsufficientBalance()

            account['balance'] -= data['amount']
            account['transaction_list'] = self.add_transaction(account, data, 'withdraw')

            self.mongo_wrapper.update(self.account_table_name, {'owner_national_id': data['owner_national_id'],
                                                                'serial': data['serial']}, account)
            message = {
                'is_successful': True,
                'message': 'Withdraw successful',
            }
            return message

    def transfer(self, request_body):
        data = request_body['data']
        required_fields = ['src_account_serial', 'dst_account_serial', 'amount']
        check_schema(data, account_definition.account_schema, required_fields)

        src_account = self.mongo_wrapper.select(self.account_table_name, {'serial': data['src_account_serial']})
        dst_account = self.mongo_wrapper.select(self.account_table_name, {'serial': data['dst_account_serial']})
        if len(src_account) == 0 or len(dst_account) == 0:
            raise AccountNotFound()
        else:
            src_account = src_account[0]
            dst_account = dst_account[0]
            if data['amount'] > src_account['balance']:
                raise InsufficientBalance()

            src_account['balance'] -= data['amount']
            dst_account['balance'] += data['amount']
            src_account['transaction_list'] = self.add_transaction(src_account, data, 'withdraw')
            dst_account['transaction_list'] = self.add_transaction(dst_account, data, 'deposit')

            self.mongo_wrapper.update(self.account_table_name, {'serial': data['src_account_serial']}, src_account)
            self.mongo_wrapper.update(self.account_table_name, {'serial': data['dst_account_serial']}, dst_account)
            message = {
                'is_successful': True,
                'message': 'Transfer successful',
            }
            return message

    def check_balance(self, request_body):
        data = request_body['data']
        pass

    def select_accounts(self, request_body):
        data = request_body['data']
        pass

    def get_user(self, request_body):
        data = request_body['data']
        pass

    @staticmethod
    def add_transaction(account, data, transaction_type):
        account_transactions = account['transaction_list']
        transaction_record = {
            'amount': data['amount'],
            'owner_account_serial': data['serial'],
            'transaction_type': transaction_type,
            'transaction_date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        account_transactions.append(transaction_record)
        return account_transactions
