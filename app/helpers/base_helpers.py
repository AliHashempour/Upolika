from abc import abstractmethod


class DBConfig:
    def __init__(self):
        """config of database such as host name , port and etc"""


class BaseWrapper:
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
