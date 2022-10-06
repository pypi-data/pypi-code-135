#!/usr/bin/env python3

from FlightStream.renderers.indicator_green import RendererIndicatorGreen
from FlightStream.sources.source import Source


class SourceBoolean(Source):

    def initialise_subclass(self):
        self.set_renderer(RendererIndicatorGreen())

    def get_value_formatted(self):
        value = self.get_sim_hook_value_as_bool()
        if value == None:
            return ''
        return value

    def get_sim_hook_value_as_bool(self) -> bool:
        value = self.get_sim_hook_value_as_int()
        if value == None:
            return False
        return value == 1
