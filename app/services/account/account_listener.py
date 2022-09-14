import time

from app.helpers import config_helper
from app.helpers.rabbit_helper import RpcServer
from app.services.account.account_worker import AccountWorkerWrapper

if __name__ == "__main__":
    service_name = 'ACCOUNT'

    while True:
        try:
            cfg_helper = config_helper.ConfigHelper()

            rabbit_server = cfg_helper.get("RABBIT", "host")
            rabbit_virtual_host = cfg_helper.get("RABBIT", "virtual_host")
            username = cfg_helper.get("RABBIT", "username")
            password = cfg_helper.get("RABBIT", 'password')
            rabbit_type = cfg_helper.get(service_name, "rabbit_type")
            queue_name = cfg_helper.get(service_name, 'service_queue_name')

            worker = AccountWorkerWrapper()

            if rabbit_type == "rpc":
                server = RpcServer(rabbit_server_host=rabbit_server, queue_name=queue_name,
                                   worker=worker, port=5672, username=username, password=password)

            else:
                raise Exception("INVALID RABBIT TYPE")
            server.start_consuming()
        except Exception as e:
            # tb.print_tb(e.__traceback__)
            time.sleep(10)
            # print("Trying to restart the server...")
