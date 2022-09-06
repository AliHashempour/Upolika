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

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def exists(self, key):
        pass


class BaseLogic:
    def __init__(self):
        pass


class BaseWorker:
    def __init__(self, logic):
        self.logic = logic

    @abstractmethod
    def serve_request(self, request_body):
        pass


class BaseServiceWrapper:
    def __init__(self):
        pass

    @abstractmethod
    def wrap(self):
        pass
