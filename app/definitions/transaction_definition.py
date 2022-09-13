import datetime

transaction_schema = {
    "amount": {
        "_type": float,
        "_null_value": 0,
        'is_required': True
    },
    "owner_account_serial": {
        "_type": str,
        "_null_value": None,
        'is_required': True
    },
    "transaction_type": {
        "_type": str,
        "_null_value": None,
        'is_required': True
    },
    "transaction_date": {
        "_type": str,
        "_null_value": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'is_required': True
    }
}
