import json

from app.helpers.base_helpers import BaseServiceWrapper, BaseWorker
from app.services.account.account_logic import AccountLogic


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

        if method_type == "select":
            return self.account_select_worker.serve_request(request)
        elif method_type == "insert":
            return self.account_insert_worker.serve_request(request)
        elif method_type == "update":
            return self.account_update_worker.serve_request(request)
        elif method_type == "delete":
            return self.account_delete_worker.serve_request(request)


class AccountSelectWorker(BaseWorker):
    def __init__(self, logic):
        super(AccountSelectWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "get_transactions":
            return self.logic.get_transactions(data)
        elif method == "get_account":
            return self.logic.get_account(data)

        return data


class AccountInsertWorker(BaseWorker):
    def __init__(self, logic):
        super(AccountInsertWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "add_transaction":
            return self.logic.add_transaction(data)

        return data


class AccountUpdateWorker(BaseWorker):
    def __init__(self, logic):
        super(AccountUpdateWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "update_balance":
            return self.logic.update_balance(data)

        return data


class AccountDeleteWorker(BaseWorker):
    def __init__(self, logic):
        super(AccountDeleteWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "delete_account":
            return self.logic.delete_account(data)

        return data
