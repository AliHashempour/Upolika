import json

from app.helpers.base_helpers import BaseServiceWrapper, BaseWorker
from app.services.management.management_logic import ManagementLogic


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

        if method_type == "select":
            return self.transaction_select_worker.serve_request(request)
        elif method_type == "insert":
            return self.transaction_insert_worker.serve_request(request)
        elif method_type == "update":
            return self.transaction_update_worker.serve_request(request)
        elif method_type == "delete":
            return self.transaction_delete_worker.serve_request(request)


class ManagementSelectWorker(BaseWorker):
    def __init__(self, logic):
        super(ManagementSelectWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "select_transactions":
            return self.logic.select_transactions(data)

        return data


class ManagementInsertWorker(BaseWorker):
    def __init__(self, logic):
        super(ManagementInsertWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "insert_transaction":
            return self.logic.insert_transaction(data)

        return data


class ManagementUpdateWorker(BaseWorker):
    def __init__(self, logic):
        super(ManagementUpdateWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "update_transaction":
            return self.logic.update_transaction(data)

        return data


class ManagementDeleteWorker(BaseWorker):
    def __init__(self, logic):
        super(ManagementDeleteWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "delete_transaction":
            return self.logic.delete_transaction(data)

        return data
