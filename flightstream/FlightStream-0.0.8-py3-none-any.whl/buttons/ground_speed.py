#!/usr/bin/env python3

from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1
from FlightStream.sources.source import Source


class ButtonGroundSpeed(ButtonMonitor):

    def initialise_instance(self):
        self.set_background(self.COLOUR_INDICATOR)
        self.add_title('GS', TextRenderLabelTopLine1())
        source1 = Source()
        source1.set_source('GROUND_VELOCITY')
        source1.set_frequency(1000)
        self.add_source(source1)
