""" 策略handler模块 """


from abc import abstractmethod

from multiprocessing.dummy import Pool
import os
import zmq
import time
import uuid
import secrets
import inspect
import pathlib
import importlib
import contextlib
from functools import wraps
from queue import Empty, Queue
from typing import Any, Callable, Optional, Union, List
from vxutils import (
    logger,
    vxtime,
    vxZMQContext,
    to_binary,
)

from vxsched.event import vxEvent, vxTrigger, vxEventQueue
from vxsched.context import vxContext

__all__ = [
    "vxEventHandlers",
    "vxRpcMethods",
    "vxEventSched",
    "vxEngine",
    "vxhandlers",
    "vxmethods",
    "vxscheduler",
    "vxengine",
    "vxPublisher",
    "vxSubscriber",
    "load_modules",
]


class vxEventHandlers:
    """消息处理函数"""

    def __init__(self, context: Optional[vxContext] = None) -> None:
        self._context = context or vxContext()
        self._handlers = {}

    @property
    def context(self):
        """获取上下文"""
        return self._context

    def register(self, event_type: str, handler: Callable) -> None:
        """注册事件处理函数

        Arguments:
            event_type {str} -- 消息类型
            handler {Callable} -- 消息处理函数,handler(context, event, tools=None)

        Raises:
            ValueError: handler类型错误
        """

        if not callable(handler):
            raise ValueError(f"{handler.__name__} is not callable.")

        handlers = self._handlers.pop(event_type, [])
        handler_names = [handler.__name__ for handler in handlers]

        if (handler.__name__ not in handler_names) and (handler not in handlers):
            handlers.append(handler)
            logger.info(
                f"{self.__class__.__name__} register event type: {event_type}, handler:"
                f" {handler}"
            )
        self._handlers[event_type] = handlers

    def unregister(self, event_type: str, handler: Optional[Callable] = None) -> None:
        """取消注册事件处理函数

        Arguments:
            event_type {str} -- 消息类型

        Keyword Arguments:
            handler {Optional[Callable]} -- 消息事件处理函数 (default: {None})
        """

        logger.info(
            f"vxScheduler unregister event type: {event_type}, handler: {handler}"
        )
        handlers = self._handlers.pop(event_type, [])
        if handler:
            if handler in handlers:
                handlers.remove(handler)

            if handlers:
                self._handlers[event_type] = handlers

    def unregister_handler(self, handler: Callable) -> None:
        """取消监听特定函数

        Arguments:
            handler {Callable} -- 待取消监听的函数
        """

        handlers = self._handlers

        for event_type, handlers in handlers.items():
            if handler in handlers:
                handlers.remove(handler)
                if handlers:
                    self._handlers[event_type] = handlers
                else:
                    self._handlers.pop(event_type)

                logger.info(
                    f"{self.__class__.__name__} unregister event type: {event_type},"
                    f" handler: {handler}"
                )

    def trigger(self, event: vxEvent) -> Any:
        """触发一个消息

        Arguments:
            event {vxEvent} -- 待触发的消息类型

        Returns:
            Any -- 所有handler
        """
        handlers = self._handlers.get(str(event.type), [])
        return [handler(self.context, event) for handler in handlers]

    def __call__(self, event_type, time_limit=1):
        def deco(func):
            @wraps(func)
            def _event_handler(context, event):
                try:
                    start = time.perf_counter()
                    ret = func(context, event)
                    cost_time = time.perf_counter() - start
                    if cost_time > time_limit:
                        logger.warning(
                            f"{self.__class__.__name__}:{func.__name__} 耗时"
                            f" {cost_time*1000:,.2f}ms 超出预定时间 {time_limit*1000:,.2f}ms."
                            f" event={event}"
                        )

                except Exception as err:
                    logger.error(
                        f"{self.__class__.__name__}:{func.__name__} error:"
                        f" {err},event={event}",
                        exc_info=True,
                    )
                    ret = None

                return ret

            self.register(event_type, _event_handler)
            return func

        return deco


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
                        ba = inspect.signature(func).bind(*args, **kwargs)
                    else:
                        ba = inspect.signature(func).bind(*args, **kwargs)
                    ba.apply_defaults()

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


vxhandlers = vxEventHandlers()
vxmethods = vxRpcMethods()


class vxEventSched:
    """调度器"""

    def __init__(
        self, channel_name: str = None, handlers: vxEventHandlers = None
    ) -> None:
        self._channel_name = channel_name or str(uuid.uuid4())
        self._handler = handlers or vxEventHandlers()
        self._subscribers = []
        self._active = False
        self._queue = vxEventQueue()
        self._pool = None

    @property
    def handler(self) -> vxEventHandlers:
        """vxEventHandler"""
        return self._handler

    @property
    def context(self) -> vxContext:
        """上下文"""
        return self._handler.context

    @property
    def subscribers(self):
        """订阅器"""
        return self._subscribers

    def activate(self):
        """激活"""
        if self._active is False:
            self._active = True
            self.submit_event("__init__")

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
        self._queue.put_nowait(send_event)
        if not self._active:
            logger.warning(
                f"{self.__class__.__name__}(id-{id(self)})"
                f" 未激活，event({send_event.type})将在激活后运行。"
            )

    def subscribe(self, subscriber: Callable) -> None:
        """订阅消息

        Arguments:
            subscriber {Callable} -- 订阅方法
        """
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            if self._active:
                self._pool.apply_async(self._run_subscribe_events, subscriber)

    def fetch_events(self):
        """抓取当前所有可触发的event"""

        events = []
        with contextlib.suppress(Empty):
            while not self._queue.empty():
                event = self._queue.get_nowait()
                events.append(event)
        return events

    def fetch_subscribe_events(self, subscriber: Callable) -> None:
        """获取订阅event"""

        try:
            events = subscriber()
            list(map(self.submit_event, events))
        except Exception as e:
            logger.error(f"{subscriber} runtime error: {e}, exc_info=True")

    def _run_subscribe_events(self, subscriber):
        logger.info(f"开始监听 {subscriber}")
        while self._active:
            self.fetch_subscribe_events(subscriber)
            vxtime.sleep(0.1)

        logger.info(f"停止监听 {subscriber}")

        return

    def _run_handler_events(self) -> None:
        """消息引擎运行函数"""

        logger.info(f"{self.__class__.__name__}(id-{id(self)}) 开始多线程模式运行...")
        while self._active:
            events = self.fetch_events()
            if events:
                self._pool.map_async(self.handler.trigger, events)
            else:
                vxtime.sleep(0.1)

    def _run(self) -> None:
        logger.info(f"{self.__class__.__name__}(id-{id(self)}) 开始单线程模式运行...")

        while self._active:
            if self._subscribers:
                # * for subscriber in self._subscribers:
                # *     try:
                # *         events = subscriber()
                # *         list(map(self.submit_event, events))
                # *     except Exception as e:
                # *         logger.error(f"error: {e}", exc_info=True)
                list(map(self.fetch_subscribe_events, self._subscribers))
            else:
                vxtime.sleep(0.1)

            list(map(self.handler.trigger, self.fetch_events()))

        logger.info(f"{self.__class__.__name__}(id-{id(self)}) 停止单线程模式运行...")
        return

    def start(self, multi_mode: bool = True, daemon=True) -> None:
        """开始运行vxScheduler

        Keyword Arguments:
            multi_mode {bool} -- 是否采用短线程模式 (default: {True})
        """

        if self._active:
            logger.warning("{self.__class__.__name__}(id-{id(self)}) 已经启动，请勿重复启动...")
            return

        self.activate()

        if multi_mode:
            self._pool = Pool(16)
            worker_thread = self._pool.apply_async(self._run_handler_events)
            self._pool.map_async(self._run_subscribe_events, self._subscribers)
            if daemon:
                worker_thread.get()
        else:
            try:
                self._run()
            finally:
                self.stop()

    def stop(self) -> None:
        """暂停函数"""
        self._active = False
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None

    def load_modules(self, mod_path):
        """加载策略目录"""
        if not os.path.exists(mod_path):
            logger.warning(msg=f"{mod_path} is not exists")
            return

        modules = os.listdir(mod_path)
        logger.info(f"loading strategy dir: {mod_path}.")
        logger.info("=" * 80)
        for mod in modules:
            if (not mod.startswith("__")) and mod.endswith(".py"):
                try:
                    loader = importlib.machinery.SourceFileLoader(
                        mod, os.path.join(mod_path, mod)
                    )
                    spec = importlib.util.spec_from_loader(loader.name, loader)
                    strategy_mod = importlib.util.module_from_spec(spec)
                    loader.exec_module(strategy_mod)
                    logger.info(f"Load Module: {strategy_mod} Sucess.")
                    logger.info("+" * 80)
                except Exception as err:
                    logger.error(f"Load Module: {mod} Failed. {err}", exc_info=True)
                    logger.error("-" * 80)


class vxPublisher:
    """发布器"""

    def __init__(self, channel_name: str) -> None:
        self._channel_name = channel_name

    @property
    def channel_name(self) -> str:
        """消息通道名称"""
        return self._channel_name

    def __str__(self) -> str:
        return f"< {self.__class__.__name__}({self.channel_name})"

    __repr__ = __str__

    @abstractmethod
    def __call__(
        self,
        event: Union[str, vxEvent],
        data="",
        trigger: Optional[vxTrigger] = None,
        priority: float = 10,
        channel: str = None,
        **kwargs,
    ) -> None:
        """发布消息

        Arguments:
            event {Union[str, vxEvent]} -- 要推送消息或消息类型
            data {Any} -- 消息数据信息 (default: {None})
            trigger {Optional[vxTrigger]} -- 消息触发器 (default: {None})
            priority {int} -- 优先级，越小优先级越高 (default: {10})
        """


class vxSubscriber:
    """订阅器"""

    def __init__(self, channel_name: str) -> None:
        self._channel_name = channel_name

    @property
    def channel_name(self) -> str:
        """消息通道名称"""
        return self._channel_name

    def __str__(self) -> str:
        return f"< {self.__class__.__name__}({self.channel_name})"

    @abstractmethod
    def __call__(self) -> List[vxEvent]:
        pass


vxscheduler = vxEventSched(vxhandlers)


class vxEngine:
    def __init__(
        self,
        channel_name: str = "",
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
        self._name = channel_name
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

    def reset(
        self,
        channel_name: str = "",
        url: str = None,
        public_key: str = None,
        context: vxContext = None,
    ):
        """重置运行参数

        Keyword Arguments:
            channel_name {str} -- 消息通道名称 (default: {""})
            url {str} -- broker backend 地址 (default: {None})
            public_key {str} -- broker backend 公钥 (default: {None})
            context {vxContext} -- context上下文 (default: {None})
        """
        if channel_name:
            self._name = channel_name

        if url:
            self._socket_params = (url, public_key)

        if context:
            self._context = context
            self._event_handlers._context = self._context
            self._rpc_methods._context = self._context

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
            self._reply_queue.put_nowait(reply_event)
            logger.info(f"注册rpc method: {self._rpc_methods.methods}")

    def submit_event(
        self,
        event: Union[str, vxEvent],
        data: Any = "",
        trigger: Optional[vxTrigger] = None,
        priority: float = 10,
        channel: str = "",
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

        send_event.channel = channel or (
            self.name if isinstance(event, str) else event.channel
        )

        logger.debug(f"提交消息: {send_event}")
        self._event_queue.put_nowait(send_event)
        if not self._active:
            logger.warning(
                f"{self.__class__.__name__}({self.name}, id-{id(self)})"
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
            logger.debug(f"{self.__class__.__name__}({self.name}) 回复消息: {reply_event}")

        elif event.channel == self._rpc_token and event.reply_to:
            try:
                reply_msg = self.rpc_method.execute(event)
            except Exception as err:
                logger.error(f"RPC调用 {event.type}({event.data}) 发生错误: {err}")
                reply_msg = err

            reply_event = vxEvent(
                type=event.type,
                data=reply_msg,
                channel=event.reply_to,
                reply_to=event.id,
            )
            self._reply_queue.put_nowait(reply_event)
            logger.info(
                f"{self.__class__.__name__}({self.name}) 回复消息: {reply_event.data}"
            )
        elif not event.reply_to:
            self.submit_event(event)
            logger.debug(
                f"{self.__class__.__name__}({self.name}) 触发消息事件: {event.type} =="
                f" {event.data}"
            )
        else:
            logger.warning(
                f"{self.__class__.__name__}({self.name}) 收到非法消息: {event.type} =="
                f" {event.data}"
            )

    def _run_backend(self) -> None:
        logger.info(
            f"{self.__class__.__name__}({self.name} id-({id(self)})) backend 启动运行..."
        )
        while self._active:
            try:
                flags = self._socket.poll(1000, zmq.POLLIN | zmq.POLLOUT)

                if flags & zmq.POLLIN != 0:
                    msg = self._socket.recv_multipart()
                    logger.debug(f"backend recv msg: {len(msg)} {msg}")
                    self._pool.apply_async(
                        self._handle_msg,
                        args=(msg,),
                        error_callback=lambda e: logger.error(e, exc_info=True),
                    )

                if flags & zmq.POLLOUT != 0:
                    with contextlib.suppress(Empty):
                        event = self._reply_queue.get_nowait()
                        self._socket.send_multipart([vxEvent.pack(event)])

            except zmq.ZMQError as e:
                logger.error(f"网络连接错误: {e}")
                self._init_socket(*self._socket_params)

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
                    logger.debug(f"{self.__class__.__name__} 触发 {event.type} 事件...")
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


vxengine = vxEngine()
