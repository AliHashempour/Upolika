account_schema = {
    "owner_first_name": {
        "_type": str,
        "_null_value": None,
        'is_required': False
    },
    "owner_last_name": {
        "_type": str,
        "_null_value": None,
        'is_required': False
    },
    "owner_national_id": {
        "_type": str,
        "_null_value": None,
        'is_required': True
    },
    "type": {
        "_type": str,
        "_null_value": 'amassed',
        'is_required': True
    },
    "serial": {
        "_type": str,
        "_null_value": None,
        'is_required': True
    },
    "balance": {
        "_type": float,
        "_null_value": 1000.0,
        'is_required': True
    },
    'transaction_list': {
        "_type": list,
        "_null_value": [],
        'is_required': False
    }
}
