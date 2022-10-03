"""账户管理"""


import pathlib
import importlib
from vxsched import vxContext, vxengine

from vxutils import logger, import_tools
from vxutils.database import vxMongoDB

# from vxutils.decorators import storage

from vxquant.model.exchange import (
    vxTick,
    vxTrade,
    vxAccountInfo,
    vxPosition,
    vxOrder,
    vxAlgoOrder,
)
from vxquant.mdapi.hq import vxTdxHQ


_default_tdgateway_config = {
    "publisher": {},
    "hqfetcher": {"class": "vxquant.mdapi.hq.vxTdxHQ", "params": {}},
    "setting": {},
    "channel_name": "gateway",
}


def run_tdgateway(configfile, mod_path):
    importlib.import_module("vxquant.strategy.pms_events", "")
    importlib.import_module("vxquant.strategy.pms_system", "")
    ctx = vxContext.load_json(configfile, _default_tdgateway_config)
    vxengine.reset(
        ctx.channel_name, ctx.setting.backend_url, ctx.setting.public_key, ctx
    )

    vxengine.context.database = vxMongoDB(ctx.setting.db_uri, ctx.setting.db_name)
    logger.info(f"设置database参数: {vxengine.context.database}.")
    vxengine.context.database.mapping("accounts", vxAccountInfo, ["account_id"])
    vxengine.context.database.mapping("positions", vxPosition, ["account_id", "symbol"])
    vxengine.context.database.mapping("orders", vxOrder, ["order_id"])
    vxengine.context.database.mapping("trades", vxTrade, ["trade_id"])
    vxengine.context.database.mapping("current", vxTick, ["symbol"])
    vxengine.context.database.mapping("algo_orders", vxAlgoOrder, ["algo_order_id"])

    vxengine.context.publisher = import_tools(
        ctx.publisher["class"], ctx.publisher["params"]
    )
    logger.info(f"加载publisher 完成。{vxengine.context.publisher}")

    vxengine.context.hqfetcher = vxTdxHQ()
    logger.info(f"加载行情接口: {vxengine.context.hqfetcher} 成功.")

    if mod_path and pathlib.Path(mod_path).is_dir():
        vxengine.load_modules(mod_path)

    vxengine.start()
