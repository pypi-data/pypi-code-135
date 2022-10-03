from typing import Tuple, Dict, Any, List
from .item import Item
from .base import BasicClass
from ..config import Config
from ..context import Context


class ProcessorEvent:
    EVENT_IN = 0
    EVENT_OUT = 1


class Processor(BasicClass):
    def __init__(self, name: str, config: Config, context: Context, scene: Any,
                 process: str, max_size: int = 1) -> None:
        super().__init__(name, config, context, scene)
        self.className = 'Processor'
        self.process = process
        self.max_size = max_size
        self.__init_processor()

    def __init_processor(self):
        """ the items processed by the process need to be pushed to a later buffer """
        self.items_ready: Dict[str, Item] = {}
        """ record events: pos: [(time, event)] """
        self.events: Dict[int, List[Tuple[int, int]]] = {}

    def receive(self, item: Item, t: int, info: Dict = ...):
        if len(self.items) > self.max_size - 1:
            raise RuntimeError(f'Process {self.name} exceeds capacity, cause: {item.name} passed in')
        pos = self.load_one_item(item)
        self.events.setdefault(pos, [])
        self.events[pos].append((t, ProcessorEvent.EVENT_IN))
        self.items.append(item)
        """ processor should be updated with ok_to_push """
        self.ok_to_push = len(self.items) < self.max_size
        """ update the process status of an item """
        item.iteminfo.start_process(
            self.process, t, self.name, self.items_pos[item])

    def check(self, t: int) -> int:
        """ similar to Source """
        res_t = -1
        """ check what is the most recent completion time of all items """
        minv = int(2e9)
        """ clear to ensure that all output in self.items_ready is at the same time """
        self.items_ready: Dict[str, Item] = {}
        for item in self.items:
            in_time = item.iteminfo.times[self.process][0]
            out_time = in_time + item.iteminfo.processor[self.process][1]
            assert in_time <= t and out_time >= t, \
                f"False: {in_time} <= {t} and {out_time} >= {t}"
            minv = min(minv, out_time)
        if minv != int(2e9):
            res_t = minv
        for item in self.items:
            in_time = item.iteminfo.times[self.process][0]
            out_time = in_time + item.iteminfo.processor[self.process][1]
            if out_time == res_t:
                self.items_ready[item.name] = item
        return res_t

    def do(self, t: int) -> Tuple[BasicClass, int]:
        for _, item in self.items_ready.items():
            in_time = item.iteminfo.times[self.process][0]
            out_time = in_time + item.iteminfo.processor[self.process][1]
            if out_time == t and item.iteminfo.times[self.process][1] == -1:
                """ update item status at process completion """
                item.iteminfo.done_process(t)
        for _, item in self.items_ready.items():
            if item.iteminfo.states[self.process] == 2:  # 2 is DONE
                return (self, t)
        return (None, t)

    def flow_to(self, item: Item, p1: int, t: int, info: Dict = ...):
        assert item in self.items
        assert item in self.items_ready.values()
        super().flow_to(item, p1, t, info=info)
        pos = super().unload_one_item(item)
        self.events[pos].append((t, ProcessorEvent.EVENT_OUT))
        del self.items_ready[item.name]
        self.items.remove(item)
        self.ok_to_push = len(self.items) < self.max_size

    def clear(self) -> None:
        super()._clear_items()
        self.__init_processor()
