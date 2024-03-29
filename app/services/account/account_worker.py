import json

from app.helpers.base_helpers import BaseServiceWrapper, BaseWorker
from app.services.account.account_logic import AccountLogic
from app.helpers.policy_helper import *


class AccountWorkerWrapper(BaseServiceWrapper):
    def __init__(self):
        super().__init__()

        self.account_logic = AccountLogic()
        self.account_select_worker = AccountSelectWorker(self.account_logic)
        self.account_insert_worker = AccountInsertWorker(self.account_logic)
        self.account_update_worker = AccountUpdateWorker(self.account_logic)
        self.account_delete_worker = AccountDeleteWorker(self.account_logic)

    def wrap(self, request_body):
        request = json.loads(request_body.decode("utf-8"))
        method_type = request["method_type"]

        try:
            if method_type == "select":
                return self.account_select_worker.serve_request(request)
            elif method_type == "insert":
                return self.account_insert_worker.serve_request(request)
            elif method_type == "update":
                return self.account_update_worker.serve_request(request)
            elif method_type == "delete":
                return self.account_delete_worker.serve_request(request)

        except AccountExists as e:
            return {'is_successful': False, 'error': 'Account Exists', 'error_description': str(e)}
        except AccountNotFound as e:
            return {'is_successful': False, 'error': 'Account Not Found', 'error_description': str(e)}
        except UserNotFound as e:
            return {'is_successful': False, 'error': 'User Not Found', 'error_description': str(e)}
        except InvalidFieldName as e:
            return {'is_successful': False, 'error': 'Invalid Field Name', 'error_description': str(e)}
        except RequiredFieldError as e:
            return {'is_successful': False, 'error': 'Required Field Error', 'error_description': str(e)}
        except AppException as e:
            return {'is_successful': False, 'error': 'App Exception', 'error_description': str(e)}
        except Exception as e:
            return {'is_successful': False, 'error': 'Exception', 'error_description': str(e)}


class AccountSelectWorker(BaseWorker):
    def __init__(self, logic):
        super(AccountSelectWorker, self).__init__(logic=logic)

    def serve_request(self, request):

        method = request["action"]
        if method == "get_transactions":
            return self.logic.get_transactions(request)
        elif method == "get_account":
            return self.logic.get_account(request)
        else:
            raise InvalidFieldName('action')


class AccountInsertWorker(BaseWorker):
    def __init__(self, logic):
        super(AccountInsertWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        method = request["action"]
        if method == "add_transaction":
            return self.logic.add_transaction(request)
        else:
            raise InvalidFieldName('action')


class AccountUpdateWorker(BaseWorker):
    def __init__(self, logic):
        super(AccountUpdateWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        method = request["action"]
        if method == "update_balance":
            return self.logic.update_balance(request)
        else:
            raise InvalidFieldName('action')


class AccountDeleteWorker(BaseWorker):
    def __init__(self, logic):
        super(AccountDeleteWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        method = request["action"]
        if method == "delete_account":
            return self.logic.delete_account(request)
        else:
            raise InvalidFieldName('action')
