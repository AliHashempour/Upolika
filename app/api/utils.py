import datetime

from app.helpers import mongo_helper


def index_user(data: dict):
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    national_id = data.get("national_id")
    password = data.get("password")

    user_info = {
        'first_name': first_name,
        'last_name': last_name,
        'national_id': national_id,
        'password': password,
        'category': 'USER',
        'created_at': datetime.datetime.now(),
    }
    mongo_wrapper = mongo_helper.MongoWrapper()

    if (mongo_wrapper.exists('users', {'national_id': national_id})) is False:
        insertion_id = mongo_wrapper.insert('users', user_info)
        return {'is_inserted': True}
    else:
        duplicate_user_error = {'is_inserted': False}
        return duplicate_user_error
