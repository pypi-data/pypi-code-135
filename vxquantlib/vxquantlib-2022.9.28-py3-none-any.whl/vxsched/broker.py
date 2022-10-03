"""发布者/订阅者"""
import asyncio
import contextlib

from collections import defaultdict
import itertools

from multiprocessing.dummy import Pool
from queue import Empty, PriorityQueue, Queue
from typing import Union, Callable, Any
from vxsched import (
    vxContext,
    vxEventHandlers,
    vxEventQueue,
    vxIntervalTrigger,
)
import zmq

from vxutils import (
    vxtime,
    logger,
    to_text,
    to_binary,
    to_timestring,
)
from vxutils.zmqsocket import vxZMQContext, vxAsyncZMQContext
from vxsched.event import TriggerStatus, vxEvent, vxTrigger

__INTERNAL_ZMQFORMAT__ = "ipc://vxquant.internal.ipc"


class vxZMQBrokerServerv0:
    """消息分发器"""

    def __init__(
        self,
        frontend_url: str = "tcp://127.0.0.1:12306",
        frontend_sercet_key: str = "",
        backend_url: str = __INTERNAL_ZMQFORMAT__,
        backend_sercet_key: str = "",
    ) -> None:
        self._active = False
        self._queue = vxEventQueue("eventbroker")
        self._pool = None

        self._ctx = vxZMQContext().instance()

        self._frontend_url = frontend_url
        self._frontend_sercet_key = frontend_sercet_key
        self._frontend = None
        self._backend_url = backend_url
        self._backend_sercet_key = backend_sercet_key
        self._backend = None
        self._transfer_to = defaultdict(list)
        self._subscribers = []

    def transfer_to(self, channel_name: str, publisher: Callable):
        """将消息通道channel_name消息转发至 publisher上

        Arguments:
            channel_name {str} -- 待转发的消息通道
            publisher {Callable} -- 发布器
        """
        if publisher not in self._transfer_to[channel_name]:
            self._transfer_to[channel_name].append(publisher)

    def fetch_from(self, subscriber: Callable):
        """从外部获取消息

        Arguments:
            subscriber {Callable} -- 订阅器
        """
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def server_forever(self) -> None:
        """开始执行服务"""
        try:
            if self._active:
                logger.warning("server 已经启动了，请勿重复启动 ...")
                return

            self._active = True
            logger.info(f"{self.__class__.__name__} 开始启动 ...")

            self._pool = Pool(16)
            sender = self._pool.apply_async(self.handle_send_event)
            recver = self._pool.apply_async(self.handle_recv_event)
            self._pool.map(self.handle_subscribe_event, self._subscribers)
            sender.get()
            recver.get()

        finally:
            self.stop()
            logger.info("{self.__class__.__name__} 运行结束...")

    def stop(self):
        """暂停运行"""
        self._active = False
        if self._frontend:
            self._frontend.close()

        if self._backend:
            self._backend.close()

        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None

    def submit_event(
        self,
        event: Union[str, vxEvent],
        data: Any = "",
        trigger: vxTrigger = None,
        priority: float = 10,
        **kwargs,
    ) -> None:
        """发布消息

        Arguments:
            event {Union[str, vxEvent]} -- 要推送消息或消息类型
            data {Any} -- 消息数据信息 (default: {None})
            trigger {Optional[vxTrigger]} -- 消息触发器 (default: {None})
            priority {int} -- 优先级，越小优先级越高 (default: {10})
        """

        if isinstance(event, str):
            send_event = vxEvent(
                type=event,
                data=data,
                trigger=trigger,
                priority=priority,
                **kwargs,
            )

        else:
            send_event = event

        logger.debug(f"提交消息: {send_event}")
        self._queue.put_nowait(send_event)

    def handle_recv_event(self) -> None:
        """处理前端相关内容"""

        self._frontend = self._ctx.socket(zmq.XSUB)
        self._frontend.bind(self._frontend_url, self._frontend_sercet_key)
        self._frontend.send(b"\x01")
        logger.info(
            f"开始监听frontend: {self._frontend_url} with key_file:"
            f" {self._frontend_sercet_key}"
        )

        while self._active:
            with self._frontend.lock:
                if self._frontend.poll(100, zmq.POLLIN) == 0:
                    continue

                (
                    channel,
                    controll_tag,
                    msg_body,
                ) = self._frontend.recv_multipart()

                ack_msg = b""
                if controll_tag == b"PUBSUB":
                    recv_event = vxEvent.unpack(msg_body)
                    recv_event.channel = to_text(channel)
                    logger.info(f"frontend: 收到event: ({recv_event})")
                    ack_msg = to_binary(recv_event.id)

                elif controll_tag == b"READY":
                    ack_msg = b"ack" + msg_body
                    logger.debug(
                        f"{to_text(channel)} is ready,send ack {to_text(ack_msg)}..."
                    )
                else:
                    logger.warning(f"未支持的方法  {controll_tag},channel={channel}")
                    continue

                ack_msgs = [channel, b"ACK", ack_msg]
                if self._frontend.poll(1000, zmq.POLLOUT) == 0:
                    logger.warning(f"发送确认信息超时 返回信息:{ack_msgs}.")
                else:
                    self._frontend.send_multipart(ack_msgs)
                    if controll_tag == b"PUBSUB":
                        self.submit_event(recv_event)

        logger.info(
            f"停止监听frontend: {self._frontend_url} with key_file:"
            f" {self._frontend_sercet_key}"
        )

    def handle_send_event(self) -> None:
        """发送event消息"""

        self._backend = self._ctx.socket(zmq.XPUB)
        self._backend.bind(self._backend_url, self._backend_sercet_key)
        logger.info(
            f"开始监听backend: {self._backend_url} with key_file:"
            f" {self._backend_sercet_key}"
        )

        while self._active:
            if self._queue.empty():
                vxtime.sleep(0.1)
                continue

            event = self._queue.get_nowait()

            message = event.message
            message["trigger"] = None
            message["next_trigger_dt"] = event.trigger.last_trigger_dt
            send_event = vxEvent(**message)

            self._pool.apply_async(self._send_event, args=(send_event,))

            publishers = self._transfer_to.get(send_event.channel, [])
            for publisher in publishers:
                self._pool.apply_async(publisher, args=(send_event,))
                logger.info(
                    f"转发消息({send_event.id} == {send_event.type} =="
                    f" {send_event.channel})至 {publisher}"
                )

    def _send_event(self, event: vxEvent) -> None:
        channel = to_binary(event.channel)
        packed_event = vxEvent.pack(event)
        with self._backend.lock:
            if self._backend.poll(100, zmq.POLLIN) != 0:
                self._backend.send_multipart([channel, b"PUBSUB", packed_event])
                logger.debug(f"backend: 发布一个消息: {event.id} {event.type}")
            else:
                logger.debug(f"backend: 丢弃一个消息: {event.id} {event.type}")

    def handle_subscribe_event(self, subscriber) -> None:
        """处理外部获取的消息"""

        logger.info(f"开始抓取subscriber ({self._subscribers})中的消息")

        while self._active:
            try:
                events = subscriber()

                for event in events:
                    logger.info(f"{subscriber}: 收到events : ({event})")
                    self.submit_event(event)

            except Exception as e:
                logger.error(f"{subscriber} runtime error: {e}", exc_info=True)

        return


class vxAsyncZMQBrokerServerv0:
    """消息分发器"""

    def __init__(
        self,
        frontend_url: str = "tcp://127.0.0.1:12306",
        frontend_sercet_key: str = "",
        backend_url: str = __INTERNAL_ZMQFORMAT__,
        backend_sercet_key: str = "",
    ) -> None:
        self._active = False
        self._queue = PriorityQueue()

        self._ctx = vxAsyncZMQContext().instance()

        self._frontend_url = frontend_url
        self._frontend_sercet_key = frontend_sercet_key
        self._frontend = None
        self._backend_url = backend_url
        self._backend_sercet_key = backend_sercet_key
        self._backend = None
        self._transfer_to = defaultdict(list)
        self._subscribers = []

    def transfer_to(self, channel_name: str, publisher: Callable):
        """将消息通道channel_name消息转发至 publisher上

        Arguments:
            channel_name {str} -- 待转发的消息通道
            publisher {Callable} -- 发布器
        """
        if publisher in self._transfer_to[channel_name]:
            logger.warning(f"更新转发通道{channel_name}的发布器，请注意...")

        self._transfer_to[channel_name].append(publisher)

    def fetch_from(self, subscriber: Callable):
        """从外部获取消息

        Arguments:
            subscriber {Callable} -- 订阅器
        """
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def submit_event(self, event: vxEvent) -> None:
        """提交event

        Arguments:
            event {vxEvent} -- 待提交的消息
        """

        if event.trigger and event.trigger.status == TriggerStatus.Pending:
            event.next_trigger_dt = next(event.trigger)
            logger.debug(
                f"更新event.next_trigger_dt: {to_timestring(event.next_trigger_dt)}"
            )

        self._queue.put_nowait(event)

    def server_forever(self) -> None:
        """开始执行服务"""
        if self._active:
            logger.warning("server 已经启动了，请勿重复启动 ...")
            return

        self._active = True

        try:
            logger.info(f"{self.__class__.__name__} 开始启动 ...")

            jobs = [self.handle_recv_event(), self.handle_send_event()]
            jobs.extend(
                [
                    self.handle_subscribe_event(subscriber)
                    for subscriber in self._subscribers
                ]
            )

            asyncio.run(asyncio.wait(jobs))

        finally:
            self.stop()

        logger.info("{self.__class__.__name__} 运行结束...")

    def stop(self):
        """暂停运行"""
        self._active = False
        if self._frontend:
            self._frontend.close()

        if self._backend:
            self._backend.close()

    async def handle_recv_event(self) -> None:
        """处理前端相关内容"""

        self._frontend = self._ctx.socket(zmq.XSUB)
        self._frontend.bind(self._frontend_url, self._frontend_sercet_key)
        # self._frontend.setsockopt_string(zmq.SUBSCRIBE, "")
        await self._frontend.send(b"\x01")
        logger.info(
            f"开始监听frontend: {self._frontend_url} with key_file:"
            f" ({self._frontend_sercet_key})"
        )

        while self._active:
            (
                channel,
                controll_tag,
                packed_event,
            ) = await self._frontend.recv_multipart()

            if controll_tag != b"PUBSUB":
                logger.warning(f"未支持的方法  {controll_tag},channel={channel}")
                continue

            recv_event = vxEvent.unpack(packed_event)
            logger.debug(f"收到event: {recv_event}")

            recv_event.channel = to_text(channel)
            self.submit_event(recv_event)

        logger.info(
            f"停止监听frontend: {self._frontend_url} with key_file:"
            f" {self._frontend_sercet_key}"
        )

    async def handle_send_event(self) -> None:
        """发送event消息"""
        self._backend = self._ctx.socket(zmq.XPUB)
        self._backend.bind(self._backend_url, self._backend_sercet_key)
        logger.info(
            f"开始监听backend: {self._backend_url} with key_file:"
            f" ({self._backend_sercet_key})"
        )

        while self._active:
            if (
                self._queue.empty()
                or self._queue.queue[0].next_trigger_dt > vxtime.now()
            ):
                await asyncio.sleep(0)  # let other task run
                continue

            event = self._queue.get_nowait()
            last_trigger_dt = event.next_trigger_dt
            if isinstance(event.trigger, vxTrigger):
                for next_trigger_dt in event.trigger:
                    event.next_trigger_dt = next_trigger_dt
                    self._queue.put_nowait(event)
                    logger.debug(
                        "更新event.next_trigger_dt:"
                        f" {to_timestring(event.next_trigger_dt)}, 并且重新入库..."
                    )
                    break

            send_event = vxEvent(
                type=event.type,
                data=event.data,
                trigger=None,
                next_trigger_dt=last_trigger_dt,
                channel=event.channel,
            )

            asyncio.create_task(self._send_event(send_event))

            publishers = self._transfer_to.get(send_event.channel, [])
            for publisher in publishers:
                publisher(send_event)
                logger.info(f"转发消息通道{send_event.channel}消息至 {publisher}")

    async def _send_event(self, event: vxEvent) -> None:
        channel = to_binary(event.channel)
        packed_event = vxEvent.pack(event)
        if await self._backend.poll(50, zmq.POLLIN) != 0:
            logger.debug(f"backend: 发布一个消息: {event}")
            await self._backend.send_multipart([channel, b"PUBSUB", packed_event])
        else:
            logger.debug(f"backend: 丢弃一个消息: {event}")

    async def handle_subscribe_event(self, subscriber) -> None:
        """处理外部获取的消息"""

        logger.info(f"开始抓取subscriber ({self._subscribers})中的消息")

        while self._active:
            try:
                events = subscriber()
                list(map(self.submit_event, events))
            except Exception as e:
                logger.error(f"{subscriber} runtime error: {e}", exc_info=True)

            await asyncio.sleep(0)

        return


_default_broker_config = {
    "transfer_outs": defaultdict(list),
    "subscribers": [],
    "publish_queue": vxEventQueue(),
    "reply_queue": Queue(),
    "rpc_methods": {},
}


def error_log(err: Exception, *args, **kwargs):
    """error_callback 处理"""
    logger.error(f"{err} {args} {kwargs}", exc_info=True)


def backend_on_subscribe(context, event) -> None:
    """订阅事件触发"""
    logger.error(f"收到订阅信息: {event.data} =====")
    if event.data.startswith("rpc_"):
        context.reply_queue.put_nowait(
            vxEvent(type="__RPC_METHODS__", channel=event.data, reply_to="__BROKER__")
        )


def backend_on_unsubscribe(context, event) -> None:
    logger.warning(f"取消订阅信息: {event.data}")
    if event.data.startswith("rpc_"):
        context.rpc_methods = {
            method: channel
            for method, channel in context.rpc_methods.items()
            if channel != event.data
        }


def handle_subscribers(context, event) -> None:
    """处理外部获取的消息"""

    # logger.debug(f"开始抓取subscriber ({context.subscribers})中的消息")
    events = [subscriber() for subscriber in context.subscribers]
    for event in itertools.chain(*events):
        context.publish_queue.put_nowait(event)
        logger.info(f"internal: 收到外部event : ({event.type})")

    return


def backend_ready_event(context, event):
    """处理ready 报文"""
    reply_event = vxEvent(
        type="__ACK__",
        data="READY",
        channel=event.channel,
    )
    context.reply_queue.put_nowait(reply_event)
    # logger.debug(f"Client({event.channel}) is ready...{reply_event.type}")


def frontend_handle_get_rpc_method(context, event):
    """前端或许rpc methods"""
    reply_event = vxEvent(
        type="__GET_RPCMETHODS__",
        data=context.rpc_methods,
        channel=event.reply_to,
    )
    context.reply_queue.put_nowait(reply_event)


def backend_on_update_methods(context, event):
    """更新rpc methods"""
    logger.warning(f"更新rpc method: {event.data}")
    context.rpc_methods.update(event.data)


class vxZMQBrokerServer:
    def __init__(
        self,
        frontend_url: str = "tcp://127.0.0.1:12306",
        frontend_sercet_key: str = "",
        backend_url: str = __INTERNAL_ZMQFORMAT__,
        backend_sercet_key: str = "",
    ) -> None:
        # * init handler
        self._context = vxContext(_default_broker_config)
        self._handler = vxEventHandlers(self._context)
        self.init_handler()

        self._pool = None
        self._active = False

        self._zmqctx = vxZMQContext().instance()
        self._frontend = self._zmqctx.socket(zmq.ROUTER)
        self._frontend.bind(frontend_url, frontend_sercet_key)
        self._backend = self._zmqctx.socket(zmq.XPUB)
        self._backend.bind(backend_url, backend_sercet_key)
        self._recv_events = {}

    @property
    def handler(self):
        """处理器"""
        return self._handler

    def init_handler(self) -> None:
        """初始化handler"""
        self._handler.register("__EVERYTICK__", handle_subscribers)
        self._handler.register("__GET_RPCMETHODS__", frontend_handle_get_rpc_method)
        self._handler.register("__READY__", backend_ready_event)
        self._handler.register("__RPC_METHODS__", backend_on_update_methods)
        self._handler.register("__ON_SUBSCRIBE__", backend_on_subscribe)
        self._handler.register("__ON_UNSUBSCRIBE__", backend_on_unsubscribe)

        self.submit_event(
            vxEvent(
                type="__EVERYTICK__",
                trigger=vxIntervalTrigger(0.5),
                channel="__BROKER__",
            ),
        )

    def transfer_out(self, channel_name: str, publisher: Callable):
        """将消息通道channel_name消息转发至 publisher上

        Arguments:
            channel_name {str} -- 待转发的消息通道
            publisher {Callable} -- 发布器
        """
        if channel_name not in self._context.transfer_outs:
            self._context.transfer_outs[channel_name] = []

        if publisher not in self._context.transfer_outs[channel_name]:
            self._context.transfer_outs[channel_name].append(publisher)

    def subscribe(self, subscriber: Callable):
        """从外部获取消息

        Arguments:
            subscriber {Callable} -- 订阅器
        """
        if subscriber not in self._context.subscribers:
            self._context.subscribers.append(subscriber)
            logger.info(f"添加 {subscriber} ...")

    def submit_event(self, event: vxEvent) -> None:
        """提交event

        Arguments:
            event {vxEvent} -- 待提交的消息
        """
        try:
            if event.id in self._recv_events:
                reply_event = self._recv_events[event.id]
                reply_event.channel = event.reply_to
                logger.warning(
                    f"重复消息，回复之前回复消息: reply_to: {reply_event.channel} with type:"
                    f" {reply_event.type} "
                )
            else:
                self._context.publish_queue.put_nowait(event)
        except Exception as e:
            logger.error(f"submit event({event.id}) error:{e}")

    def fetch_events(self):
        events = []
        with contextlib.suppress(Empty):
            while not self._context.publish_queue.empty():
                event = self._context.publish_queue.get_nowait()
                events.append(event)

        return events

    def server_forever(self) -> None:
        """开始执行服务"""
        if self._active:
            logger.warning("server 已经启动了，请勿重复启动 ...")
            return

        self._active = True
        self._pool = Pool()

        logger.info(f"{self.__class__.__name__} 开始启动 ...")
        try:
            self._pool.apply_async(
                self._run_frontend,
                error_callback=lambda e: logger.error(e, exc_info=True),
            )
            self._run_backend()

        finally:
            self.stop()

        logger.info("{self.__class__.__name__} 运行结束...")

    def stop(self):
        """暂停运行"""

        self._active = False
        if self._frontend:
            self._frontend.close()

        if self._backend:
            self._backend.close()

        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None

    def _run_frontend(self) -> None:
        while self._active:
            try:
                flags = self._frontend.poll(1000, zmq.POLLIN | zmq.POLLOUT)
                if flags & zmq.POLLIN != 0:
                    msg = self._frontend.recv_multipart()
                    # * client_addr , b"", msg_body
                    self._pool.apply_async(
                        self._handle_frontend_recv_msg,
                        args=(msg,),
                        error_callback=error_log,
                    )

                if flags & zmq.POLLOUT != 0:
                    with contextlib.suppress(Empty):
                        reply_event = self._context.reply_queue.get_nowait()

                        self._recv_events[reply_event.reply_to] = reply_event

                        client_addr = to_binary(reply_event.channel)
                        reply_event.channel = ""
                        reply_event.reply_to = ""

                        self._frontend.send_multipart(
                            [
                                client_addr,
                                b"",
                                vxEvent.pack(reply_event),
                            ]
                        )
                        logger.info(
                            f"frontend reply to ({client_addr})"
                            f" === type: {reply_event.type} data: {reply_event.data}"
                        )
            except Exception as e:
                logger.error(f"frontend 发生错误: {e}", exc_info=True)

    def _handle_frontend_recv_msg(self, msg):
        client_addr, empty, packed_event = msg
        assert empty == b""
        recv_event = vxEvent.unpack(packed_event)

        if recv_event.channel == "__BROKER__":
            # __BROKER__事件，修改调用的channel，等待后续回复
            recv_event.reply_to = client_addr
            self._handler.trigger(recv_event)
            logger.info(
                f"Client({client_addr}) 触发broker 内部事件:{recv_event.type} =="
                f" {recv_event.data}"
            )

        elif (
            recv_event.channel == "__RPC__"
            and recv_event.type not in self._context.rpc_methods
        ):
            reply_event = vxEvent(
                type="__RPC_REPLY__",
                data=ValueError(f"不支持的 {recv_event.type} 方法."),
                channel=client_addr,
            )
            self._context.reply_queue.put_nowait(reply_event)
            logger.warning(f"不支持的 {recv_event.type} 方法.")

        elif recv_event.channel == "__RPC__":
            recv_event.channel = self._context.rpc_methods[recv_event.type]
            recv_event.reply_to = client_addr
            recv_event.trigger = ""
            self.submit_event(recv_event)
            logger.info(
                f"Client({recv_event.channel}) (RPC)"
                f" 远程调用:{recv_event.type}({recv_event.data})"
            )

        elif not recv_event.channel.startswith("_"):
            reply_event = vxEvent(type="__ACK__", data="OK", channel=client_addr)
            self._context.reply_queue.put(reply_event)
            recv_event.reply_to = ""
            self.submit_event(recv_event)
            logger.info(
                f"Client向通道({recv_event.channel}) 发布(PUBLISH)"
                f" 事件:type({recv_event.type}),data({recv_event.data})"
            )
        else:
            reply_event = vxEvent(
                type="__ACK__",
                data=ValueError("not suport event."),
                channel=client_addr,
            )
            self._context.reply_queue.put(reply_event)
            logger.warning(f"Client({client_addr}) 非法消息 ...{reply_event}")

    def _run_backend(self) -> None:
        while self._active:
            try:
                flags = self._backend.poll(1000, zmq.POLLIN | zmq.POLLOUT)

                if flags & zmq.POLLIN != 0:
                    msg = self._backend.recv_multipart()
                    # logger.debug(msg)
                    self._pool.apply_async(
                        self._handle_backend_recv_msg,
                        args=(msg,),
                        error_callback=error_log,
                    )

                if flags & zmq.POLLOUT != 0:
                    events = self.fetch_events()
                    for event in events:
                        if event.channel == "__BROKER__":
                            # logger.warning(f"__BROKER__ 触发 {event.type} 事件...")
                            self._pool.apply_async(
                                self.handler.trigger,
                                args=(event,),
                                error_callback=error_log,
                            )
                        else:
                            channel = to_binary(event.channel)
                            msg_body = vxEvent.pack(event)
                            self._backend.send_multipart([channel, msg_body])

                            logger.debug(
                                "backend 通过"
                                f" {channel} 发送events:{event.type}({event.data})"
                            )

                            if event.channel in self._context.transfer_outs:
                                for publisher in self._context.transfer_outs[
                                    event.channel
                                ]:
                                    self._pool.apply_async(
                                        publisher,
                                        args=(event,),
                                        error_callback=error_log,
                                    )
                                    logger.info(
                                        f"backend: 转发 {event.id}==={event.type} to"
                                        f" {publisher}"
                                    )

            except Exception as e:
                logger.error(f"发生错误: {e}", exc_info=True)

    def _handle_backend_recv_msg(self, msg):
        try:
            if msg[0].startswith(b"\x01"):
                event = vxEvent(
                    type="__ON_SUBSCRIBE__",
                    data=msg[0][1:].decode("ascii"),
                    channel="__BROKER__",
                )

                self._handler.trigger(event)
                return

            elif msg[0].startswith(b"\x00"):
                event = vxEvent(
                    type="__ON_UNSUBSCRIBE__",
                    data=msg[0][1:].decode("ascii"),
                    channel="__BROKER__",
                )
                self._handler.trigger(event)
                return
            else:
                event = vxEvent.unpack(msg[0])
                if event.channel == "__BROKER__":
                    self.handler.trigger(event)
                elif not event.type.startswith("_"):
                    self._context.reply_queue.put_nowait(event)
                else:
                    logger.warning(f"收到错误消息: {event}")
        except Exception as e:
            logger.error(f"error: {e}", exc_info=True)
