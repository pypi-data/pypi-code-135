"""模拟成交订单"""

import argparse

from multiprocessing import Lock
import uuid

from vxsched import vxscheduler, vxContext
from vxsched import vxscheduler

from vxutils import logger, vxtime, vxDataClass, vxField, vxEnumField, vxUUIDField
from build.lib.vxquant.model.exchange import vxTrade
from vxquant.exceptions import OrderRejectReasonException
from vxquant.model.preset import vxMarketPreset
from vxquant.model.contants import OrderStatus, OrderDirection, OrderType, TradeStatus
from vxquant.model.exchange import vxOrder
from vxquant.model.portfolio import vxStockAccount


@vxscheduler.handler("on_submit_broker_order")
def tdgateway_on_submit_sim_order(context, event) -> None:
    """提交模拟委托订单"""
    broker_order = vxOrder(**event.data.message)
    broker_order.exchange_order_id = str(uuid.uuid4())
    broker_order.status = OrderStatus.New
    with context.simlock:
        context.sim_orderbook[broker_order.exchange_order_id] = broker_order
    vxscheduler.submit_event("on_order_status", broker_order)


@vxscheduler.handler("on_submit_sim_order_cancel")
def tdgateway_on_submit_sim_order_cancel(context, event) -> None:
    """提交撤销模拟委托订单"""
    wait_cancel_order = vxOrder(**event.data.message)
    broker_order = context.sim_orderbook.get(wait_cancel_order.exchange_order_id, None)
    if broker_order is None:
        return

    with context.simlock:
        if broker_order.status in [
            OrderStatus.Filled,
            OrderStatus.Expired,
            OrderStatus.Rejected,
            OrderStatus.Canceled,
            OrderStatus.Expired,
        ]:
            return

        broker_order.status = OrderStatus.Canceled
        vxscheduler.submit_event("on_order_status", broker_order)


@vxscheduler.handler("on_tick")
def tdgateway_on_simorderbook(context, _) -> None:
    """模拟撮合成交"""

    with context.simlock:
        for broker_order in context.sim_orderbook.values():
            if broker_order not in [
                OrderStatus.New,
                OrderStatus.PartiallyFilled,
                OrderStatus.PendingNew,
            ]:
                continue

            if vxtime.now() > broker_order.due_dt:
                broker_order.status = OrderStatus.Expired
                vxscheduler.submit_event("on_order_status", broker_order)
                logger.warning(f"SIM,委托超时，更新委托状态: {broker_order}")
                continue

            vxtick = context.mdapi.current(broker_order)
            if broker_order.updated_dt + 3 > vxtick.created_dt:
                continue

            if (
                broker_order.order_direction == OrderDirection.Buy
                and broker_order.order_type == OrderType.Market
                and vxtick.ask1_v > 0
            ):
                # TODO 市价买单
                broker_trade = vxTrade(
                    account_id=broker_order.account_id,
                    order_id=broker_order.order_id,
                    exchange_order_id=broker_order.exchange_id,
                    symbol=broker_order.symbol,
                    order_direction=broker_order.order_direction,
                    order_type=broker_order.order_type,
                    order_offset=broker_order.order_offset,
                    price=vxtick.ask1_p,
                    volume=min(
                        int(vxtick.ask1_v * 0.5),
                        broker_order.volume - broker_order.filled_volume,
                    ),
                    commission=0,
                    status=TradeStatus.Trade,
                )

                broker_trade.commission = (
                    broker_trade.volume
                    * broker_trade.price
                    * vxMarketPreset(broker_trade.symbol).commission_coeff_peramount
                )

                vxscheduler.submit_event("on_execution_report", broker_trade)
                logger.warning(f"SIM撮合成交: {broker_trade}")

                broker_order.filled_volume += broker_trade.volume
                broker_order.filled_amount += (
                    broker_trade.price * broker_trade.volume + broker_trade.commission
                )
                broker_order.status = (
                    OrderStatus.Filled
                    if broker_order.filled_volume >= broker_order.volume
                    else OrderStatus.PartiallyFilled
                )
                vxscheduler.submit_event("on_order_status", broker_order)
                logger.warning(f"SIM 更新委托状态: {broker_order}")
            elif (
                broker_order.order_direction == OrderDirection.Buy
                and broker_order.order_type == OrderType.Limit
                and vxtick.ask1_p < broker_order.price
            ):
                # TODO 限价买单
                pass

            elif (
                broker_order.order_direction == OrderDirection.Sell
                and broker_order.order_type == OrderType.Market
                and vxtick.bid1_v > 0
            ):
                # TODO 市价委托
                pass
            elif (
                broker_order.order_direction == OrderDirection.Sell
                and broker_order.order_type == OrderType.Limit
                and vxtick.bid1_p > broker_order.price
            ):
                # TODO 限价单撮合
                pass
