import redis

from app.helpers.base_helpers import BaseRedisWrapper
from app.helpers.config_helper import ConfigHelper


class RedisConfig:
    def __init__(self):
        """config of database such as host name , port and etc"""
        self.cfg_helper = ConfigHelper()
        ips = self.cfg_helper.get("REDIS", "host").split(',')[0]
        port = self.cfg_helper.get("REDIS", "port").split(',')[0]
        self.redis_conn = redis.Redis(host=ips, port=port, db=0)


class RedisWrapper(BaseRedisWrapper):

    def __init__(self):
        super().__init__()
        self.conf = RedisConfig()
        self.redis_client = self.conf.redis_conn

    def get(self, key):
        return self.redis_client.get(key)

    def set(self, key, value):
        return self.redis_client.set(key, value)

    def delete(self, key):
        return self.redis_client.delete(key)

    def exists(self, key):
        return self.redis_client.exists(key)

    def get_all_keys(self):
        return self.redis_client.keys()

    def get_all_values(self):
        return self.redis_client.mget(self.get_all_keys())

    def get_all_items(self):
        return self.redis_client.mget(self.get_all_keys())

    def get_all_items_as_dict(self):
        return dict(zip(self.get_all_keys(), self.get_all_values()))

    def flush(self):
        return self.redis_client.flushdb()

    def get_all_keys_as_list(self):
        return [x.decode('utf-8') for x in self.get_all_keys()]

    def get_all_values_as_list(self):
        return [x.decode('utf-8') for x in self.get_all_values()]

    def get_all_items_as_list(self):
        return [x.decode('utf-8') for x in self.get_all_items()]

    def get_all_items_as_dict_as_list(self):
        return [x.decode('utf-8') for x in self.get_all_items_as_dict()]
