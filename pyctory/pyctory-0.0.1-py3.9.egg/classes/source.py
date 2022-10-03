from typing import Dict, List, Any, Tuple
import heapq
from .item import Item
from .base import BasicClass
from ..config import Config
from ..context import Context


class Source(BasicClass):
    def __init__(self, name: str, config: Config, context: Context, scene: Any) -> None:
        super().__init__(name, config, context, scene)
        self.className = 'Source'
        self.__init_source()

    def __init_source(self):
        """ self.items is a mininum heap maintains the item objects ready to be popped """
        self.items: List[Item] = []
        """
        determine if there is an item to be popped,
        and use the list to handle items that arrive at the same time
        """
        self.items_ready: Dict[str, Item] = {}

        self.process_list: List[str] = \
            self.context.source_item_dict['process_list']
        for k, v in self.context.source_item_dict.items():
            if k != 'process_list':
                _arrival = v['arrival']
                v.setdefault('typ', None)
                _typ = v['typ']
                item = Item(k, self.config, self.process_list,
                            _arrival, v, _typ)
                heapq.heappush(self.items, item)
                self.load_one_item(item, pos=len(self.items) - 1)
                self.scene.items[item.name] = item

        """ how many items of each typ have been generated """
        self.typ_count: Dict[str, int] = {}

    def check(self, t: int) -> int:
        if len(self.items) == 0:
            return -1
        assert t <= self.items[0].iteminfo.arrival
        """ nothing happens, return res_t = -1 """
        res_t = -1

        """ if the next popup item is not yet scheduled, schedule the next popup time event """
        if len(self.items_ready) == 0 and len(self.items) != 0:
            self.items_ready[self.items[0].name] = self.items[0]
            res_t = self.items[0].iteminfo.arrival
            """ if there are items that arrive at the same time """
            for i in range(1, len(self.items)):
                item = self.items[i]
                if item.iteminfo.arrival > res_t:
                    break
                self.items_ready[item.name] = item
        elif len(self.items_ready) != 0 and \
                t == list(self.items_ready.values())[0].iteminfo.arrival:
            """
            if the next pop-up item set is already available,
            then there are items arriving at the same time and
            the event will be triggered if and only if the current moment
            """
            res_t = list(self.items_ready.values())[0].iteminfo.arrival
        return res_t

    def do(self, t: int) -> Tuple[BasicClass, int]:
        if len(self.items) == 0:
            return (None, t)
        assert t <= self.items[0].iteminfo.arrival

        if len(self.items_ready) != 0 and \
                list(self.items_ready.values())[0].iteminfo.arrival == t:
            for _, v in self.items_ready.items():
                if v.entity != self:
                    v.set_entity(self, t)
            return (self, t)

        return (None, t)

    def flow_to(self, item: Item, p1: int, t: int, info: Dict = ...):
        assert item in self.items_ready.values()
        super().flow_to(item, p1, t, info=info)
        super().unload_one_item(item)
        del self.items_ready[item.name]
        self.items.remove(item)
        heapq.heapify(self.items)

        if item.iteminfo.typ is not None:
            self.typ_count.setdefault(item.iteminfo.typ, 0)
            self.typ_count[item.iteminfo.typ] += 1
        else:
            self.typ_count.setdefault(0, 0)
            self.typ_count[0] += 1

    def receive(self, item: Item, t: int, info: Dict = ...):
        return None

    def clear(self):
        super()._clear_items()
        self.__init_source()
