"""调度器"""
import logging
from vxutils import vxtime, logger, to_timestring

from vxsched.context import vxContext
from vxsched.event import vxEvent, vxTrigger, TriggerStatus, vxEventQueue
from vxsched.core import (
    vxEventHandlers,
    vxRpcMethods,
    vxEventSched,
    vxEngine,
    vxhandlers,
    vxmethods,
    vxscheduler,
    vxPublisher,
    vxSubscriber,
    vxengine,
)
from vxsched.triggers import (
    vxDailyTrigger,
    vxWeeklyTrigger,
    vxIntervalTrigger,
    vxOnceTrigger,
)
from vxsched.pubsubs import (
    vxFTPPublisher,
    vxFTPSubscriber,
    vxZMQPublisher,
    vxZMQSubscriber,
    vxZMQRpcClient,
)


_old_factory = logging.getLogRecordFactory()

_DEFAULT_QUANT_FORMAT = (
    "%(quant_time)s %(module)s.%(funcName)s[%(lineno)d] %(levelname)s === %(message)s"
)


def _record_factory(*args, **kwargs):
    """记录工厂"""
    record = _old_factory(*args, **kwargs)
    format_str = "%F %T.%f" if vxtime.status == "LIVING" else "%F %T"
    record.quant_time = to_timestring(vxtime.now(), format_str)
    return record


logging.setLogRecordFactory(_record_factory)


_formatter = logging.Formatter(_DEFAULT_QUANT_FORMAT)
for handler in logger.handlers:
    handler.setFormatter(_formatter)


__all__ = [
    "vxContext",
    "vxEvent",
    "vxEventQueue",
    "vxEventHandlers",
    "vxRpcMethods",
    "vxEventSched",
    "vxEngine",
    "vxhandlers",
    "vxmethods",
    "vxscheduler",
    "vxengine",
    "load_modules",
    "vxPublisher",
    "vxSubscriber",
    "vxFTPPublisher",
    "vxFTPSubscriber",
    "vxZMQPublisher",
    "vxZMQSubscriber",
    "vxZMQRpcClient",
    "vxTrigger",
    "TriggerStatus",
    "vxOnceTrigger",
    "vxDailyTrigger",
    "vxWeeklyTrigger",
    "vxIntervalTrigger",
    "VERSION",
]
