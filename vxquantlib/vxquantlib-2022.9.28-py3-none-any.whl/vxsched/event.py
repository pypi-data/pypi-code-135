"""消息类型"""

import uuid
from collections import defaultdict
from heapq import heappush, heappop
from enum import Enum
from multiprocessing import Lock
from queue import Queue, Empty, Full
from typing import Iterator, Optional, Any
from abc import ABCMeta, abstractmethod


from vxutils import to_timestring, to_json, vxtime, logger, vxJSONEncoder
from vxutils.dataclass import (
    vxDataClass,
    vxIntField,
    vxDatetimeField,
    vxField,
    vxUUIDField,
)


__all__ = ["vxEvent", "vxEventQueue", "vxTrigger", "TriggerStatus"]


class TriggerStatus(Enum):
    """触发器状态

    Pending : 未开始
    Running : 已开始
    Completed: 已完成
    """

    Pending = 1  #  未开始
    Running = 2  #  已开始
    Completed = 3  #  已完成


class vxTrigger(Iterator[float], metaclass=ABCMeta):
    """触发器"""

    __slots__ = (
        "_last_trigger_dt",
        "_end_dt",
    )

    def __init__(self, end_dt=None):
        self._last_trigger_dt = None
        self._end_dt = end_dt or float("inf")

    @property
    def last_trigger_dt(self) -> Optional[float]:
        """最后一次执行日期，若未空，则未开始执行"""
        return self._last_trigger_dt

    @property
    def next_trigger_dt(self) -> Optional[float]:
        """下一次执行日期"""
        return self.get_next_trigger_dt()

    @property
    def end_dt(self) -> float:
        """下一次执行时间"""
        return self._end_dt

    @abstractmethod
    def get_next_trigger_dt(self) -> Optional[float]:
        """
        返回下一次执行timestamp，如果没有下次执行时间，则返回 'None'
        """

    def __getstate__(self) -> dict:
        """序列化函数"""
        return {key: getattr(self, key) for key in self.__slots__}

    def __setstate__(self, state: dict) -> None:
        """反序列化函数"""
        for key in self.__slots__:
            setattr(self, key, state[key])

    def __str__(self) -> str:
        return f"< {self.__class__.__name__} (id-{id(self)}): {to_json(self.message)}"

    __repr__ = __str__

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> float:
        now = vxtime.now()
        if self._end_dt and now > self._end_dt:
            raise StopIteration

        while self.get_next_trigger_dt() is not None:
            self._last_trigger_dt = self.get_next_trigger_dt()
            if self._last_trigger_dt > now:
                return self._last_trigger_dt

        raise StopIteration

    @property
    def message(self) -> dict:
        """trigger内部内容"""

        return {
            "last_trigger_dt": to_timestring(self.last_trigger_dt),
            "next_trigger_dt": to_timestring(self.get_next_trigger_dt()),
            "end_dt": to_timestring(self.end_dt),
            "status": self.status,
        }

    @property
    def status(self) -> TriggerStatus:
        """是否已完成"""

        if not self.last_trigger_dt:
            return TriggerStatus.Pending
        elif not self.next_trigger_dt:
            return TriggerStatus.Completed
        return TriggerStatus.Running


class vxEvent(vxDataClass):
    """消息类型"""

    __sortkeys__ = ("next_trigger_dt", "priority")

    # 消息id
    id: str = vxUUIDField(auto=True)
    # 消息通道
    channel: str = vxField("")
    # 消息类型
    type: str = vxField("", str)
    # 消息内容
    data: Any = vxField("")
    # 定时触发器
    trigger: Optional[vxTrigger] = vxField()
    # 下次触发事件
    next_trigger_dt: float = vxDatetimeField()
    # 优先级
    priority: int = vxIntField(10)
    # rpc消息回复地址
    reply_to: str = vxUUIDField(auto=False)


@vxJSONEncoder.register(vxTrigger)
def _(obj):
    return obj.message


class vxEventQueue(Queue):
    def _init(self, maxsize=0):
        self.queue = []
        self._event_ids = set()

    def _qsize(self):
        now = vxtime.now()
        return len([event for event in self.queue if event.next_trigger_dt <= now])

    def _put(self, event):
        if isinstance(event, str):
            event = vxEvent(type=event)

        if not isinstance(event, vxEvent):
            raise ValueError(f"Not support type(event) : {type(event)}.")

        if event.id in self._event_ids:
            raise ValueError(f"event({event.id})重复入库. {event}")

        if event.trigger and event.trigger.status.name == "Pending":
            event.next_trigger_dt = next(event.trigger, vxtime.now())

        heappush(self.queue, event)
        self._event_ids.add(event.id)

    def get(self, block=True, timeout=None):
        with self.not_empty:
            if not block:
                if not self._qsize():
                    raise Empty
            elif timeout is None:
                while not self._qsize():
                    remaining = 1
                    if len(self.queue) > 0:
                        remaining = self.queue[0].next_trigger_dt - vxtime.now()

                    if remaining > 0:
                        self.not_empty.wait(remaining)

            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = vxtime.now() + timeout
                while not self._qsize():
                    if len(self.queue) > 0:
                        min_endtime = min(endtime, self.queue[0].next_trigger_dt)
                    else:
                        min_endtime = endtime

                    remaining = min_endtime - vxtime.now()

                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)
            event = self._get()
            self.not_full.notify()
            return event

    def _get(self):
        event = heappop(self.queue)

        last_trigger_dt = event.next_trigger_dt
        if event.trigger and event.trigger.status.name != "Completed":
            event.next_trigger_dt = next(event.trigger, None)
            heappush(self.queue, event)
            self.unfinished_tasks += 1
            self.not_empty.notify()
        else:
            self._event_ids.remove(event.id)

        # 获取的event都将trigger给去掉，以免trigger在其他地方再进行传递
        reply_event = vxEvent(**event.message)
        reply_event.trigger = None
        reply_event.next_trigger_dt = last_trigger_dt
        return reply_event
