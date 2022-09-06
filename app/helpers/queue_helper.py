import uuid

import pika


class RpcClient(object):

    def __init__(self, rabbit_server_host, queue_name, port):
        self.server_queue = queue_name

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_server_host, port=port))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', durable=False, auto_delete=True, exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            self.callback_queue,
            self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
            # print("received reply: ", body)

    def call(self, body):
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key=self.server_queue,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id),
            body=body)

        while self.response is None:
            self.connection.process_data_events(time_limit=None)

        self.channel.queue_delete(self.callback_queue)
        self.connection.close()
        return self.response


class RpcServer:
    def __init__(self, rabbit_server_host, queue_name, worker, virtual_host,
                 port, auto_delete=False, username=None, password=None):
        self.queue_name = queue_name

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_server_host, port=port))

        self.channel = self.connection.channel()
        res = self.channel.queue_declare(queue=queue_name)
        self.queue_name = res.method.queue

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_request, auto_ack=True)
        self.callback_queue = res.method.queue

        self.worker = worker

    def start_consuming(self):
        self.channel.start_consuming()

    def on_request(self, ch, method, props, body):
        worker = self.worker
        response = worker.serve_request(request_body=body)

        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=str(response))
        ch.basic_ack(delivery_tag=method.delivery_tag)
        # print("replied message: ", response, ", callback_queue: ", props.reply_to, ", corr_id: ",
        # props.correlation_id)
