#!/usr/bin/env python3

from FlightStream.button_types.button_monitor import ButtonMonitor
from FlightStream.renderers.text_render_label_indicator_1 import TextRenderLabelIndicator1
from FlightStream.renderers.text_render_label_indicator_2 import TextRenderLabelIndicator2
from FlightStream.renderers.text_render_label_top_line_1 import TextRenderLabelTopLine1
from FlightStream.renderers.text_render_label_top_line_2 import TextRenderLabelTopLine2
from FlightStream.sources.bool import SourceBoolean
from FlightStream.sources.source import Source


class ButtonThrottle(ButtonMonitor):

    def initialise_instance(self):
        self.set_background(self.COLOUR_INDICATOR)
        self.add_title('Throttle', TextRenderLabelTopLine1())
        # self.add_title('Lever', TextRenderLabelTopLine2())
        source1 = Source()
        source1.set_source('GENERAL_ENG_THROTTLE_LEVER_POSITION:1')
        source1.set_renderer(TextRenderLabelIndicator1())
        self.add_source(source1)
        source2 = Source()
        source2.set_source('TURB_ENG_REVERSE_NOZZLE_PERCENT:1')
        source2.set_renderer(TextRenderLabelIndicator2())
        self.add_source(source2)
# GENERAL_ENG_PCT_MAX_RPM:1
# GENERAL_ENG_THROTTLE_LEVER_POSITION:1

# TURB_ENG_REVERSE_NOZZLE_PERCENT:1
# GENERAL ENG REVERSE THRUST ENGAGED
