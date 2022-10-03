from typing import Callable, Dict, Union

from .utils import load_data, DataAggerator
from .classes import Scene, Source, Buffer, Processor, Sink
from .config import Config
from .context import Context


class Factory:
    def __init__(self,
                 name: str,
                 config: Config = None,
                 schedule_rule: Callable = None,
                 items: Union[str, dict] = None) -> None:
        self.config = Config()
        if config is not None:
            self.config = config
        self.context = self.__init_context(items)
        self.scene = Scene(name=name, config=self.config, context=self.context)
        self.schedule_rule = schedule_rule
        self.data_aggerator = DataAggerator(self.scene)
        self.__init_scene()

    def __init_context(self, items: dict) -> Context:
        context = Context()
        context.source_item_dict = items
        return context

    def __init_scene(self) -> None:
        # run_entityName: return value for run() function
        self.run_entityName = None

    def set_items(self, items: Union[str, dict]) -> None:
        if isinstance(items, str):
            self.context.source_item_dict = load_data(items)
        elif isinstance(items, dict):
            self.context.source_item_dict = items
        else:
            raise TypeError(f"items ({type(items)}) must be str or dict")
        for e in self.scene.entities.values():
            if isinstance(e, Source):
                e.clear()

    def connect(self, up: str, down: str) -> None:
        assert self.scene.last_entity is None, "organization can't be changed after running"
        self.scene.connect(up, down)

    def disconnect(self, up: str, down: str) -> None:
        assert self.scene.last_entity is None, "organization can't be changed after running"
        self.scene.disconnect(up, down)

    def add_source(self, name: str) -> Source:
        assert self.scene.last_entity is None, "organization can't be changed after running"
        self.scene.add_source(name)
        return self.scene.entities[name]

    def add_buffer(self, name: str) -> Buffer:
        assert self.scene.last_entity is None, "organization can't be changed after running"
        self.scene.add_buffer(name)
        return self.scene.entities[name]

    def add_processor(self, name: str, process: str, position: int = 1) -> Processor:
        assert self.scene.last_entity is None, "organization can't be changed after running"
        self.scene.add_processor(name, process, position)
        return self.scene.entities[name]

    def add_sink(self, name: str) -> Sink:
        assert self.scene.last_entity is None, "organization can't be changed after running"
        self.scene.add_sink(name)
        return self.scene.entities[name]

    def reset(self) -> None:
        self.scene.clear()
        self.__init_scene()
        self.data_aggerator.reset()

    def add_custom_update_func(self, custom_update_func: Callable) -> None:
        self.data_aggerator.add_custom_update_func(custom_update_func)

    def set_render_func(self, render_func: Callable) -> None:
        self.scene.set_render_func(render_func)

    @property
    def processor2utilities(self) -> Dict[str, Dict[float, float]]:
        """ processor2utilities['process_name_pos=station_number'] = { time_point: utilization } """
        return self.data_aggerator.processor2utilities

    @property
    def buffer2number(self) -> Dict[str, Dict[float, int]]:
        """ buffer2number[buffer name] = { time point: number of workpieces } """
        return self.data_aggerator.buffer2number

    @property
    def done(self) -> bool:
        return self.scene.done

    def step(self,
             entityName: str = None,
             itemName: str = None) -> None:
        assert not self.scene.done

        """ call run() once for the initial step() calling """
        if self.scene.last_entity is None:
            self.data_aggerator.before_first_run()
            self.data_aggerator.check()
            self.run_entityName, _ = self.scene.run()
            self.data_aggerator.check()
            return None

        if self.schedule_rule is not None:
            assert entityName is None and itemName is None, \
                "no need to pass entityName and itemName," + \
                f"since self.schedule_rule<{self.schedule_rule}> is set"
            entityName, itemName = self.schedule_rule(
                self.scene, self.run_entityName, self.scene.time)
            self.data_aggerator.check()
            self.run_entityName, _ = self.scene.run(None, entityName, itemName)
            self.data_aggerator.check()
            return None
        else:
            """ according to entityName and itemName, put item to entity """
            self.data_aggerator.check()
            self.run_entityName, _ = self.scene.run(None, entityName, itemName)
            self.data_aggerator.check()
            return None
