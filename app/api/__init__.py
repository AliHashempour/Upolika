from flask import Flask, request
from flask_cors import CORS
import app.api.utils as utils
from app.helpers import communication_helper
from app.exceptions.api_exception import *

app = Flask(__name__)
CORS(app)


def execute_request(request_body):
    permitted_methods = ['sign_up', 'login']

    if request_body['method'] not in permitted_methods:
        utils.check_token(request_body)

    utils.check_tag(request_body)

    response = communication_helper.send_message(
        table=request_body['table'],
        body=request_body)

    return response


@app.route('/api/v1/select_request', methods=['post'])
def select_request():
    try:
        request_body = request.json
        res = execute_request(request.json)
        return {
            "is_successful": True,
            "error_description": None,
            "data": request_body['data'],
            "response": res
        }
    except NotAuthorizedException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}
    except InvalidInputException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}


@app.route('/api/v1/insert_request', methods=['post'])
def insert_request():
    try:
        return {
            "is_successful": True,
            "error_description": None,
            "data": None,
            "request": request.json
        }
    except NotAuthorizedException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}
    except InvalidInputException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}


@app.route('/api/v1/update_request', methods=['post'])
def update_request():
    try:
        return {
            "is_successful": True,
            "error_description": None,
            "data": None,
            "request": request.json
        }
    except NotAuthorizedException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}
    except InvalidInputException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}


@app.route('/api/v1/delete_request', methods=['post'])
def delete_request():
    try:
        return {
            "is_successful": True,
            "error_description": None,
            "data": None,
            "request": request.json
        }
    except NotAuthorizedException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}
    except InvalidInputException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}


@app.route('/api/v1/sign_up', methods=['post'])
def sign_up():
    request_body = request.json
    data = request_body['data']
    request_body['table'] = 'management'
    request_body['method'] = 'insert'
    request_body['method_type'] = 'sign_up'

    try:
        response = execute_request(request_body)

        return {
            "is_successful": True,
           
            "error_description": None,
            "data": data,
            "response": response
        }

    except InvalidInputException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}


@app.route('/api/v1/login', methods=['post'])
def login():
    request_body = request.json
    data = request_body['data']
    request_body['table'] = 'management'
    request_body['method'] = 'select'
    request_body['method_type'] = 'login'

    try:
        response = execute_request(request_body)

        return {
            "is_successful": True,
            
            "error_description": None,
            "data": data,
            "response": response
        }
    except InvalidInputException as e:
        return {"is_successful": False, "error_description": str(e), "response": None}
