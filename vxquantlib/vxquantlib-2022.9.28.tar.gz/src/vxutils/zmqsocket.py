"""zeromq 相关函数"""


import asyncio
from multiprocessing import Lock
import os
import pickle
import pathlib
import secrets
from typing import Any
import zmq
from zmq.auth import CURVE_ALLOW_ANY
from zmq.auth.thread import ThreadAuthenticator

from zmq.asyncio import Context as AsyncContext
from zmq.asyncio import Socket as AsyncSocket
from zmq.auth.asyncio import AsyncioAuthenticator

from vxutils import logger


__all__ = [
    "vxZMQContext",
    "vxSecSocket",
    "vxAsyncSecSocket",
    "vxAsyncZMQContext",
    "vxZMQRequest",
    # "reliable_request",
]


class vxSecSocket(zmq.Socket):
    """构建加密的ZMQ socket链接工具集合"""

    __auth_thread__ = None
    __authsocket_cnt__ = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__["secret_mode"] = False
        # self.curve_publickey = b""
        # self.curve_secretkey = b""
        # self.curve_serverkey = b""
        self.__dict__["_lock"] = Lock()
        self.__dict__["_server_public"] = None

    @property
    def lock(self):
        """锁"""
        return self.__dict__["_lock"]

    def _start_auth(self, secret_key) -> None:
        """开启auth"""
        if self.__class__.__auth_thread__ is None:
            self.__class__.__auth_thread__ = ThreadAuthenticator()
            self.__class__.__auth_thread__.start()
            self.__class__.__auth_thread__.configure_curve(
                domain="*", location=CURVE_ALLOW_ANY
            )
            self.__class__.__auth_thread__.allow()

        if not self.__dict__["secret_mode"]:
            self.__class__.__authsocket_cnt__ += 1
            public_keystr, secret_keystr = zmq.auth.load_certificate(secret_key)
            self.curve_publickey = public_keystr
            self.curve_secretkey = secret_keystr
            self.curve_server = True
            self.__dict__["secret_mode"] = True
            logger.info(f"{self} 启动加密模式, server public key: {public_keystr}.")

    def _stop_auth(self) -> None:
        """暂停auth"""
        if self.__dict__["secret_mode"]:
            self.__class__.__authsocket_cnt__ = max(
                self.__class__.__authsocket_cnt__ - 1, 0
            )
            self.curve_server = False
            self.__dict__["secret_mode"] = False

    def bind(self, addr: str, secret_key: str = ""):
        if secret_key and pathlib.Path(secret_key).is_file():
            self._start_auth(secret_key)

        ret = super().bind(addr)
        logger.info(f"绑定 {addr} 完成.{ret}")
        return ret

    def unbind(self, addr: str) -> None:
        """取消绑定

        Arguments:
            addr {str} -- 取消绑定的地址

        """
        self._stop_auth()
        return super().unbind(addr)

    def connect(self, addr: str = "", public_key: str = ""):
        """创建连接服务器socket

        Keyword Arguments:
            addr {str} -- 服务器地址 (default: {""})
            public_key {str} -- 服务器公钥 (default: {""})

        """
        if zmq.zmq_version_info() < (4, 0):
            logger.warning(
                "Security is not supported in libzmq version < 4.0. libzmq version"
                f" {zmq.zmq_version()}"
            )
            public_key = None

        server_public = self.__dict__.get("_server_public", None)
        if public_key and os.path.exists(public_key):
            server_public, _ = zmq.auth.load_certificate(public_key)
            self.__dict__["_server_public"] = server_public

        if server_public:
            self.curve_serverkey = server_public
            self.curve_publickey, self.curve_secretkey = zmq.curve_keypair()
            logger.info(f"启动加密模式,public server public key: {server_public}.")

        ret = super().connect(addr)
        logger.info(f"connect to {addr} ...")
        return ret

    def close(self, linger: int = None):
        super().close(linger)
        self._stop_auth()
        if self.__class__.__authsocket_cnt__ == 0 and self.__class__.__auth_thread__:
            self.__class__.__auth_thread__.stop()
            self.__class__.__auth_thread__ = None


class vxZMQContext(zmq.Context):
    """ZMQ context"""

    _socket_class = vxSecSocket


class vxAsyncSecSocket(AsyncSocket):
    """构建加密的ZMQ socket链接工具集合"""

    __auth_thread__ = None
    __authsocket_cnt__ = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.curve_server = False
        self._lock = asyncio.Lock()

    def _start_auth(self, secret_key) -> None:
        """开启auth"""

        self.__class__.__authsocket_cnt__ += 1

        if not self.__class__.__auth_thread__:
            self.__class__.__auth_thread__ = AsyncioAuthenticator()
            self.__class__.__auth_thread__.start()
            self.__class__.__auth_thread__.configure_curve(
                domain="*", location=CURVE_ALLOW_ANY
            )
            self.__class__.__auth_thread__.allow()

        self.__class__.__authsocket_cnt__ += 1
        public_keystr, secret_keystr = zmq.auth.load_certificate(secret_key)
        self.curve_publickey = public_keystr
        self.curve_secretkey = secret_keystr
        self.curve_server = True

    def _stop_auth(self) -> None:
        """暂停auth"""
        if self.curve_server:
            self.__class__.__authsocket_cnt__ = max(
                self.__class__.__authsocket_cnt__ - 1, 0
            )
            self.curve_server = False

    def bind(self, addr: str, secret_key: str = ""):
        if not secret_key:
            self._stop_auth()
            logger.info("非加密方式bind: 未指定secret key文件")
        elif not pathlib.Path(secret_key).is_file():
            self._stop_auth()
            logger.info(f"非加密方式bind: {secret_key} 文件不存在")
        else:
            self._start_auth(secret_key)
            logger.info(f"启动加密模式,secret key文件: {secret_key}.")

        logger.info(f"绑定 {addr} 完成.")
        return super().bind(addr)

    def unbind(self, addr: str) -> None:
        """取消绑定

        Arguments:
            addr {str} -- 取消绑定的地址

        """
        self._stop_auth()
        return super().unbind(addr)

    def connect(self, addr: str = "", public_key: str = ""):
        """创建连接服务器socket

        Keyword Arguments:
            addr {str} -- 服务器地址 (default: {""})
            public_key {str} -- 服务器公钥 (default: {""})

        """
        if zmq.zmq_version_info() < (4, 0):
            logger.warning(
                "Security is not supported in libzmq version < 4.0. libzmq version"
                f" {zmq.zmq_version()}"
            )
            public_key = None

        if public_key and os.path.exists(public_key):
            server_public, _ = zmq.auth.load_certificate(public_key)
            self.curve_serverkey = server_public
            self.curve_publickey, self.curve_secretkey = zmq.curve_keypair()
            logger.info(f"启动加密模式,server public key文件: {public_key}.")

        logger.info(f"链接 {addr} 完成.")
        return super().connect(addr)

    def close(self, linger: int = 0):
        super().close(linger)
        self._stop_auth()
        if self.__class__.__authsocket_cnt__ == 0 and self.__class__.__auth_thread__:
            self.__class__.__auth_thread__.stop()
            self.__class__.__auth_thread__ = None


class vxAsyncZMQContext(AsyncContext):
    """ZMQ context"""

    _socket_class = vxAsyncSecSocket


class vxZMQRequest:
    def __init__(
        self,
        url: str,
        public_key: str,
        serializer=None,
        deserializer=None,
        retry_times=5,
    ) -> None:
        self._clientid = secrets.token_bytes(16)
        self._url = url
        self._public_key = public_key
        self._ctx = None
        self._socket = None
        self._serializer = serializer or pickle.dumps
        self._deserializer = deserializer or pickle.loads
        self._retry_times = retry_times

    @property
    def socket(self):
        if self._socket is None:
            self._ctx = vxZMQContext().instance()
            self._socket = self._ctx.socket(zmq.REQ)
            self._socket.setsockopt(zmq.IDENTITY, self._clientid)
            self._socket.connect(self._url, self._public_key)

        return self._socket

    def destory(self) -> None:
        """销毁链接"""
        try:
            if self._socket:
                # self._socket.disconnect(self._url)
                self._socket.setsockopt(zmq.LINGER, 0)
                self._socket.close()

        except zmq.ZMQError as e:
            logger.warning(f"断开连接出错: {e}", exc_info=True)

        finally:
            self._socket = None

    def __str__(self) -> str:
        return f"< {self.__class__.__name__} (id-{id(self)}) connect to {self._url}."

    def __call__(self, obj) -> Any:
        packed_obj = obj if isinstance(obj, bytes) else self._serializer(obj)
        delay_time = 3000
        for i in range(self._retry_times):
            try:
                with self.socket.lock:
                    self.socket.send(packed_obj)
                    if self.socket.poll(delay_time, zmq.POLLIN):
                        packed_obj = self.socket.recv()
                        return self._deserializer(packed_obj)
            except zmq.ZMQError as err:
                logger.warning(f"socket 发送消息失败.{err}")

            self.destory()
            if i < self._retry_times - 1:
                delay_time += 1000
                logger.warning(f"准备第{i+1}次重试")
        raise TimeoutError(f"重试{self._retry_times}超时失败")
