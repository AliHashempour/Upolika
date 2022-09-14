import datetime

from app.helpers import mongo_helper, config_helper
from app.exceptions.api_exception import *
from app.helpers.redis_helper import RedisWrapper


def check_token(request_body):
    token = request_body["token"]

    redis_helper = RedisWrapper()
    token_existence = redis_helper.exists(token)
    if not token_existence:
        raise NotAuthorizedException()


def check_tag(request_body):
    index = request_body["service"]
    cfg_helper = config_helper.ConfigHelper()

    config_key = index.upper()
    if not cfg_helper.has_tag(config_key):
        raise InvalidInputException("SERVICE", index)


def cache_token(token, ip):
    redis_helper = RedisWrapper()
    redis_helper.set(token, ip)
