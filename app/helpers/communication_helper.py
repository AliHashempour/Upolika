from app.helpers import config_helper
import pika


def send_rpc_message(rabbit_host, port, user_name, password, queue_name, method, service, request_data):
    
    return 0


def send_message(method_type, table, request_data):
    method = method_type
    service = table
    data = request_data
    cfg_helper = config_helper.ConfigHelper()

    rabbit_host = cfg_helper.get('RABBITMQ', 'host')
    rabbit_port = cfg_helper.get('RABBITMQ', 'port')
    rabbit_user_name = cfg_helper.get('RABBITMQ', 'username')
    rabbit_password = cfg_helper.get('RABBITMQ', 'password')

    service_queue_name = cfg_helper.get(service.upper(), 'service_queue_name')
    service_exchange_type = cfg_helper.get(service.upper(), 'rabbit_type')

    if service_exchange_type == 'rpc':
        response = send_rpc_message(rabbit_host, rabbit_port, rabbit_user_name, rabbit_password, service_queue_name,
                                    method, service, data)
    else:
        response = {}

    return response
