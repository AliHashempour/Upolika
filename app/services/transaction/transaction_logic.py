from app.helpers.base_helpers import BaseLogic


class TransactionLogic(BaseLogic):
    def __init__(self):
        super().__init__()

    def select_transactions(self, data):
        return data
