#!/usr/bin/env python3
"""zmq broker server scripts"""

import argparse
from vxsched import vxEvent
from vxutils import import_tools, logger,storage
from vxsched.context import vxContext

_default_broker_config = {
    "subscribers": [],
    "transfer_to": [],
    "server": {
        "class": "vxsched.broker.vxZMQBrokerServer",
        "params": {
            "frontend_url": "tcp://*:12306",
            "frontend_sercet_key": "",
            "backend_url": "tcp://*:12308",
            "backend_sercet_key": "",
        },
    },
    "events": [],
}

@storage("depart","eventbroker")
def main(config_file):
    """主函数"""
    context = vxContext.load_json(config_file, _default_broker_config)

    server = import_tools(context.server["class"], context.server.params)

    for pubs in context.transfer_to:
        publisher = import_tools(pubs["class"], pubs.params)
        server.transfer_out(publisher.channel_name, publisher)
        logger.info(f"增加transfer to({publisher.channel_name},{publisher})...")

    # context.subscribers = []
    for subs in context.subscribers:
        subscriber = import_tools(subs["class"], subs.params)
        server.subscribe(subscriber)
        logger.info(f"增加subscribe : ({subscriber})")

    for event_params in context.events:
        event = vxEvent(type=event_params.type, channel=event_params.channel)
        if "trigger" in event_params:
            trigger = import_tools(
                event_params["trigger"]["class"], event_params["trigger"]["params"]
            )
            event.trigger = trigger
        server.submit_event(event)
        logger.info(f"增加预处理消息: {event.type} === {event.id}")

    server.server_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""zmq event broker server""")
    parser.add_argument(
        "-c",
        "--config",
        help="path to config json file",
        default="etc/broker.json",
        type=str,
    )
    parser.add_argument(
        "-v", "--verbose", help="debug 模式", action="store_true", default=False
    )

    args = parser.parse_args()
    if args.verbose:
        logger.setLevel("DEBUG")

    main(args.config)
