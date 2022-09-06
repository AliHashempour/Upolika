import json
from pprint import pprint

from app.helpers.base_helpers import BaseWorker, BaseServiceWrapper
from app.services.user import user_logic


class UserWorkerWrapper(BaseServiceWrapper):
    def __init__(self, request_body):
        super().__init__()
        self.request_body = request_body
        self.user_logic = user_logic.UserLogic()
        self.user_select_worker = UserSelectWorker(self.user_logic)

    def wrap(self):
        method_type = self.request_body["method_type"]
        if method_type == "select":
            return self.user_select_worker.serve_request(self.request_body)


class UserSelectWorker(BaseWorker):
    def __init__(self, logic):
        super(UserSelectWorker, self).__init__(logic=logic)

    def serve_request(self, request_body):
        request = json.loads(request_body.decode("utf-8"))
        data = request["data"]
        method = request["method"]
        if method == "select_users":
            return self.logic.select_users(data)

        return data
