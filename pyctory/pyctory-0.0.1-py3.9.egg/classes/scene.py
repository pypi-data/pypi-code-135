from typing import List, Dict, Callable, Tuple
import heapq
from copy import deepcopy

from .base import BasicClass
from .source import Source
from .buffer import Buffer
from .processor import Processor
from .sink import Sink
from .item import Item
from .connects import connect, disconnect
from ..config import Config
from ..context import Context


class Scene:
    def __init__(self, name: str, config: Config, context: Context) -> None:
        self.name = name
        self.config = config
        self.context = context

        self.render_func: Callable = None

        self.__init_scene()
        self.__reset_scene()

    def __init_scene(self):
        """ entities: {name: entity} """
        self.entities: Dict[str, BasicClass] = {}
        """ graph: {upstream: {downstream: upstream port}} """
        self.graph: Dict[str, Dict[str, int]] = {}
        """ items: {item name: item} """
        self.items: Dict[Item] = {}

        """ save entity """
        self.sources: List[Source] = []
        self.buffers: List[Buffer] = []
        self.processors: List[Processor] = []
        self.sinks: List[Sink] = []

        """ result of each entity after hierarchical traversal """
        self.levels: List[List[str]] = None

    def __reset_scene(self):
        """
        recording the occurrence of each event as an item is the basis of all statistics
        [item.name, time, prev.name, e.name, e.item_pos] """
        self.item_events: List[List] = []

        """ time event """
        self.time = 0
        self.times = []
        """ entity waiting to be decided """
        self.last_entity: BasicClass = None

    def set_render_func(self, render_func: Callable):
        self.render_func = render_func

    def connect(self, up: str, down: str):
        if up in self.graph.keys() and \
                down in self.graph[up].keys():
            raise RuntimeError(f"{up} and {down} are already connected")
        upEntity = self.entities[up]
        downEntity = self.entities[down]
        p1, _ = connect(upEntity, downEntity)
        self.graph.setdefault(up, {})
        self.graph[up][down] = p1

        self.__init_levels()

    def disconnect(self, up: str, down: str):
        if up not in self.graph.keys() or \
                down not in self.graph[up].keys():
            raise RuntimeError(f"no connection between {up} and {down}")
        upEntity = self.entities[up]
        downEntity = self.entities[down]
        disconnect(upEntity, downEntity)
        del self.graph[up][down]
        if len(self.graph[up]) == 0:
            del self.graph[up]

        self.__init_levels()

    def add_source(self, name: str):
        assert name not in self.entities.keys()
        entity = Source(name, self.config, self.context, self)
        self.entities[name] = entity
        self.sources.append(entity)

        self.__init_levels()

    def add_buffer(self, name: str):
        assert name not in self.entities.keys()
        entity = Buffer(name, self.config, self.context, self)
        self.entities[name] = entity
        self.buffers.append(entity)

        self.__init_levels()

    def add_processor(self, name: str, process: str, position: int = 1):
        """
        :params process: category of work process
        :params position: how many work postions in process
        """
        assert name not in self.entities.keys()
        entity = Processor(name, self.config, self.context,
                           self, process, position)
        self.entities[name] = entity
        self.processors.append(entity)

        self.__init_levels()

    def add_sink(self, name: str):
        assert name not in self.entities.keys()
        entity = Sink(name, self.config, self.context, self)
        self.entities[name] = entity
        self.sinks.append(entity)

        self.__init_levels()

    @property
    def legal(self) -> bool:
        """ only legal if Source and Sink exist"""
        flag1, flag2 = False, False
        for _, e in self.entities.items():
            if type(e) == Source:
                flag1 = True
            if type(e) == Sink:
                flag2 = True
        return flag1 and flag2

    @property
    def done(self) -> bool:
        """ only done if all Items are in Sink """
        for _, e in self.entities.items():
            if type(e) != Sink:
                if len(e.items) != 0:
                    return False
        return True

    def run(self,
            global_rule: Callable = None,
            entityName: str = None,
            itemName: str = None,
            info={}
            ) -> Tuple[str, int]:
        """
        If global_rule is not specified,
        it will stop at the point where a decision needs to be made
        and return the process to be decided with the current time;
        then run and wait for entityName and itemName to be passed in
        to determine where and to whom to pass for self.last_entity
        """
        if self.render_func is not None:
            self.render_func()

        if global_rule is not None:
            if entityName is not None or \
                    itemName is not None or \
                    self.last_entity is not None:
                raise RuntimeError(
                    'scheduling rules have been specified, no control data needs to be passed in')

        """ execute external incoming control data """
        if self.last_entity is not None:
            self.last_entity.flow_to(
                item=self.items[itemName],
                p1=self.graph[self.last_entity.name][entityName],
                t=self.time,
                info=info
            )

        """ start scheduling, automatic flow """
        for _, e in self.entities.items():
            t = e.check(self.time)
            if t != -1:
                heapq.heappush(self.times, t)
        while not self.done:
            no_change_flag = True
            for _, e in self.entities.items():
                e, t = e.do(self.time)
                if e is not None:
                    if global_rule is None:
                        self.last_entity = e
                        return (e.name, self.time)
                    else:
                        entityName, itemName = global_rule(
                            self, e.name, self.time)
                        e.flow_to(
                            item=self.items[itemName],
                            p1=self.graph[e.name][entityName],
                            t=self.time,
                            info=info
                        )
            if self.render_func is not None:
                self.render_func()
            for _, e in self.entities.items():
                t = e.check(self.time)
                if t != -1:
                    if t == self.time:
                        no_change_flag = False
                    if t not in self.times:
                        heapq.heappush(self.times, t)
            if no_change_flag:
                if len(self.times) == 0:
                    assert self.done
                    return (None, self.time)
                self.time = heapq.heappop(self.times)
        return (None, self.time)

    def __init_levels(self):
        self.levels = []

        st = {}
        for e in self.entities.keys():
            st[e] = False

        queue = []
        for e in self.sources:
            queue.append(e.name)
        while len(queue) > 0:
            prev = deepcopy(queue)
            self.levels.append(prev)
            queue = []
            for p in prev:
                if p not in self.graph.keys():
                    continue
                for t, _ in self.graph[p].items():
                    if st[t]:
                        continue
                    queue.append(t)
                    st[t] = True

    def clear(self):
        self.__reset_scene()
        for _, e in self.entities.items():
            e.clear()
