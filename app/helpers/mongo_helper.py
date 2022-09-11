from dataclasses import dataclass
from abc import abstractmethod

from pymongo import MongoClient

from app.helpers.base_helpers import BaseMongoWrapper
from app.helpers.config_helper import ConfigHelper


class MongoConfig:
    def __init__(self):
        """config of database such as host name , port and etc"""
        super(MongoConfig, self).__init__()
        self.cfg_helper = ConfigHelper()
        ips = self.cfg_helper.get("MONGODB", "host").split(',')[0]
        port = self.cfg_helper.get("MONGODB", "port").split(',')[0]
        self.client_conf = "mongodb://{}:{}/".format(ips, port)
        self.database_name = self.cfg_helper.get("MONGODB", "database_name")


class MongoWrapper(BaseMongoWrapper):
    def __init__(self):
        super(MongoWrapper, self).__init__()
        self.conf = MongoConfig()
        self.client = MongoClient(self.conf.client_conf)
        self.db_connection = self.client[self.conf.database_name]

    def create_table(self, table_name: str, schema: str):
        collection = self.get_collection(table_name)
        return collection

    def insert(self, table_name: str, record: dict):
        collection = self.get_collection(table_name)
        res = collection.insert_one(record)
        return str(res.inserted_id)

    def select(self, table_name: str, query: dict, sort: list = None):
        collection = self.get_collection(table_name)
        if sort is None:
            res = collection.find(query)
        else:
            res = collection.find(query).sort(sort[0], sort[1])
        return [*res]

    def update(self, table_name, _id, doc):
        collection = self.get_collection(table_name)
        doc = {"$set": doc}
        query = {"id": _id}
        res = collection.update_one(query, doc)
        return res

    def delete(self, table_name, _id, doc):
        collection = self.get_collection(table_name)
        doc = {"$set": doc}
        query = {"id": _id}
        res = collection.delete_one(query, doc)
        return res

    def get_collection(self, table_name):
        collection = self.db_connection[table_name]
        return collection

    def connect(self):
        self.client = MongoClient(self.conf.client_conf)
        self.db_connection = self.client[self.conf.database_name]

    def is_duplicate(self, table_name, query):
        collection = self.get_collection(table_name)
        res = collection.find(query)
        res = [*res]
        if len(res) > 0:
            return True
        return False

    def update_by_query(self, table_name, query: dict, doc: dict):
        collection = self.get_collection(table_name)
        doc = {"$set": doc}
        res = collection.update_one(query, doc)
        return res

    def upsert(self, table_name, query: dict, doc: dict):
        collection = self.get_collection(table_name)
        res = collection.update_one(query, {"$set": doc}, upsert=True)
        return res

    def exists(self, table_name, query: dict):
        collection = self.get_collection(table_name)
        res = collection.find_one(query)
        if res is None:
            return False
        return True
