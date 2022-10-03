"""账户管理"""

import argparse
import pathlib


from vxsched import vxContext, vxengine

from vxutils import logger, import_tools


from vxquant.model.portfolio import vxAccountsManager
from vxquant.mdapi.hq import vxTdxHQ

_default_tdgateway_config = {
    "publisher": {},
    "hqfetcher": {"class": "vxquant.mdapi.hq.vxTdxHQ", "params": {}},
    "setting": {},
    "channel_name": "gateway",
}


def main(configfile, mod_path):
    ctx = vxContext.load_json(configfile, _default_tdgateway_config)
    vxengine.reset(
        ctx.channel_name, ctx.setting.backend_url, ctx.setting.public_key, ctx
    )

    if "publisher" not in vxengine.context or not vxengine.context.publisher:
        raise ValueError("没有指定消息通道参数.")
    publisher = import_tools(
        vxengine.context.publisher["class"], vxengine.context.publisher["params"]
    )
    logger.info(f"加载publisher 完成。{publisher}")

    if "hqfetcher" not in vxengine.context or not vxengine.context.hqfetcher:
        raise ValueError("没有指定行情更新接口")
    hqfetcher = vxTdxHQ()
    logger.info(f"加载行情接口: {hqfetcher} 成功.")

    manager = vxAccountsManager(
        vxengine.context.setting.db_uri,
        vxengine.context.setting.db_name,
        publisher,
        hqfetcher,
    )

    vxengine.rpc_method("create_account", with_context=False)(manager.create_account)
    vxengine.rpc_method("get_account", with_context=False)(manager.get_account)
    vxengine.rpc_method("get_positions", with_context=False)(manager.get_positions)
    vxengine.rpc_method("get_orders", with_context=False)(manager.get_orders)
    vxengine.rpc_method("get_trades", with_context=False)(manager.get_trades)
    vxengine.rpc_method("order_volume", with_context=False)(manager.order_volume)
    vxengine.rpc_method("order_cancel", with_context=False)(manager.order_cancel)
    vxengine.rpc_method("deposit", with_context=False)(manager.deposit)
    vxengine.rpc_method("withdraw", with_context=False)(manager.withdraw)

    vxengine.event_handler("on_order_status")(manager.on_order_status)
    vxengine.event_handler("on_execution_report")(manager.on_trade_status)

    if mod_path and pathlib.Path(mod_path).is_dir():
        vxengine.load_modules(mod_path)

    vxengine.start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""trade gateway server""")
    parser.add_argument(
        "-c",
        "--config",
        help="path to config json file",
        default="etc/gateway.json",
        type=str,
    )
    parser.add_argument("-m", "--mod", help="模块存放目录", default="./mod", type=str)
    parser.add_argument(
        "-v", "--verbose", help="debug 模式", action="store_true", default=False
    )

    args = parser.parse_args()
    if args.verbose:
        logger.setLevel("DEBUG")

    main(args.config, args.mod)
