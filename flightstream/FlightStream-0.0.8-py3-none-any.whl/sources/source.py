#!/usr/bin/env python3

from mimetypes import init
from types import NoneType
from FlightStream.renderers.renderer import Renderer
from FlightStream.renderers.text_render_label_indicator import TextRenderLabelIndicator


class Source():

    def __init__(self):
        self.source_name = None
        self.frequency = 2000
        self.renderer = TextRenderLabelIndicator()
        self.last_value = ''
        self.sim_hook = None
        self.initialise_subclass()
        self.initialise_instance()

    def initialise_subclass(self):
        pass

    def initialise_instance(self):
        pass

    def has_changed(self) -> bool:
        if self.has_renderer() == None:
            return False
        value = self.get_value_formatted()
        if self.last_value != value:
            # print('Source {} was {}, now {}'.format(
            #     self.source_name, self.last_value, value))
            return True
        return False

    def has_renderer(self) -> bool:
        return self.renderer != None

    def get_source_name(self) -> None | str:
        return self.source_name

    def get_frequency(self):
        return self.frequency

    def get_renderer(self) -> Renderer:
        return self.renderer

    def get_last_value(self):
        return self.last_value

    def get_sim_hook(self):
        return self.sim_hook

    def get_sim_value(self):
        self.last_value = self.get_value_formatted()
        return self.last_value

    def get_value_formatted(self):
        value = self.get_sim_hook_value_as_int()
        if value == None:
            return ''
        return value

    def get_sim_hook_value_as_int(self) -> None | int:
        value = self.get_sim_hook_value()
        if value == None:
            return None
        return int(value)

    def get_sim_hook_value(self):
        if isinstance(self.sim_hook, NoneType) or self.sim_hook == None:
            return None
        try:
            # print('Read {} is {}'.format(self.get_title(), sim_hook.value))
            return self.sim_hook.value
        except Exception as e:
            print(e)
            return None

    def set_source(self, source: str):
        self.source_name = source

    def set_frequency(self, frequency: int):
        self.frequency = frequency

    def clear_renderer(self):
        self.renderer = None

    def set_renderer(self, renderer: Renderer):
        self.renderer = renderer

    def set_last_value(self, last_value):
        self.last_value = last_value

    def set_sim_hook(self, sim_hook):
        self.sim_hook = sim_hook
