request_schema = {
    'token': {
        '_type': str,
        '_null_value': None,
        'is_required': True
    },
    'method_type': {
        '_type': str,
        '_null_value': None,
        'is_required': True
    },
    'service': {
        '_type': str,
        '_null_value': None,
        'is_required': True
    },
    'action': {
        '_type': str,
        '_null_value': None,
        'is_required': True
    },
    'role_key': {
        '_type': str,
        '_null_value': None,
        'is_required': True
    },
    'data': {
        '_type': dict,
        '_null_value': {},
        'is_required': True
    }
}
