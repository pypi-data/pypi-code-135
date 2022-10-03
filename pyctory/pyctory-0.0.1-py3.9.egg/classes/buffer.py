import heapq
from typing import List, Tuple, Dict, Any

from .item import Item
from .base import BasicClass
from ..config import Config
from ..context import Context


class Buffer(BasicClass):
    def __init__(self, name: str, config: Config, context: Context, scene: Any) -> None:
        super().__init__(name, config, context, scene)
        self.className = 'Buffer'
        self.__init_buffer()

    def __init_buffer(self):
        """ minimum heap saves (Arrival Time, Item) """
        self.itemHeap: List[Tuple[int, Item]] = []
        """ p1s saves which can be transmitted in downstream"""
        self.p1s: List[int] = []

    def receive(self, item: Item, t: int, info: Dict = ...):
        if len(self.itemHeap) > self.max_size - 1:
            raise RuntimeError(
                f'Buffer {self.name} exceeds capacity, cause: {item.name} passed in')
        self.load_one_item(item)
        self.items.append(item)
        heapq.heappush(self.itemHeap, (t, item))

    def check(self, t: int) -> int:
        res_t: int = -1
        """ buffer transfer condition: downstream can be transferred to """
        self.p1s = []
        for p1 in self.pipe1.keys():
            entity = self.pipe1[p1][0]
            if entity.ok_to_push:
                self.p1s.append(p1)
        if len(self.p1s) != 0 and len(self.items) != 0:
            res_t = t
        return res_t

    def do(self, t: int) -> Tuple[BasicClass, int]:
        if len(self.p1s) != 0 and len(self.items) != 0:
            return (self, t)
        return (None, t)

    def flow_to(self, item: Item, p1: int, t: int, info: Dict = ...):
        assert item in self.items
        super().flow_to(item, p1, t, info=info)
        super().unload_one_item(item)
        self.items.remove(item)
        idx = -1
        for i in range(len(self.itemHeap)):
            if self.itemHeap[i][1] == item:
                idx = i
                break
        assert idx != -1
        del self.itemHeap[idx]
        heapq.heapify(self.itemHeap)

    def clear(self):
        super()._clear_items()
        self.__init_buffer()
