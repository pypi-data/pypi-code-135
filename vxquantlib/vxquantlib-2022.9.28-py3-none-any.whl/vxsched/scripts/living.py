"""实时消息处理引擎"""


from abc import ABCMeta, abstractmethod
import contextlib
from typing import List
from queue import Empty
from multiprocessing.dummy import Process
from vxutils import logger, vxtime
from vxsched import (
    vxhandlers,
    vxOnceTrigger,
    vxEventHandlers,
    vxChannel,
    vxLocalEventBroker,
)


__all__ = ["vxSingleThreadLivingEngine", "vxMultiThreadsLivingEngine"]


class vxLivingEngine(metaclass=ABCMeta):
    """实时消息处理引擎"""

    def __init__(self, handlers: vxEventHandlers) -> None:
        pass

    @abstractmethod
    def start(self, channels: List[vxChannel], **kwargs) -> None:
        """启动函数"""

    @abstractmethod
    def stop(self, *args, **kwargs) -> None:
        """暂停函数"""


class vxSingleThreadLivingEngine(vxLivingEngine):
    """单线程消息处理引擎"""

    def __init__(self, handlers: vxEventHandlers) -> None:

        self._handlers = handlers
        self._active = False

    def _run(self, channels: List[vxChannel]):
        logger.info("=" * 30)
        for channel in channels:
            logger.info(f"开始运行...监听通道{channel}")

        while self._active:
            now = vxtime.now()
            for channel in channels:
                with contextlib.suppress(Empty):
                    event = channel.get(now)
                    self._handlers.trigger(event)
            vxtime.sleep(1)

    def start(self, channels) -> None:
        """开始执行"""
        if self._active:
            logger.warning(f"当前引擎正在运行中，请停止后再试{self._active}")
            return

        self._active = True
        try:
            self._run(channels)
        finally:
            self.stop()

    def stop(self) -> None:
        """停止执行"""
        self._active = False


class vxMultiThreadsLivingEngine(vxLivingEngine):
    """多线程实时消息引擎"""

    def __init__(self, handlers: vxEventHandlers) -> None:

        self._handlers = handlers
        self._active = False
        self._processes = None

    def _run(self, channel) -> None:
        logger.info("=" * 30)
        logger.info(f"开始运行...监听通道{channel}")
        while self._active:
            now = vxtime.now()
            with contextlib.suppress(Empty):
                event = channel.get(now)
                self._handlers.trigger(event)

    def start(self, channels: List[vxChannel], blocking=False) -> None:
        """开始执行引擎

        Arguments:
            channels {List[vxChannel]} -- 需要监听的消息通道

        Keyword Arguments:
            blocking {bool} -- 是否阻断，如果为否，则不阻断 (default: {False})
        """
        self._active = True

        try:
            self._processes = [
                Process(target=self._run, args=(channel,)) for channel in channels
            ]
            list(map(lambda p: p.start(), self._processes))

            if blocking:
                [lambda p: p.join() for p in self._processes if p.is_alive()]

        except Exception as e:
            logger.info(f"======={e}")
            self.stop()

    def stop(self):
        """停止引擎"""
        self._active = False
        [lambda p: p.join() for p in self._processes if p.is_alive()]


def main(multithreads=True, config_file="./etc/config.json", mod_dir=""):
    """主函数

    Keyword Arguments:
        multithreads {bool} -- 是否使用多线程版本 (default: {True})
        config_file {str} -- 配置文件 (default: {'./etc/config.json'})
        mod_dir {str} -- 策略模块存放目录 (default: {''})
    """


if __name__ == "__main__":
    from vxsched import vxIntervalTrigger

    @vxhandlers("test1")
    def test_basic(context, event, tools) -> None:
        print("=" * 60)
        # print(context)
        print(event)
        # print(tools)

    @vxhandlers("2222")
    def test_basic2(context, event, tools) -> None:
        print("=" * 60)
        # print(context)
        print(event)
        # print(tools)

    sched = vxMultiThreadsLivingEngine(vxhandlers)
    evnet_broker = vxLocalEventBroker()
    channel = vxChannel("gateway", evnet_broker)
    channel.put("test1", trigger=vxIntervalTrigger(3))
    channel.put("2222", trigger=vxOnceTrigger(vxtime.now() + 12))
    sched.start(channels=[channel] * 5)
