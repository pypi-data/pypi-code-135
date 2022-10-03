"""vxsched 主函数"""

import argparse
import multiprocessing as mp
from vxutils import logger
from vxsched import vxscheduler, vxChannel, init_scheduler


_default_context = {
    "channel_name": "local",
    "tools": {},
    "brokers": {},
    "channels": {
        "local": {
            "class": "vxsched.vxChannel",
            "params": {"channel_name": "channel_name", "event_broker": ""},
        }
    },
}


if __name__ == "__main__":
    mp.set_start_method("fork")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--name", help="scheduler name id", default="local", type=str
    )
    parser.add_argument(
        "-c",
        "--config",
        help="config json file path: etc/config.json",
        default="config.json",
        type=str,
    )
    parser.add_argument(
        "-m", "--mod", help="module directory path : mod/ ", default="mod/", type=str
    )
    args = parser.parse_args()
    init_scheduler(
        vxscheduler,
        config_file=args.config,
        mod_path=args.mod,
        default_config=_default_context,
    )

    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info("=" * 60)
    try:
        logger.info("-" * 60)
        logger.info("初始化mod.__init__事件")
        channel = vxChannel(args.name)
        channel.put("__init__")
        vxscheduler.start(args.name, workers=16)
    except Exception as e:
        logger.error(e)
    finally:
        vxscheduler.stop()

    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info("=" * 60)
