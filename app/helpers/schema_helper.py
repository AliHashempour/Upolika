from app.exceptions.general_exception import *


def check_schema(data, schema, required_fields=None):
    invalid_field_name = None

    for field in data.keys():
        if field not in schema.keys():
            invalid_field_name = field

    if invalid_field_name is not None:
        raise InvalidFieldName(invalid_field_name)

    if required_fields is None:
        check_is_required(data, schema)
    else:
        for key in required_fields:
            if key not in data.keys():
                raise RequiredFieldError(key)


def check_is_required(data, schema):
    for key, value in schema.items():
        if value['is_required'] is True and key not in data.keys():
            raise RequiredFieldError(key)


def check_full_schema(data, schema):
    schema_keys = set(schema.keys())

    data_keys = set(data.keys())

    extra_keys = data_keys - schema_keys
    if len(extra_keys) > 0:
        for k in list(extra_keys):
            del data[k]

    if len(schema_keys - data_keys) > 0:
        for null_key in list(schema_keys - data_keys):
            data[null_key] = None

    return data


def preprocess(data, schema):
    for field in data:
        if data[field] is None and field in schema.keys() and "_null_value" in schema[field].keys():
            data[field] = schema[field]["_null_value"]
        if field in schema.keys() and "_type" in schema[field].keys():
            data[field] = schema[field]["_type"](data[field])
    return data


def field_is_empty(field, _field_name, schema):
    if field is None or field == "" or field == schema[_field_name]["_null_value"]:
        return True
    else:
        return False
