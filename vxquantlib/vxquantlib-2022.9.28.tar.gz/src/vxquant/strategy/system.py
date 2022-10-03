"""量化交易系统基础函数"""

from vxquant.utils import vxtime, logger
from vxquant.utils.toolbox import vxToolBox
from vxquant.utils.convertors import to_timestring
from vxquant.scheduler import vxhandlers
from vxquant.scheduler.triggers.daily import vxDailyTrigger
from vxquant.scheduler.triggers.interval import vxIntervalTrigger

box = vxToolBox()
logger.setLevel("DEBUG")


@vxhandlers("__init__")
def system_init(vxcontext, _):
    """系统初始化"""
    logger.info(f"""开始执行初始化操作 {to_timestring( vxtime.now())}""")
    box.local.put(
        "before_trade", data="", trigger=vxDailyTrigger("09:15:00"), priority=20
    )
    box.local.put("on_trade", data="", trigger=vxDailyTrigger("09:30:00"), priority=20)
    box.local.put(
        "before_close", data="", trigger=vxDailyTrigger("14:45:00"), priority=20
    )
    box.local.put("on_close", data="", trigger=vxDailyTrigger("14:50:00"), priority=20)
    box.local.put(
        "after_close", data="", trigger=vxDailyTrigger("15:30:00"), priority=20
    )
    box.local.put("on_settle", data="", trigger=vxDailyTrigger("16:30:00"), priority=20)


@vxhandlers("__init__")
def system_beforetrade(vxcontext, event) -> None:
    """双均线策略 before_trade方法"""
    box.local.put(
        "on_tick",
        data="",
        trigger=vxIntervalTrigger(
            3, vxtime.today("09:15:00"), vxtime.today("11:30:00")
        ),
        priority=20,
    )
    box.local.put(
        "on_tick",
        data="",
        trigger=vxIntervalTrigger(
            3, vxtime.today("13:00:00"), vxtime.today("15:00:00")
        ),
        priority=20,
    )
