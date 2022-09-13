from app.definitions import account_definition, transaction_definition
from app.helpers.base_helpers import BaseLogic
from app.helpers.config_helper import ConfigHelper
from app.helpers.mongo_helper import MongoWrapper
from app.helpers.policy_helper import *


class AccountLogic(BaseLogic):
    def __init__(self):
        super().__init__()
        self.mongo_wrapper = MongoWrapper()
        self.cfg_helper = ConfigHelper()
        self.account_table_name = self.cfg_helper.get_config("ACCOUNT")["table_name"]

    def update_balance(self, request_body):
        data = request_body['data']
        required_fields = ['owner_national_id', 'serial', 'amount']
        check_schema(data, account_definition.account_schema, required_fields)

        res = self.mongo_wrapper.select(self.account_table_name, {'owner_national_id': data['owner_national_id'],
                                                                  'serial': data['serial']})
        if len(res) == 0:
            raise AccountNotFound()
        else:
            account = res[0]
            account['balance'] = data['amount']
            self.mongo_wrapper.update(self.account_table_name, {
                'owner_national_id': data['owner_national_id'],
                'serial': data['serial']}, account)

            message = {
                'is_successful': True,
                'message': 'Balance updated successfully',
                'account': account
            }
            return message

    def add_transaction(self, request_body):
        data = request_body['data']
        check_schema(data, transaction_definition.transaction_schema)
        processed_data = preprocess(data, transaction_definition.transaction_schema)

        account = self.mongo_wrapper.select(self.account_table_name,
                                            {'serial': processed_data['owner_account_serial']})
        account = account[0]
        account_transactions = account['transaction_list']
        account_transactions.append(processed_data)
        account['transaction_list'] = account_transactions

        self.mongo_wrapper.update(self.account_table_name, {'serial': processed_data['owner_account_serial']}, account)
        message = {
            'is_successful': True,
            'message': 'Transaction added successfully',
            'transaction': processed_data
        }
        return message

    def get_transactions(self, request_body):
        data = request_body['data']
        required_fields = ['owner_national_id', 'serial']
        check_schema(data, account_definition.account_schema, required_fields)

        res = self.mongo_wrapper.select(self.account_table_name, {
            'serial': data['serial'], 'owner_national_id': data['owner_national_id']})
        account = res[0]
        transactions = account['transaction_list']
        message = {
            'is_successful': True,
            'message': 'Transactions retrieved successfully',
            'total_transactions': len(transactions),
            'transactions': transactions
        }
        return message

    def get_account(self, request_body):
        data = request_body['data']
        required_fields = ['owner_national_id', 'serial']
        check_schema(data, account_definition.account_schema, required_fields)

        res = self.mongo_wrapper.select(self.account_table_name, {
            'serial': data['serial'], 'owner_national_id': data['owner_national_id']})
        if len(res) == 0:
            raise AccountNotFound()
        else:
            account = res[0]
            message = {
                'is_successful': True,
                'message': 'Account retrieved successfully',
                'account': account
            }
            return message
