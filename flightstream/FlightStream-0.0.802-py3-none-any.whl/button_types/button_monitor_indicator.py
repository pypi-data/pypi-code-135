#!/usr/bin/env python3

from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.renderers.drawing_renderer import DrawingRenderer
from FlightStream.sources.bool import SourceBoolean


class ButtonMonitorIndicator(ButtonMonitor):

    def get_value_renderer(self, index):
        return None

    def show_lamp(self):
        if self.has_sources() == False:
            return False
        for index in range(self.get_source_count()):
            source = self.get_source(index)
            if isinstance(source, SourceBoolean):
                return source.get_sim_hook_value_as_bool()
        return False
