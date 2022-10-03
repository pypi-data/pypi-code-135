"""账户gateway远程调用方法"""


import uuid


from typing import Dict, Any
from vxsched import vxengine, logger, vxtime

from vxutils import logger, vxtime, to_timestring
from vxquant.model.portfolio import vxMarketPreset
from vxquant.model.exchange import (
    vxAlgoOrder,
    vxCashPosition,
    vxAccountInfo,
    vxOrder,
)
from vxquant.model.contants import SecType
from vxsched.event import vxEvent


from vxquant.exceptions import (
    NoEnoughCash,
    NoEnoughPosition,
    IllegalPrice,
    # * IllegalVolume,
    # * RiskRuleCheckFailed,
    # * IllegalAccountId,
    # * IllegalStrategyId,
    # * IllegalSymbol,
    # * AccountDisabled,
    # * AccountDisconnected,
    # * AccountLoggedout,
    # * NotInTradingSession,
    # * OrderTypeNotSupported,
    # * Throttle,
    # * IllegalOrder,
    # * OrderFinalized,
    # * UnknownOrder,
    # * AlreadyInPendingCancel,
)


@vxengine.event_handler("before_trade")
def pms_before_trade(context, event) -> None:
    """开盘前"""

    holidays = context.database.calendars.distinct(
        "trade_date", {"trade_date": to_timestring(vxtime.now(), "%Y-%m-%d"), "flag": 0}
    )


@vxengine.event_handler("on_gateway_settle")
def pms_on_gateway_settle(context, event):
    """日结函数"""
