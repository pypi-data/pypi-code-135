from typing import Tuple, Dict, Any, List

from .item import Item
from ..config import Config
from ..context import Context


class BasicClass:
    def __init__(self, name: str, config: Config, context: Context, scene: Any = None) -> None:
        self.name: str = name
        self.config: Config = config
        self.context: Context = context
        self.className: str = 'None'
        self.scene: Any = scene
        self.max_size: int = 9999999
        self.pipe0: Dict[int, Tuple[BasicClass, int]] = {}
        self.pipe1: Dict[int, Tuple[BasicClass, int]] = {}
        self._clear_items()

    def _clear_items(self) -> None:
        self.items: List[Item] = []
        self.items_pos: Dict[Item, int] = {}
        self.pos_items: Dict[int, Item] = {}
        """ ok_to_push: for processor to help buffer judge whether it's ok to flow item """
        self.ok_to_push: bool = True

    def load_one_item(self, item: Item, pos: int = None) -> int:
        """ add item to self.items_pos, assign postions """
        if pos is None:
            for pos in range(len(self.items_pos) + 1):
                if pos not in self.items_pos.values():
                    self.pos_items[pos] = item
                    self.items_pos[item] = pos
                    return pos
        else:
            assert pos not in self.items_pos.values()
            assert pos not in self.pos_items.keys()
            self.items_pos[item] = pos
            self.pos_items[pos] = item
            return pos
        raise RuntimeError(f"no postion for {item.name} in {self.name}")

    def unload_one_item(self, item: Item):
        """ pick item from self.items_pos and clear its position """
        if item not in self.items_pos.keys() or \
                self.items_pos[item] not in self.pos_items.keys():
            raise RuntimeError(f"{item.name} is not in {self.name}")
        pos: int = self.items_pos[item]
        del self.pos_items[pos]
        del self.items_pos[item]
        return pos

    def check(self, t: int) -> int:
        """
        Detects if a new event can be generated or completed at the current moment
        -1 means that no new events have been generated at the current moment
        """
        raise NotImplementedError

    def do(self, t: int) -> Tuple[Any, int]:
        """ Operate the events that can be operated at the current moment """
        raise NotImplementedError

    def clear(self) -> None:
        raise NotImplementedError

    def flow_to(self, item: Item, p1: int, t: int, info: Dict = {}):
        assert p1 in self.pipe1.keys()
        downStream = self.pipe1[p1][0]
        downStream_p0 = self.pipe1[p1][1]
        assert downStream.pipe0[downStream_p0][0] == self
        assert downStream.pipe0[downStream_p0][1] == p1
        assert len(downStream.items) < downStream.max_size

        assert item in self.items_pos.keys()
        assert self.pos_items[self.items_pos[item]] == item
        downStream.receive(item, t, info)
        item.set_entity(downStream, t, self)

    def receive(self, item: Item, t: int, info: Dict = {}):
        """ The receiver passively receives the item item """
        raise NotImplementedError
