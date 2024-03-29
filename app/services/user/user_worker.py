import json

from app.helpers.base_helpers import BaseWorker, BaseServiceWrapper
from app.services.user.user_logic import UserLogic
from app.exceptions.general_exception import *


class UserWorkerWrapper(BaseServiceWrapper):
    def __init__(self):
        super().__init__()

        self.user_logic = UserLogic()
        self.user_select_worker = UserSelectWorker(self.user_logic)
        self.user_insert_worker = UserInsertWorker(self.user_logic)
        self.user_update_worker = UserUpdateWorker(self.user_logic)
        self.user_delete_worker = UserDeleteWorker(self.user_logic)

    def wrap(self, request_body):
        request = json.loads(request_body.decode("utf-8"))
        method_type = request["method_type"]

        try:
            if method_type == "select":
                return self.user_select_worker.serve_request(request)
            elif method_type == "insert":
                return self.user_insert_worker.serve_request(request)
            elif method_type == "update":
                return self.user_update_worker.serve_request(request)
            elif method_type == "delete":
                return self.user_delete_worker.serve_request(request)

        except AccountExists as e:
            return {'is_successful': False, 'error': 'Account Exists', 'error_description': str(e)}
        except AccountNotFound as e:
            return {'is_successful': False, 'error': 'Account not found', 'error_description': str(e)}
        except InsufficientBalance as e:
            return {'is_successful': False, 'error': 'Insufficient Balance', 'error_description': str(e)}
        except UserNotFound as e:
            return {'is_successful': False, 'error': 'User not found', 'error_description': str(e)}
        except InvalidFieldName as e:
            return {'is_successful': False, 'error': 'Invalid Field Name', 'error_description': str(e)}
        except RequiredFieldError as e:
            return {'is_successful': False, 'error': 'Required Field Error', 'error_description': str(e)}
        except AppException as e:
            return {'is_successful': False, 'error': 'App Exception', 'error_description': str(e)}
        except Exception as e:
            return {'is_successful': False, 'error': 'Exception', 'error_description': str(e)}


class UserSelectWorker(BaseWorker):
    def __init__(self, logic):
        super(UserSelectWorker, self).__init__(logic=logic)

    def serve_request(self, request):

        method = request["action"]
        if method == "check_balance":
            return self.logic.check_balance(request)
        elif method == "select_accounts":
            return self.logic.select_accounts(request)
        elif method == "get_user":
            return self.logic.get_user(request)
        else:
            raise InvalidFieldName('action')


class UserInsertWorker(BaseWorker):
    def __init__(self, logic):
        super(UserInsertWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        method = request["action"]
        if method == "add_account":
            return self.logic.add_account(request)
        else:
            raise InvalidFieldName('action')


class UserUpdateWorker(BaseWorker):
    def __init__(self, logic):
        super(UserUpdateWorker, self).__init__(logic=logic)

    def serve_request(self, request):

        method = request["action"]
        if method == "deposit":
            return self.logic.deposit(request)
        elif method == "withdraw":
            return self.logic.withdraw(request)
        elif method == "transfer":
            return self.logic.transfer(request)
        else:
            raise InvalidFieldName('action')


class UserDeleteWorker(BaseWorker):
    def __init__(self, logic):
        super(UserDeleteWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        method = request["action"]
        if method == "remove_account":
            return self.logic.remove_account(request)
        else:
            raise InvalidFieldName('action')
