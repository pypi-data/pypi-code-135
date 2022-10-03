"""数据采集"""


from vxsched import vxengine
from vxutils import logger, vxtime, to_timestring


@vxengine.event_handler("before_trade")
def datacollector_before_trade(context, event) -> None:
    """每日早上开始执行采集任务"""

    # 1. 日历信息，如果
    today = to_timestring(vxtime.now(), "%Y-%m-%d")

    logger.info(f"开始执行{today}的采集任务")
    context.publisher("update_calendars", today)

    logger.info("开始更新证券列表 ... ")
    context.publisher("update_instruments", today)

    logger.info("开始采集分红数据")
    context.publisher("update_")
