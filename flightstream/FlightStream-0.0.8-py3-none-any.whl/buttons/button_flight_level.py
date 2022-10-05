#!/usr/bin/env python3

from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1
from FlightStream.sources.flight_level import SourceFlightLevel


class ButtonFlightLevel(ButtonMonitor):

    def initialise_instance(self):
        self.set_background(self.COLOUR_INDICATOR)
        self.add_title('FL', TextRenderLabelTopLine1())
        source = SourceFlightLevel()
        source.set_source('AUTOPILOT_ALTITUDE_LOCK_VAR')
        self.add_source(source)
