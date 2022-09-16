#!/bin/bash
# shellcheck disable=SC2155
# shellcheck disable=SC2006
export PYTHONPATH=`pwd`
flask run &
python ./app/listeners/management_listener.py &
python ./app/listeners/user_listener.py &
python ./app/listeners/account_listener.py
