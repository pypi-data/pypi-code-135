from typing import Tuple, Dict, Any

from .item import Item
from .base import BasicClass
from ..config import Config
from ..context import Context


class Sink(BasicClass):
    def __init__(self, name: str, config: Config, context: Context, scene: Any) -> None:
        super().__init__(name, config, context, scene)
        self.className = 'Sink'

    def receive(self, item: Item, t: int, info: Dict = ...):
        self.items.append(item)
        self.load_one_item(item)
        item.iteminfo.done_time = t

    def check(self, t: int) -> int:
        return -1

    def do(self, t: int) -> Tuple[BasicClass, int]:
        return (None, t)

    def flow_to(self, item: Item, p1: int, t: int, info: Dict = ...):
        return super().flow_to(item, p1, t, info=info)

    def clear(self) -> None:
        super()._clear_items()
