#!/usr/bin/env python3

from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1
from FlightStream.sources.flight_level import SourceFlightLevel


class ButtonAltitude(ButtonMonitor):

    def initialise_instance(self):
        self.set_background(self.COLOUR_INDICATOR)
        self.add_title('ALT', TextRenderLabelTopLine1())
        source1 = SourceFlightLevel()
        source1.set_source('PLANE_ALT_ABOVE_GROUND')
        self.add_source(source1)
# PLANE_ALTITUDE
# RADIO_HEIGHT