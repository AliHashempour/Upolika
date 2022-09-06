import json

from app.helpers import config_helper, queue_helper


def send_rpc_message(rabbit_host, port, queue_name, request_body):
    client = queue_helper.RpcClient(rabbit_server_host=rabbit_host,
                                    port=port,
                                    queue_name=queue_name)

    message = json.dumps(request_body)
    resp = client.call(message)

    response = json.loads(resp.decode("utf-8"))

    return response


def send_message(table, body):
    service = table
    request_body = body
    cfg_helper = config_helper.ConfigHelper()

    rabbit_host = cfg_helper.get('RABBITMQ', 'host')
    rabbit_port = cfg_helper.get('RABBITMQ', 'port')

    service_queue_name = cfg_helper.get(service.upper(), 'service_queue_name')
    service_exchange_type = cfg_helper.get(service.upper(), 'rabbit_type')

    if service_exchange_type == 'rpc':
        response = send_rpc_message(rabbit_host, rabbit_port, service_queue_name, request_body)
    else:
        response = {}

    return response
