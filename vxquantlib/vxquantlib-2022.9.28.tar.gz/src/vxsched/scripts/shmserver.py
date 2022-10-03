"""共享内存EventBrokerServer"""

import argparse
from vxutils import to_binary, logger
from vxsched.pubsubs.shm import vxShareMemoryEventBrokerServer


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="""shm event broker server""")
    parser.add_argument(
        "--host",
        help="bind ip address,default: any ip address on the server",
        default="127.0.0.1",
        type=str,
    )
    parser.add_argument(
        "-p",
        "--port",
        help="bind ports,default: 5555",
        default=5555,
        type=int,
    )
    parser.add_argument(
        "-k", "--keyfile", help="private key file path", default="", type=str
    )
    args = parser.parse_args()
    address = (args.host, args.port)
    try:
        with open(args.keyfile, "r", encoding="utf-8") as f:
            authkey = f.read()
    except IOError:
        authkey = args.keyfile

    authkey = to_binary(authkey)
    # server = vxShareMemoryEventBrokerServer(address, authkey)
    # logger.info(f"开始运行shm event broker server: {args.host}:{args:port}")

    try:
        with vxShareMemoryEventBrokerServer(address, authkey) as server:
            server.get_server().serve_forever()
    except Exception as e:
        logger.warning("shm event broker server 停止服务. %s", e)
