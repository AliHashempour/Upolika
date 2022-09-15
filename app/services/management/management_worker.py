import json

from app.helpers.base_helpers import BaseServiceWrapper, BaseWorker
from app.services.management.management_logic import ManagementLogic
from app.exceptions.general_exception import *


class ManagementWorkerWrapper(BaseServiceWrapper):
    def __init__(self):
        super().__init__()

        self.transaction_logic = ManagementLogic()
        self.transaction_select_worker = ManagementSelectWorker(self.transaction_logic)
        self.transaction_insert_worker = ManagementInsertWorker(self.transaction_logic)
        self.transaction_update_worker = ManagementUpdateWorker(self.transaction_logic)
        self.transaction_delete_worker = ManagementDeleteWorker(self.transaction_logic)

    def wrap(self, request_body):
        request = json.loads(request_body.decode("utf-8"))
        method_type = request["method_type"]

        try:
            if method_type == "select":
                return self.transaction_select_worker.serve_request(request)
            elif method_type == "insert":
                return self.transaction_insert_worker.serve_request(request)
            elif method_type == "update":
                return self.transaction_update_worker.serve_request(request)
            elif method_type == "delete":
                return self.transaction_delete_worker.serve_request(request)

        except UserExists as e:
            return {'is_successful': False, 'error': 'User Exists', 'error_description': str(e)}
        except UserNotFound as e:
            return {'is_successful': False, 'error': 'User not found', 'error_description': str(e)}
        except AccountExists as e:
            return {'is_successful': False, 'error': 'Account Exists', 'error_description': str(e)}
        except AccountNotFound as e:
            return {'is_successful': False, 'error': 'Account not found', 'error_description': str(e)}
        except InvalidFieldName as e:
            return {'is_successful': False, 'error': 'Invalid Field Name', 'error_description': str(e)}
        except RequiredFieldError as e:
            return {'is_successful': False, 'error': 'Required Field Error', 'error_description': str(e)}
        except PermissionDenied as e:
            return {'is_successful': False, 'error': 'Permission Denied', 'error_description': str(e)}
        except AppException as e:
            return {'is_successful': False, 'error': 'App Exception', 'error_description': str(e)}
        except Exception as e:
            return {'is_successful': False, 'error': 'Exception', 'error_description': str(e)}


class ManagementSelectWorker(BaseWorker):
    def __init__(self, logic):
        super(ManagementSelectWorker, self).__init__(logic=logic)

    def serve_request(self, request):

        method = request["action"]

        if method == "login":
            return self.logic.login_user(request)
        elif method == "select_all_users":
            return self.logic.select_all_users(request)
        elif method == "select_all_accounts":
            return self.logic.select_all_accounts(request)
        elif method == "find_account":
            return self.logic.find_account(request)
        else:
            raise InvalidFieldName('action')


class ManagementInsertWorker(BaseWorker):
    def __init__(self, logic):
        super(ManagementInsertWorker, self).__init__(logic=logic)

    def serve_request(self, request):

        method = request["action"]

        if method == "sign_up":
            return self.logic.sign_up(request)
        elif method == "add_user":
            return self.logic.add_user(request)
        elif method == "add_account":
            return self.logic.add_account(request)
        else:
            raise InvalidFieldName('action')


class ManagementUpdateWorker(BaseWorker):
    def __init__(self, logic):
        super(ManagementUpdateWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        method = request["action"]

        if method == "update_user":
            return self.logic.update_user(request)
        else:
            raise InvalidFieldName('action')


class ManagementDeleteWorker(BaseWorker):
    def __init__(self, logic):
        super(ManagementDeleteWorker, self).__init__(logic=logic)

    def serve_request(self, request):

        method = request["action"]

        if method == "delete_user":
            return self.logic.delete_user(request)
        elif method == "delete_account":
            return self.logic.delete_account(request)
        else:
            raise InvalidFieldName('action')
