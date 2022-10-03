#!/usr/bin/env python3
"""zmq broker server scripts"""

import argparse
from vxsched.broker import vxZMQBrokerServer, vxAsyncZMQBrokerServer
from vxsched.context import vxContext
from vxsched.pubsubs import vxZMQPublisher, vxZMQSubscriber

_default_broker_config = {
    "subscribers": {
        "tt1": {"class": "vxsched.pubsubs.vxZMQSubscriber", "params": {}},
    },
    "transfer_to": {
        "test": {
            "class": "vxsched.pubsubs.vxZMQPublisher",
            "params": {"channel_name": "test"},
        }
    },
    "server": {
        "class": "vxsched.broker.vxZMQBrokerServer",
        "params": {
            "frontend_url": "tcp://*:12306",
            "fronted_secrets_key": "",
            "backend_url": "tcp://*:12308",
            "backend_secrets_key": "",
        },
    },
}


def main(context):
    """主函数"""
    print(context)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="""zmq event broker server""")
    parser.add_argument(
        "-c",
        "--config",
        help="path to config json file",
        default="etc/broker.json",
        type=str,
    )

    args = parser.parse_args()
    context = vxContext.load_json(args.config, _default_broker_config)
    main(context)
