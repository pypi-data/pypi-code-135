"""各类组件启动程序"""

import importlib
import argparse
from vxutils import logger, storage

# from vxquant.scripts import *

importlib.import_module("vxquant.scripts", "")


@storage("scripts", "main")
def main(config, mod):
    logger.info(f"config={config}, mod={mod}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""trade gateway server""")
    parser.add_argument("-s", "--script", help="启动组件", default="main")
    parser.add_argument(
        "-c",
        "--config",
        help="path to config json file",
        default="config.json",
        type=str,
    )
    parser.add_argument("-m", "--mod", help="模块存放目录", default="./mod", type=str)
    parser.add_argument(
        "-v", "--verbose", help="debug 模式", action="store_true", default=False
    )
    args = parser.parse_args()

    if args.verbose:
        logger.setLevel("DEBUG")

    func = storage.get("scripts", args.script)

    if callable(func):
        func(args.config, args.mod)
