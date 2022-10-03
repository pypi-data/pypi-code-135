"""rpc"""


import time
import pickle
import inspect
import zmq
import importlib
import contextlib
import pathlib

import secrets
from multiprocessing.dummy import Pool
from queue import Empty, PriorityQueue, Queue
from functools import wraps
from collections import defaultdict
from typing import Callable, Optional, Any, Union

from vxutils import logger, vxtime, vxZMQContext, to_timestring, to_binary
from vxsched import (
    vxContext,
    vxEvent,
    vxEventHandlers,
    vxEventQueue,
    vxTrigger,
    TriggerStatus,
)


class vxRpcMethods:
    """消息处理函数"""

    def __init__(self, context: Optional[vxContext] = None) -> None:
        self._context = context or vxContext()
        self._methods = {}

    @property
    def context(self):
        """获取上下文"""
        return self._context

    @property
    def methods(self):
        """所有支持得方法"""
        return list(self._methods.keys())

    def register(self, method_name: str, handler: Callable) -> None:
        """注册事件处理函数

        Arguments:
            method_name {str} -- 消息类型
            handler {Callable} -- 消息处理函数,handler(context, event, tools=None)

        Raises:
            ValueError: handler类型错误
        """

        if not callable(handler):
            raise ValueError(f"{handler} is not callable.")

        self.__call__(method_name)(handler)

    def unregister(self, method_name: str) -> None:
        """取消注册RPC处理函数

        Arguments:
            method_name {str} -- 消息类型
            handler {Optional[Callable]} -- 消息事件处理函数 (default: {None})
        """

        logger.info(f"{self.__class__.__name__} unregister rpc_method: {method_name}")
        self._methods.pop(method_name)

    def execute(self, event: vxEvent) -> Any:
        """触发一个消息

        Arguments:
            event {vxEvent} -- 待触发的消息类型

        Returns:
            Any -- 所有handler
        """
        handler = self._methods.get(event.type, None)
        if handler:
            return handler(self._context, event)

        raise NotImplementedError(f"调用方法 {event.type} 暂不支持...")

    def __call__(self, method_name, with_context=True, time_limit=1, func=None):
        def deco(func):
            @wraps(func)
            def _rpc_handler(context, event):
                try:
                    args, kwargs = event.data
                    if with_context:
                        args = (context, *args)
                        ba = inspect.signature(func).bind(args, kwargs)
                    else:
                        ba = inspect.signature(func).bind(args, kwargs)

                    start = time.perf_counter()
                    ret = func(*ba.args, **ba.kwargs)
                    cost_time = time.perf_counter() - start
                    if cost_time > time_limit:
                        logger.warning(
                            f"{self.__class__.__name__}:{func.__name__} 耗时"
                            f" {cost_time*1000:,.2f}ms 超出预定时间 {time_limit*1000:,.2f}ms."
                            f" kwargs={event.data}"
                        )

                except Exception as err:
                    logger.error(
                        f"{self.__class__.__name__}:{func.__name__} error:"
                        f" {err},event={event}",
                        exc_info=True,
                    )
                    ret = err

                return ret

            self._methods[method_name] = _rpc_handler
            logger.info(
                f"{self.__class__.__name__} register rpc_method: {method_name} =="
                f" {_rpc_handler.__name__}()"
            )
            return func

        if func:
            deco(func)

        return deco

    def load_modules(self, mod_path):
        """加载策略目录"""
        if not pathlib.Path(mod_path).exists():
            logger.warning(msg=f"{mod_path} is not exists")
            return

        modules = pathlib.Path(mod_path).iterdir()
        logger.info(f"loading strategy dir: {mod_path}.")
        logger.info("=" * 80)
        for mod in modules:
            if (not mod.name.startswith("__")) and mod.name.endswith(".py"):
                try:
                    loader = importlib.machinery.SourceFileLoader(
                        mod.name, mod.as_posix()
                    )
                    spec = importlib.util.spec_from_loader(loader.name, loader)
                    strategy_mod = importlib.util.module_from_spec(spec)
                    loader.exec_module(strategy_mod)
                    logger.info(f"Load Module: {strategy_mod} Sucess.")
                    logger.info("+" * 80)

                except Exception as err:
                    logger.error(
                        f"Load Module: {mod.as_posix()} Failed. {err}", exc_info=True
                    )
                    logger.error("-" * 80)


class vxEngine:
    def __init__(
        self,
        name: str = "",
        url: str = None,
        public_key: str = None,
        context: vxContext = None,
        event_handlers: vxEventHandlers = None,
        rpc_methods: vxRpcMethods = None,
    ) -> None:
        """_summary_

        Keyword Arguments:
            name {str} -- engine 名称，若不指定，则由系统自行生成uuid (default: {None})
            channel {vxChannel} -- 消息通道 (default: {None})
            context {vxContext} -- 上下文 (default: {None})
            event_handlers {vxEventHandlers} -- 事件处理函数 (default: {None})
            rpc_methods {vxRpcMethods} -- 远程调用处理函数 (default: {None})
        """
        self._name = name
        self._active = False
        self._rpc_token = f"rpc_{secrets.token_hex(16)}"
        self._zmqctx = None
        self._socket = None
        self._socket_params = (url, public_key)

        self._context = context or vxContext()
        self._event_queue = vxEventQueue()
        self._reply_queue = Queue()

        self._event_handlers = event_handlers or vxEventHandlers(self._context)
        self._rpc_methods = rpc_methods or vxRpcMethods(self._context)
        self._pool = None

        self._subscribers = []

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}({self.name}) with socket:"
            f" {self._socket_params[0]}"
        )

    @property
    def name(self) -> str:
        """engine 名称"""
        return self._name

    @property
    def queue(self) -> Queue:
        """消息队列"""
        return self._event_queue

    @property
    def context(self) -> vxContext:
        """上下文"""
        return self._context

    @property
    def event_handler(self) -> vxEventHandlers:
        """事件处理函数

        engine = vxEngine()
        @engine.event_handler("on_say")
        def on_say(context, event):
            print(event)

        """
        return self._event_handlers

    @property
    def rpc_method(self) -> vxRpcMethods:
        """远程调用处理函数

        @vxEngine.rpc_method("say_helloworld")
        def say_helloworld(*args, **kwargs):
            print(args)
            print(kwargs)

        """
        return self._rpc_methods

    def activate(self) -> None:
        if self._active is True:
            return
        self._active = True
        self.submit_event("__init__")

        if self._socket_params[0]:
            self._init_socket(*self._socket_params)

    def _init_socket(self, url: str, public_key: str):
        """激活zmq socket

        Arguments:
            url {str} -- 绑定远程服务器地址
            public_key {str} -- 公钥文件地址
        """

        self._zmqctx = vxZMQContext().instance()
        self._socket = self._zmqctx.socket(zmq.XSUB)
        self._socket.connect(url, public_key)

        self._socket.send(b"\x01" + to_binary(self.name))
        logger.debug(f"subscribe '{self.name}'")

        self._socket.send(b"\x01" + b"*")
        logger.debug("subscribe '*'")

        self._socket.send(b"\x01" + to_binary(self._rpc_token))
        logger.debug(f"subscribe rpc_token: '{self._rpc_token}'")

        if self._rpc_methods.methods:
            reply_event = vxEvent(
                type="__RPC_METHODS__",
                data={method: self._rpc_token for method in self._rpc_methods.methods},
                channel="__BROKER__",
            )
            self._reply_queue.put(reply_event)
            logger.info(f"注册rpc method: {self._rpc_methods.methods}")

    def submit_event(
        self,
        event: Union[str, vxEvent],
        data: Any = "",
        trigger: Optional[vxTrigger] = None,
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
        self._event_queue.put_nowait(send_event)
        if not self._active:
            logger.warning(
                f"{self.__class__.__name__}({self._name}, id-{id(self)})"
                f" 未激活，event({send_event.type})将在激活后运行。"
            )

    def _handle_msg(self, msg):
        event = vxEvent.unpack(msg[1])
        logger.debug(
            f"收到channel:{event.channel} 的 {event.type} 消息: {event.data} reply to :"
            f" {event.reply_to}"
        )

        if event.channel == self._rpc_token and event.type == "__GET_RPCMETHODS__":
            reply_event = vxEvent(
                type="__RPC_METHODS__",
                data={method: self._rpc_token for method in self._rpc_methods},
                channel=event.reply_to,
            )
            self._reply_queue.put(reply_event)
            logger.debug(f"{self.__class__.__name__}({self._name}) 回复消息: {reply_event}")

        elif event.channel == self._rpc_token and event.reply_to:
            try:
                reply_msg = self.rpc_method.execute(event)
            except Exception as err:
                logger.error(f"RPC调用 {event.type}({event.data}) 发生错误: {err}")
                reply_msg = err

            reply_event = vxEvent(
                type=event.type, data=reply_msg, channel=event.reply_to
            )
            self._reply_queue.put_nowait(reply_event)
            logger.debug(
                f"{self.__class__.__name__}({self._name}) 回复消息: {reply_event.data}"
            )
        elif not event.reply_to:
            self.submit_event(event)
            logger.debug(
                f"{self.__class__.__name__}({self._name}) 触发消息事件: {event.type} =="
                f" {event.data}"
            )
        else:
            logger.warning(
                f"{self.__class__.__name__}({self._name}) 收到非法消息: {event.type} =="
                f" {event.data}"
            )

    def _run_backend(self) -> None:
        logger.info(
            f"{self.__class__.__name__}({self._name} id-({id(self)})) backend 启动运行..."
        )
        while self._active:
            flags = self._socket.poll(1000, zmq.POLLIN | zmq.POLLOUT)

            if flags & zmq.POLLIN != 0:
                msg = self._socket.recv_multipart()
                logger.info(msg)
                self._pool.apply_async(
                    self._handle_msg,
                    args=(msg,),
                    error_callback=lambda e: logger.error(e, exc_info=True),
                )

            if flags & zmq.POLLOUT != 0:
                with contextlib.suppress(Empty):
                    event = self._reply_queue.get_nowait()
                    self._socket.send_multipart([vxEvent.pack(event)])

    def start(self) -> None:
        """开始运行"""

        if self._active:
            logger.info(f"{self.__class__.__name__}({self.name}) 已经启动，请勿重复启动...")

        self.activate()

        logger.info(f"{self.__class__.__name__}({self.name}) 开始启动...")
        try:
            self._pool = Pool()

            if self._socket:
                self._pool.apply_async(
                    self._run_backend, error_callback=lambda e: logger.error(e)
                )
            while self._active:
                with contextlib.suppress(Empty):
                    event = self.queue.get(0.1)
                    logger.info(f"{self.__class__.__name__} 触发 {event.type} 事件...")
                    self._pool.apply_async(self.event_handler.trigger, args=(event,))

        finally:
            self.stop()
            logger.info(f"{self.__class__.__name__}({self.name}) 已经停止...")

    def stop(self) -> None:
        """暂停运行"""
        self._active = False
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None


if __name__ == "__main__":
    logger.setLevel("DEBUG")
    rpcworker = vxEngine("test", "tcp://127.0.0.1:6666")

    @rpcworker.event_handler("sayhelloworld")
    def helloworld(context, event):
        logger.info("=" * 60)
        logger.info(event)
        logger.info("=" * 60)

    @rpcworker.rpc_method("say")
    def sayhelloworld1(hello, world, the=1):
        # logger.info("=" * 60)
        # logger.info(args)
        # logger.info(kwargs)
        # logger.info("=" * 60)
        return f"hello world: {hello} {world}, {the}"

    rpcworker.start()
