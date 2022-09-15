import datetime

from app.helpers import mongo_helper, config_helper
from app.exceptions.api_exception import *
from app.helpers.redis_helper import RedisWrapper


def check_token(request_body):
    token = request_body["token"]

    redis_helper = RedisWrapper()
    if token is None or not redis_helper.exists(token):
        raise NotAuthorized()


def check_tag(request_body):
    index = request_body["service"]
    cfg_helper = config_helper.ConfigHelper()

    config_key = index.upper()
    if not cfg_helper.has_tag(config_key):
        raise InvalidInput("SERVICE", index)


def cache_token(token, ip):
    redis_helper = RedisWrapper()
    redis_helper.set(token, ip)
