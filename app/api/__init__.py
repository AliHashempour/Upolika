from flask import Flask, request
from flask_cors import CORS
import app.api.utils as utils

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/select_request', methods=['post'])
def select_request():
    print(request.json)
    return {
        "is_successful": True,
        "error_code": 0,
        "error_description": None,
        "data": None,
        "request": request.json
    }


@app.route('/api/v1/insert_request', methods=['post'])
def insert_request():
    print(request.json)
    return {
        "is_successful": True,
        "error_code": 0,
        "error_description": None,
        "data": None,
        "request": request.json
    }


@app.route('/api/v1/update_request', methods=['post'])
def update_request():
    print(request.json)
    return {
        "is_successful": True,
        "error_code": 0,
        "error_description": None,
        "data": None,
        "request": request.json
    }


@app.route('/api/v1/delete_request', methods=['post'])
def delete_request():
    print(request.json)
    return {
        "is_successful": True,
        "error_code": 0,
        "error_description": None,
        "data": None,
        "request": request.json
    }


@app.route('/api/v1/sign_up', methods=['post'])
def sign_up():
    request_body = request.json
    data = request_body['data']
    res = utils.index_user(data=data)
    return {
        "is_successful": True,
        "error_code": 0,
        "error_description": None,
        "data": None,
        "response": res
    }
