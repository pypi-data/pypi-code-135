from typing import Callable, Dict, List

from ..classes import Scene, BasicClass, Processor, Buffer
from .watcher_utils import EntityState


class DataAggerator:
    def __init__(self, sc: Scene) -> None:
        self.sc = sc
        self.config = sc.config
        self.custom_update_funcs: List[Callable] = []
        self.reset()

    def reset(self, clear_custom_update_funcs: bool = False) -> None:
        """
        Record the real-time status of each entity
        Note that one position per processor is considered an entity here and is counted from 0
        """
        self.entity_state_dict: Dict[str, EntityState] = None

        """ information for recording real-time statistics """
        # ensure that the elements in times are in increasing order
        self.times: List[float] = []
        # processor2utilities['process_name_pos=station_number'] = { time_point: utilization }
        self.processor2utilities: Dict[str, Dict[float, float]] = {}
        # buffer2number[buffer name] = { time point: number of workpieces }
        self.buffer2number: Dict[str, Dict[float, int]] = {}

        if clear_custom_update_funcs:
            self.custom_update_func: List[Callable] = []

    def before_first_run(self):
        """
        call before run()
        since we can only know how many entities there are before run()
        """
        self.entity_state_dict = self.__init_entity_state_dict()

    def __init_entity_state_dict(self) -> Dict[str, EntityState]:
        entity_state_dict = {}
        for entity in self.sc.entities.values():
            if isinstance(entity, Processor):
                for pos in range(entity.max_size):
                    name = DataAggerator.__get_entity_state_name(entity, pos)
                    entity_state_dict[name] = EntityState()
            else:
                name = DataAggerator.__get_entity_state_name(entity)
                entity_state_dict[name] = EntityState()
        return entity_state_dict

    @staticmethod
    def __get_entity_state_name(entity: BasicClass, pos: int = -1) -> str:
        if isinstance(entity, Processor):
            return f"{entity.name}_pos={pos}"
        else:
            return entity.name

    def add_custom_update_func(self, custom_update_func: Callable) -> None:
        self.custom_update_funcs.append(custom_update_func)

    def check(self) -> None:
        # update times
        if len(self.times) > 0:
            assert self.times[-1] <= self.sc.time
            if self.times[-1] < self.sc.time:
                self.times.append(float(self.sc.time))
        else:
            self.times.append(float(self.sc.time))
        # update entities status
        for entity in self.sc.entities.values():
            if isinstance(entity, Processor):
                for pos in range(entity.max_size):
                    self.__update_processor_pos(entity, pos)
            elif isinstance(entity, Buffer):
                self.__update_buffer(entity)
        for func in self.custom_update_funcs:
            func(entity)

    def __update_processor_pos(self, entity: Processor, pos: int) -> None:
        """
        Check if the previous state is the same as the current state
        Check whether to update used_time or free_time based on the comparison of the two states
        """
        name = self.__get_entity_state_name(entity, pos)
        entityState = self.entity_state_dict[name]
        entityState.curr_state = EntityState.STATE_BUSY if pos in entity.pos_items.keys(
        ) else EntityState.STATE_IDLE
        if entityState.prev_state == EntityState.STATE_IDLE:
            if entityState.curr_state == EntityState.STATE_BUSY:
                entityState.used_time += self.sc.time - entityState.prev_time
            elif entityState.curr_state == EntityState.STATE_IDLE:
                entityState.free_time += self.sc.time - entityState.prev_time
        elif entityState.prev_state == EntityState.STATE_BUSY:
            if entityState.curr_state == EntityState.STATE_BUSY:
                entityState.used_time += self.sc.time - entityState.prev_time
            elif entityState.curr_state == EntityState.STATE_IDLE:
                entityState.free_time += self.sc.time - entityState.prev_time
        """ update entities status """
        entityState.prev_state = entityState.curr_state
        entityState.prev_time = self.sc.time
        """ update processor2utilities """
        self.processor2utilities.setdefault(name, {})
        self.processor2utilities[name][self.sc.time] = entityState.used_time / self.sc.time \
            if self.sc.time > 0 else 0

    def __update_buffer(self, entity: Buffer) -> None:
        """ records how many backlogged items are in the buffer at the current point in time """
        name = self.__get_entity_state_name(entity)
        self.buffer2number.setdefault(name, {})
        self.buffer2number[name][self.sc.time] = len(entity.items)
