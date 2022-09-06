from abc import abstractmethod


class BaseMongoWrapper:
    def __init__(self):
        """config of database """

    @abstractmethod
    def create_table(self, table_name: str, schema: str):
        """creating table """

    @abstractmethod
    def insert(self, table_name: str, record: dict):
        """insert data to the table"""

    @abstractmethod
    def select(self, table_name: str, query):
        """select data from data base"""

    def update(self, table_name: str, _id, doc: dict):
        """updating record"""

    def delete(self, table_name: str, _id, doc: dict):
        """deleting record"""


class BaseRedisWrapper:
    def __init__(self):
        """"redis config"""

    def get(self, key):
        pass

    def set(self, key, value):
        pass

    def delete(self, key):
        pass

    def exists(self, key):
        pass

    def get_all_keys(self):
        pass

    def get_all_values(self):
        pass

    def get_all_items(self):
        pass

    def get_all_items_as_dict(self):
        pass

    def flush(self):
        pass

    def get_all_keys_as_list(self):
        pass

    def get_all_values_as_list(self):
        pass

    def get_all_items_as_list(self):
        pass

    def get_all_items_as_dict_as_list(self):
        pass


class BaseWorker:
    def serve_request(self, request_body):
        pass
