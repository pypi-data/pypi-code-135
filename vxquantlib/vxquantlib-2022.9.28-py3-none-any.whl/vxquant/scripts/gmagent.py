"""gmagent"""

import os
import pathlib
import importlib
import subprocess
import sys

try:
    from gm import api as gm_api
    from vxquant.tdapi.gm import gmTdAPI
except ImportError:
    gm_api = None
    gmTdAPI = None

from vxutils import logger, vxtime, to_timestamp, to_enum, to_timestring, storage
from multiprocessing import Process
from vxsched import vxscheduler
from vxquant.model.contants import AccountType
from vxquant.model.preset import vxMarketPreset
from vxquant.model.tools.gmData import gmOrderConvter, gmTradeConvter
from vxquant.strategy.executeunit import init_agent


__all__ = ["run_gmagent", "init", "on_tick", "on_order_status", "on_execution_report"]


def init(gmcontext):
    """
    掘金量化策略中必须有init方法,且策略会首先运行init定义的内容
    """

    # 设置 时间函数
    vxtime.set_timefunc(lambda: to_timestamp(gmcontext.now))
    # 设置gm tdapi接口
    if vxscheduler.context.tdapi is None:
        account_type = vxscheduler.context.get("account_type", AccountType.Normal)
        account_type = to_enum(account_type, AccountType, AccountType.Normal)
        vxscheduler.context.tdapi = gmTdAPI(gmcontext, account_type)

    account = vxscheduler.context.tdapi.get_account()
    logger.info(f"检查下单接口是否正常: 账户({account.account_id}) 净资产: {account.nav:,.2f}元.")
    running_mode = vxscheduler.context.get("running_mode", "realtrade_time")
    if running_mode == "realtrade_time":
        tick_symbols = vxscheduler.context.get(
            "tick_symbols",
            [
                "SHSE.000001",
                "SHSE.000688",
                "SHSE.511880",
                "SHSE.510300",
                "SHSE.511990",
                "SHSE.511660",
                "SHSE.204001",
                "SZSE.399001",
                "SZSE.399673",
                "SZSE.159001",
                "SZSE.159919",
                "SZSE.159915",
                "SZSE.159937",
                "SZSE.131810",
            ],
        )
        logger.info(f"订阅tick data: {tick_symbols}")
        gm_api.subscribe(
            tick_symbols,
            "tick",
        )
        gm_api.schedule(do_settle, "1d", "15:00:00")
        gm_api.schedule(before_trade, "1d", "09:15:00")
        logger.info("安排函数 before_trade 于09:15:00 启动; 函数 do_settle 于15:00:00启动；")
    elif running_mode == "simtrade24":
        interval = int(vxscheduler.context.get("tick_interval", 10))
        now = vxtime.now()
        for i in range(3, 600, interval):
            gm_api.schedule(on_tick, "1d", to_timestring(now + i, "%H:%M:%S"))
        gm_api.schedule(quit_simtrade, "1d", to_timestring(now + 603, "%H:%M:%S"))
        logger.info("安排函数 600s中每隔{interval}s运行一次on_tick")
    else:
        raise ValueError(
            f"running mode only support['realtrade_time','simtrade24']. {running_mode}"
        )

    vxscheduler.activate()
    logger.info("执行初始化时间__init__ ....")
    list(map(vxscheduler.handler.trigger, vxscheduler.fetch_events()))
    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info("=" * 60)


def do_settle(gmcontext):
    """收盘后，等待日结"""

    end_dt = vxtime.today("22:00:00")
    logger.info(f"开盘后运行时段，截止{to_timestring(end_dt)}.....")
    while vxtime.now() < end_dt:
        on_tick(gmcontext, None)
        vxtime.sleep(1)


def before_trade(gmcontext):
    """开盘前"""
    logger.info(f"开盘前运行时段.....{gmcontext.now}")
    end_dt = vxtime.today("09:30:00")
    while vxtime.now() < end_dt:
        on_tick(gmcontext, None)
        vxtime.sleep(1)


def all_day_run(gmcontext):
    """全天事件"""
    logger.info(f"开始运行全天事件.... {to_timestring(vxtime.now())}")
    end_dt = vxtime.now() + 60 * 60 * 24 - 1
    while vxtime.now() < end_dt:
        on_tick(gmcontext, None)
        vxtime.sleep(0.1)
    logger.info(f"结束运行全天事件.... {to_timestring(vxtime.now())}")


def on_tick(gmcontext, gmtick=None):
    """on tick"""

    for subscriber in vxscheduler.subscribers:
        try:
            events = subscriber()
            if events:
                logger.debug(f"收到{len(events)}个")
                list(map(vxscheduler.submit_event, events))

        except Exception as e:
            logger.error(f"subscriber runing error: {e}")

    list(map(vxscheduler.handler.trigger, vxscheduler.fetch_events()))


def on_order_status(gmcontext, order):
    """
    委托状态更新事件. 参数order为委托信息
    响应委托状态更新事情，下单后及委托状态更新时被触发
    3.0.113 后增加.
    与on_order_status 具有等同含义, 在二者都被定义时(当前函数返回类型为类，速度更快，推介使用), 只会调用 on_order_status_v2
    """
    logger.debug(f"gmorder: {order}")
    vxorder = gmOrderConvter(order)

    if vxorder.status.name not in ["New", "PendingNew"]:
        vxscheduler.submit_event("on_broker_order_status", vxorder)
        logger.info(f"内部上报委托更新: {vxorder}...")
    else:
        logger.warning(f"抛弃OrderStatus.New and OrderStatus.PendingNew订单更新. {vxorder}")


def on_execution_report(gmcontext, execrpt):
    """
    委托执行回报事件. 参数 execrpt 为执行回报信息
    响应委托被执行事件，委托成交后被触发
    3.0.113 后增加
    已 on_execution_report 具有等同含义, 在二者都被定义时(当前函数返回类型为类，速度更快，推介使用), 只会调用 on_execution_report_v2
    """

    logger.debug(f"gmtrade: {execrpt}")
    vxtrade = gmTradeConvter(execrpt)
    if vxtrade.commission == 0:
        _preset = vxMarketPreset(vxtrade.symbol)
        vxtrade.commission = max(
            (
                vxtrade.price
                * vxtrade.volume
                * (
                    _preset.commission_coeff_peramount
                    if vxtrade.order_direction.name == "Buy"
                    else (
                        _preset.commission_coeff_peramount + _preset.tax_coeff_peramount
                    )
                )
            ),
            5,
        )

    if vxtrade.status.name == "Trade":
        vxscheduler.submit_event("on_broker_execution_report", vxtrade)
        logger.info(f"内部上报成交回报 {vxtrade} ...")
    else:
        logger.warning(f"抛弃非成交回报信息。 {vxtrade}")


def quit_simtrade(gmcontext):
    """退出时调用"""
    logger.warning("**** 模拟交易结束 ****")
    sys.exit(0)


def run_gmagent(config, mod):
    """运行gmagent

    Arguments:
        config {} -- _description_
        mod {_type_} -- _description_
    """
    importlib.import_module("vxquant.strategy.executeunit", "")
    ENV = os.environ.copy()
    ENV.update({"GMCONFIGFILE": config, "AGENTMOD": mod})
    subprocess.run(["python", f"{__file__}"], env=ENV)


if __name__ == "__main__":
    from vxquant.strategy.executeunit import init_agent

    init_agent(os.environ.get("GMCONFIGFILE", "agent.json"))
    gm_api.run(
        strategy_id=vxscheduler.context.gm_strategyid,
        filename=pathlib.Path(__file__).name,
        mode=gm_api.MODE_LIVE,
        token=vxscheduler.context.gm_token,
    )
