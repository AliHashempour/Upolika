from abc import abstractmethod, ABC


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


class BaseRedisWrapper(ABC):
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


class BaseWorker:
    def serve_request(self, request_body):
        pass
