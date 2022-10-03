from typing import List, Dict, Any, Union

from .iteminfo import ItemInfo
from ..config import Config


class Item:
    def __init__(self, name: str, config: Config,
                 process_list: List[str],
                 arrival: int = -1,
                 process_time: Dict[str, int] = {},
                 typ: Union[str, int, None] = None,
                 ) -> None:
        self.name = name
        self.config = config
        self.iteminfo = ItemInfo(process_list, arrival, process_time, typ)
        """ item in which entity """
        self.entity: Any = None

    """ overwrite operator <=, for priority queue (minimum heap) """
    def __lt__(t1, t2) -> bool:
        return t1.iteminfo.arrival < t2.iteminfo.arrival

    def set_entity(self, e: Any, t: int, prev: Any = None) -> None:
        self.entity = e

        if self.config.log_item:
            # if self.name == "003":
            if prev is not None:
                print(f"[{t: >7d}] Item {self.name} entered {e.name} from {prev.name}"
                      f"[pos={self.entity.items_pos[self]}]")
            else:
                print(f"[{t: >7d}] Item {self.name} entered {e.name}"
                      f"[pos={self.entity.items_pos[self]}]")

        """ record data in the format [item.name, time, prev.name, e.name, e.item_pos] """
        event = [self.name, t, None, e.name, self.entity.items_pos[self]]
        if prev is not None:
            event[2] = prev.name
        e.scene.item_events.append(event)
