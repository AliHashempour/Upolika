from app.exceptions.general_exception import *
from app.helpers.config_helper import ConfigHelper


def check_schema(data, schema, required_fields=None):
    invalid_field_name = None

    if required_fields is None:
        check_is_required(data, schema)

        for field in data.keys():
            if field not in schema.keys():
                invalid_field_name = field

        if invalid_field_name is not None:
            raise InvalidFieldName(invalid_field_name)

    else:
        for key in required_fields:
            if key not in data.keys():
                raise RequiredFieldError(key)

        for field in list(data.keys()).copy():
            if field not in required_fields:
                del data[field]


def check_is_required(data, schema):
    for key, value in schema.items():
        if value['is_required'] is True and key not in data.keys():
            raise RequiredFieldError(key)


def preprocess(data, schema):
    for field in schema.keys():
        if field not in data.keys():
            data[field] = None

    for field in data:
        if data[field] is None and field in schema.keys() and "_null_value" in schema[field].keys():
            data[field] = schema[field]["_null_value"]
        if field in schema.keys() and "_type" in schema[field].keys() and schema[field]["_null_value"] is not None:
            data[field] = schema[field]["_type"](data[field])
    for field in list(data.keys()).copy():
        if data[field] is None:
            del data[field]

    return data


def field_is_empty(field, _field_name, schema):
    if field is None or field == "" or field == schema[_field_name]["_null_value"]:
        return True
    else:
        return False


def check_role(request_body, for_admin=False):
    role_key = request_body['role_key']

    cfg_helper = ConfigHelper()
    admin_key = cfg_helper.get('ROLES_KEY', 'admin_key')
    user_key = cfg_helper.get('ROLES_KEY', 'user_key')

    if for_admin is True:
        if role_key != admin_key:
            raise PermissionDenied('admin')
    elif for_admin is False:
        if role_key != user_key:
            raise PermissionDenied('user')
