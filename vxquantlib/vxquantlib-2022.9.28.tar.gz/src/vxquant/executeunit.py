"""Agent 模板"""
import argparse
from multiprocessing import Lock
from vxutils import logger, vxtime, import_tools, to_timestring
from vxsched import vxContext, vxEvent, vxIntervalTrigger, vxscheduler, vxDailyTrigger
from vxquant.model.exchange import vxOrder, OrderStatus

_default_agent_config = {
    "agent_name": "",
    "publisher": {},
    "subscribers": [],
    "tdapi": {},
}


@vxscheduler.handler("__init__")
def agent_init(context: vxContext, _) -> None:
    """agent 初始化"""
    context.lock = Lock()
    context.pending_broker_orders = {}
    context.pending_broker_trades = {}
    context.gateway_orders = {}

    # 发送agent_init 的消息，请求gateway返回当前agent正在运行的gateway orders
    context.publisher("sync_orders", data=context.agent_name)
    vxscheduler.submit_event("on_monitor", trigger=vxIntervalTrigger(1))
    vxscheduler.submit_event("on_settle", trigger=vxDailyTrigger("16:00:00"))


@vxscheduler.handler("on_reply_sync_orders")
def on_reply_sync_orders(context: vxContext, event: vxEvent) -> None:
    """收到gateway回复agent_init 消息"""
    gateway_orders, gateway_trades = event.data

    # with context.lock:
    #    context.database.savemany(*gateway_orders.values())
    for gateway_order in gateway_orders.values():
        context.gateway_orders[gateway_order.exchange_order_id] = gateway_order

    broker_trades = context.tdapi.get_execution_reports()
    missing_trades = set(broker_trades.keys()) - set(gateway_trades.keys())

    for trade_id in missing_trades:
        vxscheduler.submit_event("on_broker_trade_status", broker_trades[trade_id])
    logger.info(f"更新missing_trades 至 pending_broker_trades: {missing_trades}")

    logger.info(f"=== broker_orders 处理完成。共缺失{len(missing_trades)}个broker_trade。")

    broker_orders = context.tdapi.get_orders()
    for gateway_order in gateway_orders:
        if not gateway_order.exchange_order_id:
            logger.warning(
                f"WARNING: gateway order({gateway_order.order_id})"
                " 无exchange_order_id信息，请核实.."
            )
            continue

        broker_order = broker_orders.pop(gateway_order.exchange_order_id, None)
        if broker_order is None:
            logger.warning(
                f"WARNING: gateway order({gateway_order.order_id})"
                " 无exchange_order_id信息，请核实.."
            )
            continue

        if (
            broker_order.status == gateway_order.status
            and broker_order.filled_volume == gateway_order.filled_volume
        ):
            logger.debug(
                f"WARNING: gateway order({gateway_order.order_id}) the same with broker"
                f" order({broker_order.exchange_order_id}) status:"
                f" {gateway_order.status}"
            )
            continue

        vxscheduler.submit_event("on_broker_order_status", broker_order)


@vxscheduler.handler("on_submit_broker_order")
def on_recv_gateway_order(context, event):
    """收到gateway下发的委托订单"""
    logger.info(f"通过{event.channel} 收到委托订单: {event.data}")
    gateway_order = event.data
    with context.lock:
        (broker_order,) = context.tdapi.order_batch(gateway_order)
        gateway_order.exchange_order_id = broker_order.exchange_order_id
        gateway_order.status = OrderStatus.New
        # context.database.gateway_orders.save(gateway_order)
        context.gateway_orders[gateway_order.exchange_order_id] = gateway_order

    logger.info(
        f"通过{context.publisher.channel_name} 上报 on_order_status 更新 : {gateway_order}"
    )
    context.publisher("on_order_status", gateway_order)


@vxscheduler.handler("on_submit_broker_order_cancel")
def on_recv_gateway_order_cancel(context, event):
    """收到gateway下发的取消委托订单"""
    logger.info(f"通过{event.channel} 收到取消委托订单: {event.data}")
    gateway_order = event.data
    context.tdapi.order_cancel(gateway_order)


@vxscheduler.handler("on_broker_order_status")
def on_broker_order_status(context, event):
    """收到券商柜台订单更新"""
    logger.info(f"通过{event.channel} 收到交易所订单更新: {event.data}")
    broker_order = event.data
    exchange_order_id = broker_order.exchange_order_id
    with context.lock:
        try:
            gateway_order = context.gateway_orders[exchange_order_id]

            if gateway_order.status in [
                OrderStatus.Rejected,
                OrderStatus.Suspended,
                OrderStatus.Canceled,
                OrderStatus.Expired,
                OrderStatus.Filled,
            ]:
                logger.warning(
                    f"gateway_order({gateway_order.order_id})已终结，当前状态:"
                    f" {gateway_order.status}, 收到broker_order更新: {broker_order}"
                )
                return

            if gateway_order.filled_volume > broker_order.filled_volume:
                logger.warning(
                    f"gateway_order({gateway_order.order}) 已成交"
                    f" {gateway_order.filled_volume} > 收到broker更新成交:"
                    f" {broker_order.filled_volume} 忽略更新: {broker_order}"
                )
                return

            gateway_order.status = broker_order.status
            gateway_order.filled_volume = broker_order.filled_volume
            gateway_order.filled_amount = broker_order.filled_amount
            gateway_order.updated_dt = broker_order.updated_dt
            context.gateway_orders[gateway_order.exchange_order_id] = gateway_order

        except KeyError:
            if broker_order.status in [
                OrderStatus.Rejected,
                OrderStatus.Suspended,
                OrderStatus.Canceled,
                OrderStatus.Expired,
                OrderStatus.Filled,
            ]:
                context.pending_broker_orders[exchange_order_id] = broker_order
                logger.warning(
                    f"加入pengding broker orders中: exchange_order_id={exchange_order_id}"
                )

            if (
                exchange_order_id not in context.pending_broker_orders
                or context.pending_broker_orders[exchange_order_id].filled_volume
                < broker_order.filled_volume
            ):
                context.pending_broker_orders[exchange_order_id] = broker_order
                logger.warning(
                    "加入pengding broker orders中:"
                    f" exchange_order_id={exchange_order_id} filled_volume={broker_order.filled_volume}"
                )

            return

    logger.info(
        f"通过{context.publisher.channel_name} 上报 on_order_status 更新 : {gateway_order}"
    )
    context.publisher("on_order_status", gateway_order)


@vxscheduler.handler("on_broker_execution_report")
@vxscheduler.handler("on_broker_trade_status")
def on_broker_trade_status(context, event):
    """收到券商柜台成交回报信息"""
    logger.info(f"通过{event.channel} 收到交易所订单更新: {event.data}")
    broker_trade = event.data

    with context.lock:
        try:
            # * gateway_order = next(
            # *     context.database.gateway_orders.find(
            # *         f"exchange_order_id = '{broker_trade.exchange_order_id}'"
            # *     )
            # * )
            gateway_order = context.gateway_orders[broker_trade.exchange_order_id]

            broker_trade.order_id = gateway_order.order_id
            broker_trade.account_id = gateway_order.account_id

            logger.info(
                f"通过{context.publisher.channel_name} 上报 on_execution_reports_status 更新"
                f" : {broker_trade}"
            )
            context.publisher("on_execution_report", broker_trade)

        except KeyError:
            if (
                broker_trade.trade_id not in context.pending_broker_trades
                or context.pending_broker_trades[broker_trade.trade_id].updated_dt
                < broker_trade.updated_dt
            ):
                context.pending_broker_trades[broker_trade.trade_id] = broker_trade


@vxscheduler.handler("on_monitor")
def on_monitor_order(context, _) -> None:
    """订单监控"""
    if context.pending_broker_trades:
        with context.lock:
            broker_trades, context.pending_broker_trades = (
                context.pending_broker_trades,
                {},
            )
        for broker_trade in broker_trades.values():
            if broker_trade.exchange_order_id in context.gateway_orders:
                vxscheduler.submit_event(
                    "on_broker_execution_reports_status", broker_trade
                )
            else:
                with context.lock:
                    context.pending_broker_trades[
                        broker_trade.exchange_order_id
                    ] = broker_trade

    if context.pending_broker_orders:
        with context.lock:
            broker_orders, context.pending_broker_orders = (
                context.pending_broker_orders,
                {},
            )

        for broker_order in broker_orders.values():
            if broker_order.exchange_order_id in context.gateway_orders:
                vxscheduler.submit_event("on_broker_order_status", broker_order)
            else:
                with context.lock:
                    context.pending_broker_orders[
                        broker_order.exchange_order_id
                    ] = broker_order


@vxscheduler.handler("__stop__")
def on_stop_scheduler(context, _) -> None:
    """停止运行"""
    vxscheduler.stop()


@vxscheduler.handler("on_settle")
@vxscheduler.handler("__on_sync__")
def agent_on_settle(context, _):
    """日结函数"""
    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info(f"======== 日结开始 {to_timestring(vxtime.now(), '%Y-%m-%d')} ========")

    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info("=" * 60)

    logger.info(f"处理pending broker trades {len(context.pending_broker_trades)}个...")
    for broker_trade in context.pending_broker_trades.values():
        logger.info(f"删除未处理broker trade: {broker_trade}")
    context.pending_broker_trades = {}
    logger.info("=" * 60)

    logger.info(f"处理pending broker orders {len(context.pending_broker_orders)}个...")
    for broker_order in context.pending_broker_orders.values():
        logger.info(f"删除未处理broker trade: {broker_order}")
    context.pending_broker_orders = {}
    logger.info("=" * 60)

    try:
        account_info = context.tdapi.get_account()
        positions = context.tdapi.get_positions()
        orders = context.tdapi.get_orders()
        trades = context.tdapi.get_execution_reports()
        sync_data = {
            "account_info": account_info,
            "positions": positions,
            "orders": orders,
            "trades": trades,
        }
        context.publisher("on_sync", sync_data)
        logger.info(f"上报同步数据方案 {sync_data}")

    except Exception as e:
        logger.error(f"ERROR: collecting sync data error: {e}")

    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info(f"======== 日结结束 {to_timestring(vxtime.now(), '%Y-%m-%d')} ========")
    logger.info("=" * 60)
    logger.info("=" * 60)
    logger.info("=" * 60)


def init_agent(config_file: str, mode="listener") -> None:
    """初始化agent

    Arguments:
        config_file {str} -- 配置文件
    """
    config = vxContext.load_json(config_file, _default_agent_config)
    vxscheduler.context.update(config)
    logger.info(f"设定agent_name: {vxscheduler.context.agent_name}")

    if config.publisher:
        vxscheduler.context.publisher = import_tools(
            config.publisher["class"], config.publisher["params"]
        )
    else:
        vxscheduler.context.publisher = None
        logger.warning("上报成交信息的发布器参数缺失，请设置后运行。vxscheduler.publisher = [YOUR PUBLISHER]")

    for sub_config in config.subscribers:
        subscriber = import_tools(sub_config["class"], sub_config["params"])
        vxscheduler.subscribe(subscriber)
        logger.info(f"增加subscriber: {subscriber}")

    if config.tdapi:
        vxscheduler.context.tdapi = import_tools(
            config.tdapi["class"], config.tdapi["params"]
        )
    else:
        vxscheduler.context.tdapi = None
        logger.warning("下单接口参数确实，请自行设置: vxscheduler.tdapi = [YOUR TDAPI]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""zmq event broker server""")
    parser.add_argument(
        "-c",
        "--config",
        help="path to config json file",
        default="etc/agent.json",
        type=str,
    )
    parser.add_argument(
        "-v", "--verbose", help="debug 模式", action="store_true", default=False
    )

    args = parser.parse_args()
    if args.verbose:
        logger.setLevel("DEBUG")
    vxContext(_default_agent_config).save_json("etc/agent.json")

    init_agent(args.config)

    if not vxscheduler.context.publisher:
        raise ValueError(
            "上报成交信息的发布器参数缺失，请设置后运行。vxscheduler.publisher = [YOUR PUBLISHER]"
        )

    if not vxscheduler.context.tdapi:
        raise ValueError("下单接口参数确实，请自行设置: vxscheduler.tdapi = [YOUR TDAPI]")

    vxscheduler.start()
