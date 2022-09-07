import json

from app.helpers.base_helpers import BaseWorker, BaseServiceWrapper
from app.services.user.user_logic import UserLogic


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

        if method_type == "select":
            return self.user_select_worker.serve_request(request)
        elif method_type == "insert":
            return self.user_insert_worker.serve_request(request)
        elif method_type == "update":
            return self.user_update_worker.serve_request(request)
        elif method_type == "delete":
            return self.user_delete_worker.serve_request(request)


class UserSelectWorker(BaseWorker):
    def __init__(self, logic):
        super(UserSelectWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "select_users":
            return self.logic.select_users(data)

        return data


class UserInsertWorker(BaseWorker):
    def __init__(self, logic):
        super(UserInsertWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "insert_user":
            return self.logic.insert_user(data)

        return data


class UserUpdateWorker(BaseWorker):
    def __init__(self, logic):
        super(UserUpdateWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "update_user":
            return self.logic.update_user(data)

        return data


class UserDeleteWorker(BaseWorker):
    def __init__(self, logic):
        super(UserDeleteWorker, self).__init__(logic=logic)

    def serve_request(self, request):
        data = request["data"]
        method = request["method"]
        if method == "delete_user":
            return self.logic.delete_user(data)

        return data