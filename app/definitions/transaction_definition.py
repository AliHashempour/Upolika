transaction_schema = {
    "amount": {"_type": float, "_null_value": 0, 'is_required': True},
    "owner_account_serial": {"_type": str, "_null_value": None, 'is_required': True},
    "transaction_type": {"_type": str, "_null_value": None, 'is_required': True},
    "transaction_date": {"_type": str, "_null_value": "1970/01/01 00:00:00.000000", 'is_required': True}
}
