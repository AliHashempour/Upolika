import json

from app.helpers.base_helpers import BaseServiceWrapper, BaseWorker
from app.services.transaction.transaction_logic import TransactionLogic


class TransactionWorkerWrapper(BaseServiceWrapper):
    def __init__(self):
        super().__init__()

        self.transaction_logic = TransactionLogic()
        self.transaction_select_worker = TransactionSelectWorker(self.transaction_logic)
        self.transaction_insert_worker = TransactionInsertWorker(self.transaction_logic)
        self.transaction_update_worker = TransactionUpdateWorker(self.transaction_logic)
        self.transaction_delete_worker = TransactionDeleteWorker(self.transaction_logic)

    def wrap(self, request_body):
        request = json.loads(request_body.decode("utf-8"))
        method_type = request["method_type"]

        if method_type == "select":
            return self.transaction_select_worker.serve_request(request)
        elif method_type == "insert":
            return self.transaction_insert_worker.serve_request(request)
        elif method_type == "update":
            return self.transaction_update_worker.serve_request(request)
        elif method_type == "delete":
            return self.transaction_delete_worker.serve_request(request)


class TransactionSelectWorker(BaseWorker):
    def __init__(self, logic):
        super(TransactionSelectWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "select_transactions":
            return self.logic.select_transactions(data)

        return data


class TransactionInsertWorker(BaseWorker):
    def __init__(self, logic):
        super(TransactionInsertWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "insert_transaction":
            return self.logic.insert_transaction(data)

        return data


class TransactionUpdateWorker(BaseWorker):
    def __init__(self, logic):
        super(TransactionUpdateWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "update_transaction":
            return self.logic.update_transaction(data)

        return data


class TransactionDeleteWorker(BaseWorker):
    def __init__(self, logic):
        super(TransactionDeleteWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "delete_transaction":
            return self.logic.delete_transaction(data)

        return data
