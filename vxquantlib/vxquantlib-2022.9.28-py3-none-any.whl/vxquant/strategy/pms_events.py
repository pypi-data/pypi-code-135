"""PositionManagerServies 账户管理服务"""

from collections import defaultdict
import contextlib
from queue import Empty, Queue
import uuid
import pymongo
import pandas as pd
from typing import Dict, Any
from vxsched import vxengine, logger, vxtime

from vxquant.model.portfolio import vxMarketPreset
from vxquant.model.exchange import (
    vxAlgoOrder,
    vxCashPosition,
    vxPosition,
    vxAccountInfo,
    vxOrder,
)
from vxquant.model.contants import (
    OrderDirection,
    # OrderOffset,
    OrderStatus,
    # OrderType,
    SecType,
)
from vxsched.event import vxEvent


from vxquant.exceptions import (
    NoEnoughCash,
    NoEnoughPosition,
    # * IllegalVolume,
    IllegalPrice,
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


@vxengine.event_handler("__init__")
def pms_init(context, event) -> None:
    """初始化"""
    cur = context.database.agent_mapping.find({})
    context.agent_map = {item.account_id: item.channel_name for item in cur}
    context.pending_order_queue = Queue()
    context.rebalance_orders = {}


@vxengine.event_handler("on_order_status")
def pms_on_order_status(context, event):
    """收到委托订单更新"""
    with context.database.start_session(causal_consistency=True) as session:
        # 1. 更新order 状态信息
        broker_order = event.data
        if broker_order.status not in [
            OrderStatus.PartiallyFilled,
            OrderStatus.New,
            OrderStatus.PendingNew,
        ]:
            # 已终结订单，根据返回信息更新数据库订单
            context.database.orders.update_one(
                {
                    "order_id": broker_order.order_id,
                    "status": {"$in": ["New", "PendingNew", "PartiallyFilled"]},
                },
                {
                    "$set": {
                        "filled_volume": broker_order.filled_volume,
                        "filled_amount": broker_order.filled_amount,
                        "filled_vwap": broker_order.filled_vwap,
                        "status": broker_order.status.name,
                        "exchange_order_id": broker_order.exchange_order_id,
                        "updated_dt": broker_order.updated_dt,
                    }
                },
                upsert=True,
                session=session,
            )
        else:
            context.database.orders.update_one(
                {
                    "order_id": broker_order.order_id,
                    "status": {"$in": ["New", "PendingNew", "PartiallyFilled"]},
                },
                {
                    "$set": {
                        "filled_volume": broker_order.filled_volume,
                        "filled_amount": broker_order.filled_amount,
                        "filled_vwap": broker_order.filled_vwap,
                        "status": broker_order.status.name,
                        "exchange_order_id": broker_order.exchange_order_id,
                        "updated_dt": broker_order.updated_dt,
                    }
                },
                session=session,
            )
        _update_frozens(context, [broker_order.account_id], session=session)
        _update_account_info(context, [broker_order.account_id], session=session)


@vxengine.event_handler("on_execution_report")
def pms_on_execution_report(context, event) -> None:
    """收到成交回报信息"""

    with context.database.start_session(causal_consistency=True, lock=True) as session:
        broker_trade = event.data
        # 保存trades 层数据
        context.database.save("trades", broker_trade, session=session)

        # 处理order filled_volumes
        _update_order_filled_volumes(
            context, [broker_trade.account_id], session=session
        )

        # 处理 position volume数据
        if broker_trade.order_direction == OrderDirection.Buy:
            _update_position_buy(context, broker_trade, session)
        else:
            _update_position_sell(context, broker_trade, session)

        _update_frozens(context, [broker_trade.account_id], session=session)
        _update_account_info(context, [broker_trade.account_id], session=session)


def _update_position_buy(context, broker_trade, session=None):
    filled_amount = broker_trade.price * broker_trade.volume
    commission = broker_trade.commission

    item = context.database.positions.find_one(
        {
            "account_id": broker_trade.account_id,
            "symbol": "CNY",
        },
        {"_id": 0},
    )

    cash = vxCashPosition(item)
    delta = cash.volume_his - filled_amount - commission
    cash.volume_his = max(delta, 0)
    cash.volume_today += min(delta, 0)
    context.database.save("positions", cash, session=session)

    preset = vxMarketPreset(broker_trade.symbol)

    context.database.positions.update_one(
        {"account_id": broker_trade.account_id, "symbol": broker_trade.symbol},
        {
            "$set": {
                "lasttrade": broker_trade.price,
            },
            "$inc": {
                "volume_today": broker_trade.volume,
                "cost": filled_amount + commission,
            },
            "$setOnInsert": {
                "position_id": str(uuid.uuid4()),
                "position_side": "Long",
                "volume_his": 0,
                "volume": broker_trade.volume,
                "security_type": preset.security_type.name,
                "allow_t0": preset.allow_t0,
                "frozen": 0,
                "available": broker_trade.volume if preset.allow_t0 else 0,
                "fnl": -commission,
                "benchmark_marketvalue": -1,
                "uplimit_marketvalue": -1,
                "downlimit_marketvalue": -1,
            },
        },
        upsert=True,
        session=session,
    )

    return


def _update_position_sell(context, broker_trade, session=None):
    filled_amount = broker_trade.price * broker_trade.volume
    commission = broker_trade.commission
    item = context.database.positions.find_one(
        {"account_id": broker_trade.account_id, "symbol": broker_trade.symbol}
    )
    symbol_position = vxPosition(item)
    delta = symbol_position.volume_his - broker_trade.volume
    symbol_position.volume_his = max(delta, 0)
    symbol_position.volume_today += min(delta, 0)
    symbol_position.lasttrade = broker_trade.price
    symbol_position.cost = symbol_position.cost - filled_amount + commission

    context.database.positions.update_one(
        {"account_id": broker_trade.account_id, "symbol": broker_trade.symbol},
        {"$set": symbol_position.message},
    )

    context.database.positions.update_one(
        {"account_id": broker_trade.account_id, "symbol": "CNY"},
        {
            "$inc": {
                "volume_today": +filled_amount - commission,
                "volume": +filled_amount - commission,
                "available": +filled_amount - commission,
                "marketvalue": +filled_amount - commission,
                "cost": +filled_amount - commission,
            }
        },
    )


def _update_frozens(context, account_ids, session=None):
    """重新计算持仓冻结信息"""
    modify_position_ids = context.database.orders.distinct(
        "frozen_position_id", {"account_id": {"$in": account_ids}}, session=session
    )
    agg_position_frozens = context.database.orders.aggregate(
        [
            {
                "$match": {
                    # "account_id": {"$in": account_ids},
                    "frozen_position_id": {"$in": modify_position_ids},
                    "status": {"$in": ["New", "PartiallyFilled", "PendingNew"]},
                }
            },
            {
                "$project": {
                    "account_id": "$account_id",
                    "order_id": "$order_id",
                    "frozen_position_id": "$frozen_position_id",
                    "order_direction": "$order_direction",
                    "left_volume": {"$subtract": ["$volume", "$filled_volume"]},
                    "price": "$price",
                    "cost": {
                        "$multiply": [
                            {"$subtract": ["$volume", "$filled_volume"]},
                            "$price",
                        ]
                    },
                }
            },
            {
                "$group": {
                    "_id": {
                        "account_id": "$account_id",
                        "position_id": "$frozen_position_id",
                        "order_direction": "$order_direction",
                    },
                    "left_volume": {"$sum": "$left_volume"},
                    "cost": {"$sum": "$cost"},
                }
            },
        ],
        session=session,
    )
    update_position_cmds = [
        pymongo.UpdateMany(
            {"position_id": {"$in": modify_position_ids}}, {"$set": {"frozen": 0.0}}
        )
    ]
    update_account_cmds = []

    for agg_position_frozen in agg_position_frozens:
        position_id = agg_position_frozen["_id"]["position_id"]
        order_direction = agg_position_frozen["_id"]["order_direction"]

        if order_direction == "Buy":
            update_cmd = pymongo.UpdateOne(
                {"position_id": position_id},
                {"$set": {"frozen": (agg_position_frozen["cost"] * 1.003)}},
            )
            update_account_cmd = pymongo.UpdateOne(
                {"accountt_id": agg_position_frozen["_id"]["account_id"]},
                {"$set": {"frozen": (agg_position_frozen["cost"] * 1.003)}},
            )
            update_account_cmds.append(update_account_cmd)
            logger.info(f"更新SQL accounts: {update_account_cmd}")

        else:
            update_cmd = pymongo.UpdateOne(
                {"position_id": position_id},
                {"$set": {"frozen": (agg_position_frozen["left_volume"])}},
            )

        update_position_cmds.append(update_cmd)
        logger.info(f"更新SQL positions: {update_cmd}")

    context.database.positions.bulk_write(
        update_position_cmds, ordered=True, session=session
    )
    if update_account_cmds:
        context.database.accounts.bulk_write(
            update_account_cmds,
            ordered=True,
        )
        # logger.warning(f"更新SQL accounts: {update_account_cmds}")


def _update_order_filled_volumes(context, account_ids, session=None):
    """重新计算委托订单成交信息"""
    unfinished_order_ids = context.database.distinct(
        "orders",
        "order_id",
        {
            "status": {"$in": ["New", "PendingNew", "PartiallyFilled", "Unknown"]},
            "account_id": {"$in": account_ids},
        },
        session=session,
    )
    logger.info(f"共有{len(unfinished_order_ids)}个未完成订单.")
    agg_filled_volumes = context.database.trades.aggregate(
        [
            {"$match": {"order_id": {"$in": unfinished_order_ids}}},
            {
                "$group": {
                    "_id": {
                        "order_id": "$order_id",
                        "order_direction": "$order_direction",
                    },
                    "volume": {"$max": "$volume"},
                    "filled_volume": {"$sum": "$volume"},
                    "commission": {"$sum": "$commission"},
                    "cost": {"$sum": {"$multiply": ["$price", "$volume"]}},
                }
            },
            {"$match": {"filled_volume": {"$gt": 0}}},
        ],
        session=session,
    )

    update_order_cmds = []
    modify_order_ids = []
    for agg_filled_volume in agg_filled_volumes:
        order_id = agg_filled_volume["_id"]["order_id"]
        order_direction = agg_filled_volume["_id"]["order_direction"]
        filled_amount = (
            (agg_filled_volume["cost"] + agg_filled_volume["cost"])
            if order_direction == "Buy"
            else (agg_filled_volume["cost"] - agg_filled_volume["cost"])
        )
        filled_vwap = filled_amount / agg_filled_volume["filled_volume"]
        logger.info(
            f"订单{order_id} {order_direction} filled_amount={filled_amount} filled_vwap={filled_vwap}."
        )

        update_order_cmd = pymongo.UpdateOne(
            {"order_id": order_id},
            {
                "$set": {
                    "filled_volume": agg_filled_volume["filled_volume"],
                    "filled_amount": filled_amount,
                    "filled_vwap": filled_vwap,
                    "status": "Filled"
                    if agg_filled_volume["filled_volume"] >= agg_filled_volume["volume"]
                    else "PartiallyFilled",
                }
            },
        )
        update_order_cmds.append(update_order_cmd)
        modify_order_ids.append(order_id)
    if update_order_cmds:
        context.database.accounts.bulk_write(update_order_cmds, session=session)


def _update_account_info(context, account_ids, session=None):
    """重新计算账户值"""

    positions = context.database.query(
        "positions", {"account_id": {"$in": account_ids}}, session=session
    )
    account_infos = {}
    update_positions = []
    for position in positions:
        if position.account_id not in account_infos:
            account_infos[position.account_id] = {
                "balance": 0,
                "frozen": 0,
                "marketvalue": 0,
                "fnl": 0,
            }
        if position.symbol == "CNY":
            cash = vxCashPosition(position)
            account_infos[position.account_id]["balance"] = cash.marketvalue
            account_infos[position.account_id]["frozen"] = cash.frozen
            update_positions.append(cash)
        else:
            account_infos[position.account_id]["marketvalue"] += position.marketvalue
            account_infos[position.account_id]["fnl"] += position.fnl
            update_positions.append(position)

    cur = context.database.query(
        "accounts", {"account_id": {"$in": list(account_ids)}}, session=session
    )

    update_account_infos = []
    for account_info in cur:
        update_dict = account_infos.get(account_info.account_id, {})
        account_info.update(**update_dict)
        logger.debug(f"更新后account_info:{account_info}")
        update_account_infos.append(account_info)

    context.database.save_many("positions", update_positions, session=session)
    context.database.save_many("accounts", update_account_infos, session=session)


@vxengine.event_handler("on_submit_algo_order_rebalance")
def pms_on_submit_algo_order_rebalance(context, event):
    """处理再平衡算法单：algo_order_type: Rebalance"""
    algo_order = event.data

    weights = algo_order.params["weights"]
    total_amount = algo_order.params["total_amount"]
    benchmark_marketvalues = {}
    if total_amount:
        df = pd.DataFrame(weights.values(), index=weights.keys(), columns=["weight"])

        df["weight"] = (
            df["weight"] / df["weight"].sum() if df["weight"].sum() > 0 else 0
        )
        df["target_amount"] = df["weight"] * total_amount
        benchmark_marketvalues = df["target_amount"].round(2).to_dict()
        benchmark_marketvalues.pop("CNY", None)

    cmds = [
        pymongo.UpdateMany(
            {
                "account_id": algo_order.account_id,
                "symbol": {"$ne": "CNY"},
            },
            {"$set": {"benchmark_marketvalue": 0}},
        )
    ]
    ticks = _update_ticks(context, *benchmark_marketvalues.keys())
    for symbol, benchmark_marketvalue in benchmark_marketvalues.items():
        _preset = vxMarketPreset(symbol)
        message = vxPosition(
            acount_id=algo_order.account_id,
            security_type=_preset.security_type,
            symbol=symbol,
            allow_t0=_preset.allow_t0,
        ).message
        message.pop("account_id", None)
        message.pop("benchmark_marketvalue", None)
        message.pop("lasttrade", None)
        cmds.append(
            pymongo.UpdateOne(
                {"account_id": algo_order.account_id, "symbol": symbol},
                {
                    "$set": {
                        "benchmark_marketvalue": benchmark_marketvalue,
                        "lasttrade": ticks[symbol].lasttrade
                        if symbol in ticks
                        else 1.0,
                    },
                    "$setOnInsert": message,
                },
                upsert=True,
            )
        )
    results = context.database.positions.bulk_write(
        cmds,
        ordered=True,
    )
    logger.info(f"更新持仓标准: {results}")


@vxengine.rpc_method("order_cancel", with_context=True)
def pms_order_cancel(context, *orders):
    """取消委托订单"""

    cancel_order_ids = [order.order_id for order in orders]

    cur = context.database.query(
        "orders",
        {
            "order_id": {"$in": cancel_order_ids},
            "status": {"$in": ["New", "PendingNew", "PartiallyFilled"]},
            # "exchange_order_id": {"$ne": ""},
        },
    )
    for order in cur:
        channel = context.agent_map.get(order.account_id, "simtest")
        context.publisher("on_submit_broker_order_cancel", order, channel=channel)
        logger.warning(
            f"account({order.account_id})通过 {channel} 发送 on_submit_broker_cancel"
            f" 取消委托订单: {order}"
        )
    return


def _update_ticks(context, *symbols) -> Dict:
    """更新ticks数据

    Returns:
        Dict -- Dict['symbol':vxTick]
    """
    now = vxtime.now()
    cached_symbols = context.database.distinct(
        "current",
        "symbol",
        {"symbol": {"$in": symbols}, "created_dt": {"$gt": now - 3}},
    )
    missing_symbols = set(symbols) - set(cached_symbols)
    if len(missing_symbols) > 0:
        for i in range(5):
            try:
                vxticks = context.hqfetcher(*missing_symbols)
                break
            except Exception as e:
                logger.warning(f"第{i+1}次获取missing_symbols错误...{e}")
                vxticks = {}

        if vxticks:
            context.database.save_many("current", vxticks.values())
    cur = context.database.query("current", {"symbol": {"$in": symbols}})
    return {vxtick.symbol: vxtick for vxtick in cur}


@vxengine.event_handler("on_tick")
def pms_on_tick(context, event):
    """更新positions的lasttrade"""

    before_trade_dt = vxtime.today("09:15:00")
    noonbreak_start_dt = vxtime.today("11:30:00")
    noonbreak_end_dt = vxtime.today("13:00:00")
    after_close_dt = vxtime.today("15:30:00")

    if not any(
        (
            before_trade_dt <= vxtime.now() < noonbreak_start_dt,
            noonbreak_end_dt <= vxtime.now() <= after_close_dt,
        )
    ):
        return

    symbols = context.database.positions.distinct("symbol", {"symbol": {"$ne": "CNY"}})

    if symbols:
        ticks = _update_ticks(context, *symbols)
        if ticks:
            context.database.positions.bulk_write(
                [
                    pymongo.UpdateMany(
                        {"symbol": symbol}, {"$set": {"lasttrade": tick.lasttrade}}
                    )
                    for symbol, tick in ticks.items()
                ],
                ordered=False,
            )


@vxengine.event_handler("on_tick")
def pms_on_monitor_position_benchmark(context, _) -> None:
    """监控仓位是否偏离预定值"""

    with context.database.start_session(lock=True) as session:
        unfinished_order_ids = context.database.orders.distinct(
            "order_id",
            {
                "order_id": {"$in": list(context.rebalance_orders.keys())},
                "status": {"$in": ["New", "PendingNew", "PartiallyFilled"]},
            },
            session=session,
        )

        context.rebalance_orders = {
            order_id: context.rebalance_orders[order_id]
            for order_id in unfinished_order_ids
        }

        cancel_orders = defaultdict(list)
        # 1分钟未成交委托，撤销后，再提交.
        expired_orders = context.database.query(
            "orders",
            {
                "order_id": {"$in": list(context.rebalance_orders.keys())},
                "status": {"$in": ["New", "PendingNew", "PartiallyFilled"]},
                "created_dt": {"$lt": vxtime.now() - 60},
            },
            session=session,
        )
        for order in expired_orders:
            channel = context.agent_map.get(order.account_id, "simtest")
            cancel_orders[channel].append(order)
            logger.info(f"委托订单{order.order_id} 超1分钟未成交，撤销再下单.")

        _check_position_marketvalue_above_benchmark(context, session)
        _check_position_marketvalue_below_benchmark(context, session)

        if not context.pending_order_queue.empty():
            vxengine.event_handler.trigger(vxEvent(type="on_submit_order_batch"))

        for channel, orders in cancel_orders.items():
            context.publisher(
                "on_submit_broker_order_batch_cancel", data=orders, channel=channel
            )
            logger.info(f"通过{channel} 下发取消委托订单: {len(orders)}个")


def _check_position_marketvalue_above_benchmark(context, session=None):
    """检查position 的marketvalue 是否大于benchmark，需要执行卖出操作"""
    cur = context.database.positions.aggregate(
        [
            {
                "$match": {
                    "benchmark_marketvalue": {"$gte": 0},
                    "symbol": {"$ne": "CNY"},
                    "position_id": {"$nin": list(context.rebalance_orders.values())},
                }
            },
            {
                "$project": {
                    "account_id": "$account_id",
                    "position_id": "$position_id",
                    "symbol": "$symbol",
                    "lasttrade": "$lasttrade",
                    "volume": "$volume",
                    "available": "$available",
                    "marketvalue": {"$multiply": ["$lasttrade", "$volume"]},
                    "benchmark_marketvalue": "$benchmark_marketvalue",
                    "diff": {
                        "$subtract": [
                            {"$multiply": ["$lasttrade", "$volume"]},
                            "$benchmark_marketvalue",
                        ],
                    },
                    "gap": {
                        "$subtract": [
                            {"$multiply": ["$lasttrade", "$volume"]},
                            {"$multiply": ["$benchmark_marketvalue", 1.05]},
                        ]
                    },
                }
            },
            {"$match": {"gap": {"$gt": 0}}},
            {"$sort": {"diff": -1}},
        ],
        session=session,
    )

    order_update_cmds = []

    for agg_diff in cur:
        _preset = vxMarketPreset(agg_diff["symbol"])
        diff_volume = (
            abs(agg_diff["diff"])
            / agg_diff["lasttrade"]
            // _preset.volume_unit
            * _preset.volume_unit
        )
        volume = min(
            diff_volume,
            agg_diff["available"],
        )

        if volume == 0:
            logger.debug(f"账户({agg_diff['account_id']}) 卖出仓位volume 为0，暂无需调整 ")
            continue

        ret_cur = context.database.positions.update_one(
            {
                "account_id": agg_diff["account_id"],
                "symbol": agg_diff["symbol"],
                "available": {"$gte": volume},
            },
            {"$inc": {"frozen": volume, "available": -volume}},
        )
        if ret_cur.matched_count == 0:
            logger.error(
                f"账户({agg_diff['account_id']})"
                f" symbol({agg_diff['symbol']})冻结仓位:{volume} 失败。"
            )
            continue

        gateway_order = vxOrder(
            account_id=agg_diff["account_id"],
            frozen_position_id=agg_diff["position_id"],
            symbol=agg_diff["symbol"],
            order_direction="Sell",
            order_offset="Close",
            order_type="Limit",
            volume=volume,
            price=agg_diff["lasttrade"],
            status=OrderStatus.PendingNew,
        )
        context.pending_order_queue.put_nowait(gateway_order)
        context.rebalance_orders[gateway_order.order_id] = agg_diff["position_id"]
        order_update_cmds.append(
            pymongo.UpdateOne(
                {"order_id": gateway_order.order_id},
                {"$set": gateway_order.message},
                upsert=True,
            )
        )

    if order_update_cmds:
        context.database.orders.bulk_write(
            order_update_cmds, ordered=False, session=session
        )


def _check_position_marketvalue_below_benchmark(context, session=None):
    """检查低于标准benchmark的持仓，买入相应的仓位"""
    cur = context.database.positions.aggregate(
        [
            {
                "$match": {
                    "benchmark_marketvalue": {"$gte": 0},
                    "symbol": {"$ne": "CNY"},
                    "position_id": {"$nin": list(context.rebalance_orders.values())},
                }
            },
            {
                "$project": {
                    "account_id": "$account_id",
                    "position_id": "$position_id",
                    "symbol": "$symbol",
                    "lasttrade": "$lasttrade",
                    "volume": "$volume",
                    "available": "$available",
                    "marketvalue": {"$multiply": ["$lasttrade", "$volume"]},
                    "benchmark_marketvalue": "$benchmark_marketvalue",
                    "diff": {
                        "$subtract": [
                            "$benchmark_marketvalue",
                            {"$multiply": ["$lasttrade", "$volume"]},
                        ],
                    },
                    "gap": {
                        "$subtract": [
                            {"$multiply": ["$benchmark_marketvalue", 0.95]},
                            {"$multiply": ["$lasttrade", "$volume"]},
                        ]
                    },
                }
            },
            {"$match": {"gap": {"$gt": 0}}},
            {"$sort": {"diff": -1}},
        ],
        session=session,
    )
    order_update_cmds = []

    for agg_diff in cur:
        # 需要买入股票

        _preset = vxMarketPreset(agg_diff["symbol"])
        diff_volume = (
            abs(agg_diff["diff"])
            / agg_diff["lasttrade"]
            // _preset.volume_unit
            * _preset.volume_unit
        )

        item = context.database.positions.find_one(
            {"account_id": agg_diff["account_id"], "symbol": "CNY"}, {"_id": 0}
        )
        cash = vxCashPosition(item)

        volume = min(
            diff_volume,
            cash.available / 1.003 // _preset.volume_unit * _preset.volume_unit,
        )
        if volume == 0:
            logger.debug(f"账户({agg_diff['account_id']}) 买入仓位为0，暂不调整.")
            continue
        frozen_amount = volume * agg_diff["lasttrade"] * 1.003
        ret_cur = context.database.positions.update_one(
            {
                "account_id": cash.account_id,
                "symbol": "CNY",
                "available": {"$gte": frozen_amount},
            },
            {"$inc": {"frozen": frozen_amount, "available": -frozen_amount}},
        )
        if ret_cur.matched_count == 0:
            logger.error(
                f"账户({agg_diff['account_id']}) symbol(agg_diff['symbol'])"
                f" 冻结CNY仓位:{frozen_amount} 失败。"
            )
            continue

        context.database.accounts.update_one(
            {"account_id": cash.account_id},
            {"$inc": {"frozen": frozen_amount, "available": -frozen_amount}},
        )
        logger.info(f"差距：{agg_diff}")

        gateway_order = vxOrder(
            account_id=agg_diff["account_id"],
            frozen_position_id=cash.position_id,
            symbol=agg_diff["symbol"],
            order_direction="Buy",
            order_offset="Open",
            order_type="Limit",
            volume=volume,
            price=agg_diff["lasttrade"],
            status=OrderStatus.PendingNew,
        )
        context.pending_order_queue.put_nowait(gateway_order)
        context.rebalance_orders[gateway_order.order_id] = agg_diff["position_id"]

        order_update_cmds.append(
            pymongo.UpdateOne(
                {"order_id": gateway_order.order_id},
                {"$set": gateway_order.message},
                upsert=True,
            )
        )

    if order_update_cmds:
        context.database.orders.bulk_write(
            order_update_cmds, ordered=False, session=session
        )


@vxengine.event_handler("on_submit_order_batch")
def pms_on_submit_order_batch(context, event):
    """批量提交委托订单"""

    if event.data:
        [context.pending.order_queue.put_nowait(vxorder) for vxorder in event.data]

    with contextlib.suppress(Empty):
        gateway_orders = defaultdict(list)
        while not context.pending_order_queue.empty():
            order = context.pending_order_queue.get_nowait()
            channel = context.agent_map.get(order.account_id, "simtest")
            gateway_orders[channel].append(order)
            logger.info(f"通过channel({channel}) 提交: {order}")

    for channel, orders in gateway_orders.items():
        context.publisher("on_submit_broker_order_batch", data=orders, channel=channel)


@vxengine.rpc_method("create_account", with_context=True)
def pms_create_account(
    context,
    account_id: str = None,
    balance: float = 1_000_000,
    portfolio_id: str = "",
    channel_name: str = None,
    if_exists: str = "skip",
) -> str:
    """创建账户

    Keyword Arguments:
        account_id {str} -- 账户id (default: {None})
        balance {float} -- 初始余额 (default: {1_000_000})
        portfolio_id {str} -- 组合id (default: {""})
        channel_name {str} -- 下单通道，缺省为空 (default: {None})
        if_exists {str} -- 若存在账户已存在(default: {"skip"})
                            'delete' ---> 删除原来账户
                            'skip' --->  跳过
                            'raise' ---> raise 一个exception


    Raises:
        ValueError: 账户已存在时，且if_exists == 'raise' 则raise一个exception

    Returns:
        str -- _description_
    """

    channel_name = channel_name or "simtest"

    if context.database.accounts.count_documents({"account_id": account_id}) > 0:
        if if_exists == "skip":
            return account_id
        elif if_exists == "delete":
            context.database.accounts.delete_many({"account_id": account_id})
            context.database.positions.delete_many({"account_id": account_id})
            context.database.orders.delete_many({"account_id": account_id})
            context.database.trades.delete_many({"account_id": account_id})
        elif if_exists == "raise":
            raise ValueError(f"account_id({account_id}) 已存在。")

    account_id = account_id or str(uuid.uuid4())
    account_info = vxAccountInfo(
        account_id=account_id,
        portfolio_id=portfolio_id,
        deposit=balance,
        balance=balance,
        fund_shares=balance,
        fund_nav_yd=1.0,
        settle_day=vxtime.today("00:00:00") - 60 * 60 * 24,
    )

    cash_position = vxCashPosition(
        portfolio_id=portfolio_id,
        account_id=account_id,
        volume_today=balance,
    )

    with context.database.start_session() as session:
        context.database.save("accounts", account_info, session=session)
        context.database.save("positions", cash_position, session=session)
        context.database.agent_mapping.update_one(
            {"account_id": account_id},
            {"$set": {"channel_name": channel_name}},
            upsert=True,
        )
        context.agent_map[account_id] = channel_name
        _update_account_info(context, [account_id])


@vxengine.rpc_method("deposit", with_context=True)
def pms_deposit(context, account_id, money: float) -> None:
    """转入金额"""

    account_info = context.database.accounts.find_one(
        {"account_id": account_id}, {"_id": 0}
    )
    if account_info is None:
        raise ValueError(f"账户信息不存在: {account_id}")
    account_info = vxAccountInfo(account_info)

    cash_position = context.database.positions.find_one(
        {"account_id": account_id, "symbol": "CNY"}, {"_id": 0}
    )
    cash_position = vxCashPosition(cash_position)
    logger.info(f"{account_info.nav}, {money}")

    account_info.fund_shares += money / account_info.fund_nav
    account_info.deposit += money
    account_info.balance += money
    cash_position.volume_today += money
    logger.info(f"{account_info.nav}, {money},{cash_position.marketvalue}")

    with context.database.start_session() as session:
        context.database.save("accounts", account_info, session=session)
        context.database.save("positions", cash_position, session=session)

        _update_account_info(context, [account_id], session=session)


@vxengine.rpc_method("withdraw", with_context=True)
def withdraw(context, account_id, money: float) -> None:
    """转出金额"""
    if money <= 0:
        raise IllegalPrice(f"转出金额 {money} <= 0 错误.")

    with context.database.start_session(causal_consistency=True) as session:
        cash = context.database.query_one(
            "positions",
            {"account_id": account_id, "symbol": "CNY"},
            session=session,
        )
        cash = vxCashPosition(cash)
        if money > cash.available:
            raise NoEnoughCash(f"转出金额{money} 大于可用金额 {cash.available}。 ")
        account_info = context.database.query_one(
            "accounts", {"account_id": account_id}, session=session
        )

        account_info.withdraw += money
        account_info.fund_shares -= money / account_info.fund_nav
        account_info.balance -= money

        if money < cash.volume_his:
            cash.volume_his -= money
        else:
            money -= cash.volume_his
            cash.volume_his = 0
            cash.volume_today -= money

        context.database.save("accounts", account_info, session=session)
        context.database.save("positions", cash, session=session)
        _update_account_info(context, [account_id], session=session)


@vxengine.rpc_method("get_account", with_context=True)
def pms_get_account(context, account_id: str, session=None) -> vxAccountInfo:
    """获取账户信息

    Arguments:
        account_id {str} -- 账户id

    Returns:
        vxAccountInfo -- 账户信息
    """
    logger.info(f"account_id({account_id}) session: {session}")
    account_info = context.database.query_one(
        "accounts", {"account_id": account_id}, session=session
    )
    if not account_info:
        return {}

    account_info.fnl = 0
    account_info.marketvalue = 0
    cur = context.database.query("positions", {"account_id": account_id})
    for position in cur:
        if position.symbol == "CNY":
            account_info.balance = position.marketvalue
            account_info.frozen = position.frozen
        else:
            account_info.fnl += position.fnl
            account_info.marketvalue += position.marketvalue

    return account_info


@vxengine.rpc_method("get_positions", with_context=True)
def pms_get_positions(context, account_id: str, symbol: str = None) -> Dict:
    """获取相应的持仓信息

    Arguments:
        account_id {str} -- account_id 账户id
        symbol {str} -- 持仓信息 (default: {None})

    Returns:
        Dict -- Dict['account_id': vxAccountInfo]
    """
    filter_ = {"account_id": account_id}
    if symbol:
        filter_["symbol"] = symbol
    cur = context.database.query("positions", filter_)
    return {position.symbol: position for position in cur}


@vxengine.rpc_method("get_orders", with_context=True)
def get_orders(
    context,
    account_id: str,
    order_id: str = None,
    exchange_order_id: str = None,
    is_unfinished=False,
) -> Dict:
    """获取成交订单信息

    Arguments:
        account_id {str} -- 账户id

    Keyword Arguments:
        order_id {str} -- 委托订单id (default: {None})
        exchange_order_id {str} -- 交易所委托订单id (default: {None})
        is_unfinished {bool} -- 是否未完成 (default: {False})

    Returns:
        Dict -- Dict['order_id': vxOrder]
    """
    filter_ = {"account_id": account_id}
    if order_id:
        filter_["order_id"] = order_id
    if exchange_order_id:
        filter_["exchange_order_id"] = exchange_order_id
    if is_unfinished:
        filter_["status"] = {"$in": ["New", "PendingNew", "PartiallyFilled"]}

    cur = context.database.query("orders", filter_)
    return {o.order_id: o for o in cur}


@vxengine.rpc_method("get_trades", with_context=True)
def get_trades(
    context,
    account_id: str,
    order_id: str = None,
    trade_id: str = None,
    exchange_order_id: str = None,
) -> Dict:
    """获取成交信息

    Arguments:
        account_id {str} -- 账户id

    Keyword Arguments:
        order_id {str} -- 委托订单id (default: {None})
        trade_id {str} -- 成交回报id (default: {None})
        exchange_order_id {str} -- 交易所委托订单id (default: {None})

    Returns:
        Dict -- Dict['trade_id':vxTrade]
    """
    filter_ = {"account_id": account_id}
    if order_id:
        filter_["order_id"] = order_id

    if trade_id:
        filter_["trade_id"] = trade_id

    if exchange_order_id:
        filter_["exchange_order_id"] = exchange_order_id

    cur = context.database.query("trades", filter_)
    return {t.trade_id: t for t in cur}


@vxengine.rpc_method("order_volume", with_context=True)
def pms_order_volume(
    context,
    account_id: str,
    symbol: str,
    volume: int,
    price: float = 0.0,
    algo_order_id: str = "",
) -> vxOrder:
    """委托交易volume的symbol证券

    Arguments:
        account_id {str} -- 交易账号
        symbol {str} -- 目标证券代码
        volume {int} -- volume> 0时，表示买入，volume < 0时，表示卖出
        price {float} -- price 为0 时，则表示市价单，price > 0 时，表示限价单 (default: {0.0})

    Returns:
        vxOrder -- 委托订单号
    """
    with context.database.start_session(causal_consistency=True, lock=True) as session:
        order = vxOrder(
            account_id=account_id,
            algo_order_id=algo_order_id,
            symbol=symbol,
            status="PendingNew",
        )

        if price < 0.0:
            raise ValueError(f"委托价格({price})必须大于等于0.")
        elif price == 0:
            _preset = vxMarketPreset(order.symbol)

            order.order_type = (
                "Limit"
                if _preset.security_type == SecType.BOND_CONVERTIBLE
                else "Market"
            )

            tick = _update_ticks(context, order.symbol)

            order.price = (
                tick[order.symbol].bid1_p if volume < 0 else tick[order.symbol].ask1_p
            )
        else:
            order.order_type = "Limit"
            order.price = price

        if volume == 0:
            raise ValueError("委托volume 不可以为0.")

        elif volume > 0:
            order.order_direction = "Buy"
            order.order_offset = "Open"
            order.volume = volume
            frozen_position = context.database.query_one(
                "positions",
                {"account_id": account_id, "symbol": "CNY"},
                session=session,
            )
            frozen_position = vxCashPosition(frozen_position)
            frozen_amount = order.volume * order.price * 1.003
            if frozen_amount > frozen_position.available:
                raise NoEnoughCash(
                    f"Buy {symbol} volume({order.volume}) on price({order.price})"
                    f" frozen {frozen_amount} > {frozen_position.available}"
                )
            order.frozen_position_id = frozen_position.position_id
            frozen_position.frozen += frozen_amount
        else:
            order.order_direction = "Sell"
            order.order_offset = "Close"
            order.volume = abs(volume)
            frozen_position = context.database.query_one(
                "positions",
                {"account_id": account_id, "symbol": symbol},
                session=session,
            )
            if not frozen_position or frozen_position.available < order.volume:
                raise NoEnoughPosition(
                    f"Sell {symbol} volume({order.volume})"
                    f" 可用持仓:({frozen_position.available if frozen_position else 0})."
                )
            order.frozen_position_id = frozen_position.position_id
            frozen_position.available += order.volume

        context.database.save("orders", order, session=session)
        context.database.save("positions", frozen_position, session=session)

        _update_frozens(context, [account_id], session=session)
        _update_account_info(context, [account_id], session=session)

        channel = context.agent_map.get(account_id, "simtest")
        context.publisher("on_submit_broker_order", data=order, channel=channel)
        logger.warning(
            f"account({account_id}) 通过channel({channel}) 发送"
            f" on_submit_broker_order 委托订单: {order}"
        )
        return order


@vxengine.rpc_method("algo_order", with_context=True)
def pms_algo_order(context, account_id, algo_order_type, params: Dict) -> Any:
    """算法委托单"""
    algo_order = vxAlgoOrder(
        account_id=account_id,
        algo_order_type=algo_order_type,
        params=params,
        status="New",
    )
    context.database.algo_orders.update_one(
        {"algo_order_id": algo_order.algo_order_id}, {"$set": algo_order.message}
    )
    logger.info(f"提交算法委托 : {algo_order}.")
    vxengine.event_handler.trigger(
        vxEvent(
            type=f"on_submit_algo_order_{algo_order.algo_order_type.name.lower()}",
            data=algo_order,
        )
    )
    return algo_order


@vxengine.rpc_method("algo_order_cancel", with_context=True)
def pms_algo_order_cancel(context, algo_order) -> Any:
    """取消算法委托单"""
    # algo_order = context.database.algo_orders.find_one
    pass
